import json
import os
import sqlite3
from datetime import datetime

# Garante que o banco seja salvo dentro da pasta ERP-NOVO/data/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_USER_PATH = os.path.join(DATA_DIR, "usuarios.db")


def hash_senha(senha):
    import hashlib

    return hashlib.sha256(senha.encode()).hexdigest()


def init_db():
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            responsavel TEXT NOT NULL,
            email TEXT,
            telefone TEXT,
            vencimento INTEGER DEFAULT 10,
            status TEXT DEFAULT 'Ativo',
            modulos TEXT NOT NULL,
            forma_pagamento TEXT DEFAULT 'Pix',
            valor_mensalidade REAL DEFAULT 0.0,
            data_ativacao TEXT,
            data_bloqueio TEXT
        )
    """
    )

    # Migrações seguras para colunas novas
    colunas_novas = [
        ("forma_pagamento", "TEXT DEFAULT 'Pix'"),
        ("valor_mensalidade", "REAL DEFAULT 0.0"),
        ("data_ativacao", "TEXT"),
        ("data_bloqueio", "TEXT"),
    ]
    for col, tipo in colunas_novas:
        try:
            cursor.execute(f"ALTER TABLE empresas ADD COLUMN {col} {tipo}")
        except sqlite3.OperationalError:
            pass

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            username TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL,
            setor TEXT,
            modulos TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0,
            foto_path TEXT DEFAULT '',
            num_id TEXT DEFAULT '0000',
            empresa_id INTEGER DEFAULT 1,
            primeiro_acesso INTEGER DEFAULT 0
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS solicitacoes_acesso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            username TEXT NOT NULL,
            senha TEXT NOT NULL,
            setor TEXT NOT NULL,
            num_id TEXT NOT NULL,
            data_solicitacao TEXT NOT NULL
        )
    """
    )

    # Garante Empresa Matriz
    cursor.execute("SELECT id FROM empresas WHERE id = 1")
    if not cursor.fetchone():
        hoje = datetime.now().strftime("%Y-%m-%d")
        mods = json.dumps(
            [
                "Boas-vindas",
                "Administrativo",
                "Comercial",
                "Recursos Humanos",
                "Financeiro",
                "Jurídico",
                "Técnico",
            ]
        )
        cursor.execute(
            """
            INSERT INTO empresas (id, razao_social, cnpj, responsavel, email, telefone, vencimento, status, modulos, forma_pagamento, valor_mensalidade, data_ativacao)
            VALUES (1, 'Empresa Matriz / Sistema', '00.000.000/0001-00', 'Admin Global', 'admin@sistema.com', '', 10, 'Ativo', ?, 'Isento', 0.0, ?)
        """,
            (mods, hoje),
        )

    # Garante Usuário Admin Master
    cursor.execute("SELECT username FROM usuarios WHERE username = 'admin'")
    if not cursor.fetchone():
        mods = json.dumps(
            [
                "Boas-vindas",
                "Administrativo",
                "Comercial",
                "Recursos Humanos",
                "Financeiro",
                "Jurídico",
                "Técnico",
            ]
        )
        cursor.execute(
            """
            INSERT INTO usuarios (username, nome, senha, setor, modulos, is_admin, foto_path, num_id, empresa_id, primeiro_acesso)
            VALUES ('admin', 'Administrador Global', ?, 'Administrativo', ?, 1, '', '0000', 1, 0)
        """,
            (hash_senha("123"), mods),
        )

    conn.commit()
    conn.close()


