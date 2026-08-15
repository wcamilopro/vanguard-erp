import streamlit as st
from core.db import autenticar_usuario, init_db
from core.estilos import aplicar_fundo_login

FAVICON_VANGUARD = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'><path d='M20 4L36 32H27L20 18L13 32H4L20 4Z' fill='%233B82F6'/><path d='M20 18L26 32H21L20 29L19 32H14L20 18Z' fill='%23E2E8F0'/></svg>"

st.set_page_config(
    page_title="Vanguard | Login",
    page_icon=FAVICON_VANGUARD,
    layout="centered",
    initial_sidebar_state="collapsed",
)

init_db()
aplicar_fundo_login()

# Estilo isolado exclusivamente para o card de login
st.markdown(
    """
    <style>
        .vanguard-login-card {
            background-color: #FFFFFF !important;
            padding: 32px !important;
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

_, col_centro, _ = st.columns([1, 1.2, 1])

with col_centro:
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<div class='vanguard-login-card'>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 24px;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 4px;">
                <svg width="38" height="38" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20 4L36 32H27L20 18L13 32H4L20 4Z" fill="#3B82F6"/>
                    <path d="M20 18L26 32H21L20 29L19 32H14L20 18Z" fill="#E2E8F0"/>
                </svg>
                <span style="font-size: 28px; font-weight: 800; color: #0F172A; letter-spacing: -1px; font-family: 'Segoe UI', sans-serif;">
                    VANGUARD
                </span>
            </div>
            <div style="font-size: 10px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 2px;">
                SISTEMAS DE GESTÃO
            </div>
            <div style="font-size: 12px; color: #64748B; margin-top: 6px; font-style: italic;">
                "Controle absoluto. Operação simples."
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("form_login_isolado"):
        usuario_input = st.text_input("Usuário / Login")
        senha_input = st.text_input("Senha", type="password")

        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        submit = st.form_submit_button("Entrar no Sistema", use_container_width=True, type="primary")

        if submit:
            if usuario_input and senha_input:
                res = autenticar_usuario(usuario_input, senha_input)

                if res == "BLOQUEADO":
                    st.error("🚫 Acesso Suspenso. Entre em contato com o suporte financeiro.")
                elif res:
                    st.success("🎉 Login aprovado com sucesso!")
                    st.info("Clique no botão abaixo para abrir o seu ERP:")
                    
                    # ⚠️ URL exata do seu app principal no Streamlit Cloud
                    url_do_erp = "https://vanguard-erp.streamlit.app"
                    
                    st.markdown(
                        f'<a href="{url_do_erp}" target="_self"><button style="width:100%; background-color:#2563EB; color:white; padding:12px; border:none; border-radius:6px; font-weight:bold; cursor:pointer; margin-top:10px;">ACESSAR SISTEMA ERP</button></a>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.error("Usuário ou senha incorretos.")
            else:
                st.warning("Preencha todos os campos.")

    st.markdown("</div>", unsafe_allow_html=True)
