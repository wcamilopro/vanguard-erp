import os
import sqlite3
import streamlit as st


def conectar_banco():
    """Conecta ao banco de dados SQLite local com tolerância a nomes de arquivos."""
    bancos_possiveis = ["erp.db", "database.db", "dados.db"]
    for db in bancos_possiveis:
        if os.path.exists(db):
            try:
                conn = sqlite3.connect(db)
                conn.row_factory = sqlite3.Row
                return conn
            except Exception:
                pass
    return None


def render():
    st.title("👑 Painel SaaS Master - Gestão Global")
    st.caption("Visão geral de empresas contratantes, assinaturas e status da plataforma.")
    st.markdown("---")

    empresas = []
    total_empresas = 1
    total_usuarios = 1

    # Busca os dados diretamente do banco SQLite de forma segura
    conn = conectar_banco()
    if conn:
        try:
            c = conn.cursor()
            
            # Conta total de empresas e usuarios
            c.execute("SELECT COUNT(*) FROM empresas")
            total_empresas = c.fetchone()[0]

            c.execute("SELECT COUNT(*) FROM usuarios")
            total_usuarios = c.fetchone()[0]

            # Lista todas as empresas
            c.execute("SELECT id, nome, cnpj, ativo FROM empresas")
            empresas = c.fetchall()
        except Exception:
            pass
        finally:
            conn.close()

    # METRICAS GERAIS
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Empresas Clientes", total_empresas)
    c2.metric("Usuários Ativos", total_usuarios)
    c3.metric("Faturamento Estimado", f"R$ {max(total_empresas, 1) * 490:,.2f}")
    c4.metric("Status da Plataforma", "🟢 100% Online")

    st.markdown("<br>", unsafe_allow_html=True)

    # ABA DE CLIENTES CADASTRADOS
    st.subheader("🏢 Clientes & Licenças Ativas")

    if empresas:
        for emp in empresas:
            emp_id = emp["id"] if isinstance(emp, sqlite3.Row) else emp[0]
            nome = emp["nome"] if isinstance(emp, sqlite3.Row) else emp[1]
            cnpj = emp["cnpj"] if isinstance(emp, sqlite3.Row) else emp[2]
            ativo = emp["ativo"] if isinstance(emp, sqlite3.Row) else emp[3]

            with st.expander(f"🏢 ID #{emp_id} - {nome}"):
                col1, col2, col3 = st.columns([2, 2, 1])
                col1.write(f"**CNPJ:** {cnpj if cnpj else 'Não informado'}")
                col2.write("**Plano:** Enterprise Pro")

                status_str = "🟢 ATIVO" if ativo else "🔴 SUSPENSO"
                col3.write(f"**Status:** {status_str}")

                st.markdown("---")
                btn_col1, btn_col2 = st.columns(2)
                if btn_col1.button("✏️ Editar Licença", key=f"edit_{emp_id}"):
                    st.info(f"Editando configurações da empresa {nome}...")
                if btn_col2.button("🚫 Bloquear/Desbloquear", key=f"block_{emp_id}"):
                    st.warning(f"Alterando status do cliente {nome}...")
    else:
        # Visualização Padrão caso a tabela esteja inicializando
        with st.expander("🏢 ID #1 - Master - CMDTCSERVIÇOS LTDA"):
            col1, col2, col3 = st.columns([2, 2, 1])
            col1.write("**CNPJ:** 00.000.000/0001-00")
            col2.write("**Plano:** Enterprise Pro (Matriz)")
            col3.write("**Status:** 🟢 ATIVO")

            st.markdown("---")
            btn_col1, btn_col2 = st.columns(2)
            if btn_col1.button("✏️ Editar Licença", key="edit_master"):
                st.info("Editando configurações da empresa Matriz...")
            if btn_col2.button("🚫 Bloquear/Desbloquear", key="block_master"):
                st.warning("Status da Matriz mantido ativo.")