def autenticar_usuario(username, senha):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT u.username, u.nome, u.senha, u.setor, u.modulos, u.is_admin, u.foto_path, u.num_id, u.empresa_id, u.primeiro_acesso, e.status
        FROM usuarios u
        LEFT JOIN empresas e ON u.empresa_id = e.id
        WHERE LOWER(TRIM(u.username)) = LOWER(TRIM(?))
    """,
        (username,),
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        senha_input_hash = hash_senha(senha.strip())
        if row[2] == senha.strip() or row[2] == senha_input_hash:
            if row[10] == "Bloqueado":
                return "BLOQUEADO"
            return {
                "username": row[0],
                "nome": row[1],
                "setor": row[3],
                "modulos": json.loads(row[4]),
                "is_admin": bool(row[5]),
                "foto_path": row[6],
                "num_id": row[7],
                "empresa_id": row[8],
                "primeiro_acesso": bool(row[9]),
            }
    return None


def cadastrar_empresa_e_master(
    razao_social,
    cnpj,
    responsavel,
    email,
    telefone,
    vencimento,
    modulos_sel,
    username_master,
    senha_temp,
    forma_pagamento="Pix",
    valor_mensalidade=0.0,
):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()

    hoje = datetime.now().strftime("%Y-%m-%d")
    modulos_json = json.dumps(modulos_sel)

    cursor.execute(
        """
        INSERT INTO empresas (razao_social, cnpj, responsavel, email, telefone, vencimento, status, modulos, forma_pagamento, valor_mensalidade, data_ativacao)
        VALUES (?, ?, ?, ?, ?, ?, 'Ativo', ?, ?, ?, ?)
    """,
        (
            razao_social,
            cnpj,
            responsavel,
            email,
            telefone,
            vencimento,
            modulos_json,
            forma_pagamento,
            valor_mensalidade,
            hoje,
        ),
    )

    empresa_id = cursor.lastrowid
    user_limpo = username_master.strip().lower()
    senha_hashed = hash_senha(senha_temp.strip())

    cursor.execute(
        """
        INSERT OR REPLACE INTO usuarios (username, nome, senha, setor, modulos, is_admin, foto_path, num_id, empresa_id, primeiro_acesso)
        VALUES (?, ?, ?, 'Diretoria', ?, 1, '', '0001', ?, 1)
    """,
        (
            user_limpo,
            f"Master - {razao_social}",
            senha_hashed,
            modulos_json,
            empresa_id,
        ),
    )

    conn.commit()
    conn.close()
    return empresa_id


def atualizar_empresa_db(
    empresa_id,
    razao_social,
    cnpj,
    responsavel,
    email,
    telefone,
    vencimento,
    status,
    modulos,
    forma_pagamento,
    valor_mensalidade,
):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()

    data_bloqueio = (
        datetime.now().strftime("%Y-%m-%d") if status == "Bloqueado" else None
    )

    cursor.execute(
        """
        UPDATE empresas
        SET razao_social=?, cnpj=?, responsavel=?, email=?, telefone=?, vencimento=?, status=?, modulos=?, forma_pagamento=?, valor_mensalidade=?, data_bloqueio=?
        WHERE id=?
    """,
        (
            razao_social,
            cnpj,
            responsavel,
            email,
            telefone,
            vencimento,
            status,
            json.dumps(modulos),
            forma_pagamento,
            valor_mensalidade,
            data_bloqueio,
            empresa_id,
        ),
    )

    conn.commit()
    conn.close()


def listar_empresas_db():
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, razao_social, cnpj, responsavel, email, telefone, vencimento, status, modulos, forma_pagamento, valor_mensalidade, data_ativacao, data_bloqueio FROM empresas"
    )
    rows = cursor.fetchall()
    conn.close()

    empresas = []
    for r in rows:
        empresas.append(
            {
                "id": r[0],
                "razao_social": r[1],
                "cnpj": r[2],
                "responsavel": r[3],
                "email": r[4],
                "telefone": r[5],
                "vencimento": r[6],
                "status": r[7],
                "modulos": json.loads(r[8]),
                "forma_pagamento": r[9] or "Pix",
                "valor_mensalidade": r[10] or 0.0,
                "data_ativacao": r[11] or "N/A",
                "data_bloqueio": r[12] or "N/A",
            }
        )
    return empresas


def alterar_senha_primeiro_acesso_db(username, nova_senha):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    senha_hashed = hash_senha(nova_senha)
    cursor.execute(
        "UPDATE usuarios SET senha = ?, primeiro_acesso = 0 WHERE LOWER(TRIM(username)) = LOWER(TRIM(?))",
        (senha_hashed, username),
    )
    conn.commit()
    linhas = cursor.rowcount
    conn.close()
    return linhas > 0


def listar_usuarios_db():
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, nome, setor, modulos, is_admin, num_id, empresa_id FROM usuarios"
    )
    rows = cursor.fetchall()
    conn.close()

    usuarios = []
    for r in rows:
        usuarios.append(
            {
                "username": r[0],
                "nome": r[1],
                "setor": r[2],
                "modulos": json.loads(r[3]),
                "is_admin": bool(r[4]),
                "num_id": r[5],
                "empresa_id": r[6],
            }
        )
    return usuarios


def listar_solicitacoes_db():
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, username, senha, setor, num_id, data_solicitacao FROM solicitacoes_acesso"
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": r[0],
            "nome": r[1],
            "username": r[2],
            "senha": r[3],
            "setor": r[4],
            "num_id": r[5],
            "data": r[6],
        }
        for r in rows
    ]


def aprovar_solicitacao_db(
    sol_id, username, nome, senha, setor, num_id, modulos
):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, nome, senha, setor, modulos, is_admin, empresa_id, primeiro_acesso) VALUES (?, ?, ?, ?, ?, 0, 1, 0)",
        (username, nome, senha, setor, json.dumps(modulos)),
    )
    cursor.execute("DELETE FROM solicitacoes_acesso WHERE id = ?", (sol_id,))
    conn.commit()
    conn.close()


def rejeitar_solicitacao_db(sol_id):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM solicitacoes_acesso WHERE id = ?", (sol_id,))
    conn.commit()
    conn.close()


def excluir_usuario_db(username):
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM usuarios WHERE LOWER(TRIM(username)) = LOWER(TRIM(?))",
        (username,),
    )
    conn.commit()
    conn.close()

def obter_empresa_por_id(empresa_id):
    """Retorna os detalhes da empresa pelo ID."""
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, razao_social, cnpj, responsavel, email, telefone, vencimento, status, modulos, forma_pagamento, valor_mensalidade, data_ativacao, data_bloqueio 
        FROM empresas WHERE id = ?
    """,
        (empresa_id,),
    )
    r = cursor.fetchone()
    conn.close()

    if r:
        return {
            "id": r[0],
            "razao_social": r[1],
            "cnpj": r[2],
            "responsavel": r[3],
            "email": r[4],
            "telefone": r[5],
            "vencimento": r[6],
            "status": r[7],
            "modulos": json.loads(r[8]),
            "forma_pagamento": r[9] or "Pix",
            "valor_mensalidade": r[10] or 0.0,
            "data_ativacao": r[11] or "N/A",
            "data_bloqueio": r[12] or "N/A",
        }
    return None

def excluir_empresa_db(empresa_id):
    """Remove permanentemente uma empresa e todos os seus usuários associados."""
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE empresa_id = ?", (empresa_id,))
    cursor.execute("DELETE FROM empresas WHERE id = ?", (empresa_id,))
    conn.commit()
    conn.close()


def redefinir_senha_usuario_db(username, nova_senha):
    """Redefine a senha de um usuário via suporte e força o primeiro acesso."""
    conn = sqlite3.connect(DB_USER_PATH)
    cursor = conn.cursor()
    senha_hashed = hash_senha(nova_senha)
    cursor.execute(
        "UPDATE usuarios SET senha = ?, primeiro_acesso = 1 WHERE LOWER(TRIM(username)) = LOWER(TRIM(?))",
        (senha_hashed, username),
    )
    conn.commit()
    conn.close()


init_db()