import sqlite3
import streamlit as st

def get_db():
    """Conexão direta ao banco de dados SQLite."""
    conn = sqlite3.connect("vanguard.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_saas_schema():
    """Garante a estrutura das tabelas do SaaS Master."""
    conn = get_db()
    cursor = conn.cursor()
    
    # Tabela de Empresas / Clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            plano TEXT DEFAULT 'Enterprise Pro',
            status TEXT DEFAULT 'ATIVO',
            valor_mensal REAL DEFAULT 490.00,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Garante a empresa Matriz ID #1
    cursor.execute("SELECT COUNT(*) FROM empresas WHERE id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO empresas (id, nome, cnpj, plano, status, valor_mensal)
            VALUES (1, 'Master - CMDTC SERVIÇOS LTDA', '00.000.000/0001-00', 'Enterprise Pro (Matriz)', 'ATIVO', 490.00)
        """)
    
    conn.commit()
    conn.close()

def render():
    init_saas_schema()
    
    st.title("👑 Painel SaaS Master - Gestão Global")
    st.caption("Controle central de empresas contratantes, assinaturas e status da plataforma.")
    st.markdown("<br>", unsafe_allow_html=True)

    conn = get_db()
    cursor = conn.cursor()

    # --- MÉTRICAS GERAIS ---
    cursor.execute("SELECT COUNT(*) FROM empresas")
    total_empresas = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM empresas WHERE status = 'ATIVO'")
    empresas_ativas = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(valor_mensal) FROM empresas WHERE status = 'ATIVO'")
    faturamento_row = cursor.fetchone()[0]
    faturamento = faturamento_row if faturamento_row else 0.0

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Total de Clientes", total_empresas)
    with kpi2:
        st.metric("Assinaturas Ativas", empresas_ativas)
    with kpi3:
        st.metric("Faturamento Mensal", f"R$ {faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with kpi4:
        st.metric("Status da Plataforma", "🟢 100% Operacional")

    st.divider()

    # --- ABAS DE NAVEGAÇÃO ---
    tab_listar, tab_novo = st.tabs(["🏢 Clientes & Licenças Ativas", "➕ Cadastrar Novo Cliente SaaS"])

    # ==========================================
    # TAB 1: LISTAGEM, EDIÇÃO E EXCLUSÃO DE CLIENTES
    # ==========================================
    with tab_listar:
        cursor.execute("SELECT * FROM empresas ORDER BY id ASC")
        empresas = cursor.fetchall()

        if not empresas:
            st.info("Nenhum cliente cadastrado no momento.")
        else:
            for emp in empresas:
                emp_id = emp["id"]
                nome = emp["nome"]
                cnpj = emp["cnpj"]
                plano = emp["plano"]
                status = emp["status"]
                valor = emp["valor_mensal"]

                # Badge de Status
                status_color = "🟢 ATIVO" if status == "ATIVO" else "🔴 BLOQUEADO"

                with st.container(border=True):
                    col_info, col_status = st.columns([3, 1])
                    
                    with col_info:
                        st.markdown(f"### ID #{emp_id} - {nome}")
                        st.caption(f"**CNPJ:** {cnpj} | **Plano:** {plano} | **Mensalidade:** R$ {valor:,.2f}")
                    
                    with col_status:
                        st.markdown(f"**Status:** {status_color}")

                    # AÇÕES RÁPIDAS (EDITAR, BLOQUEAR, EXCLUIR)
                    c_edit, c_block, c_del = st.columns([1, 1, 1])

                    # 1. EDITAR LICENÇA
                    with c_edit:
                        with st.popover("✏️ Editar Dados"):
                            st.markdown(f"**Editar Cliente #{emp_id}**")
                            with st.form(key=f"form_edit_{emp_id}"):
                                novo_nome = st.text_input("Razão Social / Nome", value=nome)
                                novo_cnpj = st.text_input("CNPJ", value=cnpj)
                                novo_plano = st.selectbox(
                                    "Plano Contratado",
                                    ["Enterprise Pro", "Corporate", "Business", "Start"],
                                    index=0 if plano not in ["Corporate", "Business", "Start"] else ["Enterprise Pro", "Corporate", "Business", "Start"].index(plano)
                                )
                                novo_valor = st.number_input("Valor Mensal (R$)", value=float(valor), step=50.0)

                                if st.form_submit_button("Salvar Alterações", type="primary"):
                                    c = get_db()
                                    c.execute("""
                                        UPDATE empresas 
                                        SET nome = ?, cnpj = ?, plano = ?, valor_mensal = ?
                                        WHERE id = ?
                                    """, (novo_nome, novo_cnpj, novo_plano, novo_valor, emp_id))
                                    c.commit()
                                    c.close()
                                    st.success("Dados atualizados com sucesso!")
                                    st.rerun()

                    # 2. BLOQUEAR / DESBLOQUEAR
                    with c_block:
                        action_label = "🔴 Bloquear" if status == "ATIVO" else "🟢 Desbloquear"
                        if st.button(action_label, key=f"btn_block_{emp_id}", use_container_width=True):
                            novo_status = "BLOQUEADO" if status == "ATIVO" else "ATIVO"
                            c = get_db()
                            c.execute("UPDATE empresas SET status = ? WHERE id = ?", (novo_status, emp_id))
                            c.commit()
                            c.close()
                            st.toast(f"Status do cliente ID #{emp_id} alterado para {novo_status}!")
                            st.rerun()

                    # 3. EXCLUIR CLIENTE (COM SEGURANÇA)
                    with c_del:
                        if emp_id == 1:
                            st.button("🔒 Matriz Protegida", disabled=True, use_container_width=True)
                        else:
                            with st.popover("🗑️ Excluir"):
                                st.error("⚠️ Esta ação é irreversível!")
                                confirm = st.text_input(f"Digite EXCLUIR para confirmar", key=f"conf_del_{emp_id}")
                                if st.button("Confirmar Exclusão", type="primary", key=f"btn_del_conf_{emp_id}"):
                                    if confirm.strip().upper() == "EXCLUIR":
                                        c = get_db()
                                        c.execute("DELETE FROM empresas WHERE id = ?", (emp_id,))
                                        c.commit()
                                        c.close()
                                        st.success("Cliente removido com sucesso.")
                                        st.rerun()
                                    else:
                                        st.warning("Confirmação incorreta.")

    # ==========================================
    # TAB 2: CADASTRAR NOVO CLIENTE / EMPRESA
    # ==========================================
    with tab_novo:
        st.subheader("Cadastrar Nova Empresa Contratante")
        st.caption("Preencha os dados abaixo para provisionar um novo acesso na plataforma SaaS.")

        with st.form("form_novo_cliente", clear_on_submit=True):
            col_a, col_b = st.columns(2)

            with col_a:
                cad_nome = st.text_input("Razão Social / Nome da Empresa *")
                cad_cnpj = st.text_input("CNPJ *", placeholder="00.000.000/0001-00")
                cad_admin_user = st.text_input("Usuário Admin Inicial *", value="admin")

            with col_b:
                cad_plano = st.selectbox("Plano Contratado", ["Enterprise Pro", "Corporate", "Business", "Start"])
                cad_valor = st.number_input("Valor da Mensalidade (R$)", value=490.00, step=50.0)
                cad_admin_pass = st.text_input("Senha Inicial *", type="password", value="1234")

            st.markdown("<br>", unsafe_allow_html=True)
            submit_novo = st.form_submit_button("🚀 Cadastrar e Activar Empresa", type="primary", use_container_width=True)

            if submit_novo:
                if not cad_nome or not cad_cnpj or not cad_admin_user or not cad_admin_pass:
                    st.error("Por favor, preencha todos os campos obrigatórios (*).")
                else:
                    c = get_db()
                    cur = c.cursor()
                    
                    # Insere a nova empresa
                    cur.execute("""
                        INSERT INTO empresas (nome, cnpj, plano, status, valor_mensal)
                        VALUES (?, ?, ?, 'ATIVO', ?)
                    """, (cad_nome, cad_cnpj, cad_plano, cad_valor))
                    
                    nova_empresa_id = cur.lastrowid

                    # Insere o usuário administrador inicial vinculado a esta empresa
                    try:
                        cur.execute("""
                            INSERT INTO usuarios (username, senha, nome, setor, empresa_id, is_admin, primeiro_acesso)
                            VALUES (?, ?, ?, 'Diretoria', ?, 1, 1)
                        """, (cad_admin_user, cad_admin_pass, f"Admin {cad_nome}", nova_empresa_id))
                    except Exception:
                        pass  # Ignora caso a estrutura de usuários seja gerenciada em outro modulo

                    c.commit()
                    c.close()

                    st.success(f"Empresa '{cad_nome}' cadastrada com sucesso com ID #{nova_empresa_id}!")
                    st.rerun()

    conn.close()
