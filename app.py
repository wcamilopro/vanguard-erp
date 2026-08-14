import importlib
import streamlit as st
from core.db import (
    alterar_senha_primeiro_acesso_db,
    autenticar_usuario,
    init_db,
)
from core.estilos import (
    aplicar_estilos_customizados,
    aplicar_fundo_login,
    renderizar_card_usuario,
)

# Favicon Oficial Vanguard (Azul em cima e Cinza Claro em baixo)
FAVICON_VANGUARD = "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'><path d='M20 4L36 32H27L20 18L13 32H4L20 4Z' fill='%233B82F6'/><path d='M20 18L26 32H21L20 29L19 32H14L20 18Z' fill='%23E2E8F0'/></svg>"

st.set_page_config(
    page_title="Vanguard | Sistemas de Gestão",
    page_icon=FAVICON_VANGUARD,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializa o Banco de Dados com segurança
init_db()

# Inicialização limpa do Session State
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

if "modulo_ativo" not in st.session_state:
    st.session_state["modulo_ativo"] = "Boas-vindas"


def reexecutar():
    """Força o recarregamento seguro da página."""
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()


def modal_primeiro_acesso(username):
    """Modal obrigatório para redefinição de senha no primeiro acesso."""
    st.warning("🔒 Primeiro Acesso Detectado")
    st.info("Por razões de segurança, cadastre uma nova senha para continuar.")

    with st.form("form_primeiro_acesso"):
        nova_senha = st.text_input("Nova Senha", type="password")
        confirma_senha = st.text_input("Confirme a Nova Senha", type="password")
        btn_salvar = st.form_submit_button("Atualizar Senha e Acessar", use_container_width=True, type="primary")

        if btn_salvar:
            if not nova_senha or len(nova_senha) < 4:
                st.error("A senha deve conter no mínimo 4 caracteres.")
            elif nova_senha != confirma_senha:
                st.error("As senhas digitadas não coincidem.")
            else:
                if alterar_senha_primeiro_acesso_db(username, nova_senha):
                    st.success("Senha alterada com sucesso!")
                    st.session_state["usuario_logado"]["primeiro_acesso"] = False
                    reexecutar()
                else:
                    st.error("Erro ao atualizar a senha. Tente novamente.")


def tela_login():
    """Tela de Login Corporativa Vanguard (Card destacado com botões padronizados)."""
    aplicar_fundo_login()

    _, col_centro, _ = st.columns([1, 1.1, 1])

    with col_centro:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            # LOGOTIPO PADRONIZADO (Azul em cima e Cinza Claro em baixo)
            st.markdown(
                """
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 4px;">
                        <svg width="38" height="38" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 4L36 32H27L20 18L13 32H4L20 4Z" fill="#3B82F6"/>
                            <path d="M20 18L26 32H21L20 29L19 32H14L20 18Z" fill="#E2E8F0"/>
                        </svg>
                        <span style="font-size: 28px; font-weight: 800; color: #FFFFFF; letter-spacing: -1px; font-family: 'Segoe UI', sans-serif;">
                            VANGUARD
                        </span>
                    </div>
                    <div style="font-size: 10px; font-weight: 700; color: #60A5FA; text-transform: uppercase; letter-spacing: 2px;">
                        SISTEMAS DE GESTÃO
                    </div>
                    <div style="font-size: 12px; color: #94A3B8; margin-top: 6px; font-style: italic;">
                        "Controle absoluto. Operação simples."
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            usuario_input = st.text_input("Usuário / Login", key="login_usuario")
            senha_input = st.text_input("Senha", type="password", key="login_senha")
            
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            submit = st.button("Entrar no Sistema", use_container_width=True, type="primary", key="btn_entrar_sistema")

            if submit:
                if usuario_input and senha_input:
                    res = autenticar_usuario(usuario_input, senha_input)

                    if res == "BLOQUEADO":
                        st.error("🚫 Acesso Suspenso. Entre em contato com o suporte financeiro.")
                    elif res:
                        st.session_state["usuario_logado"] = res
                        st.session_state["modulo_ativo"] = "Boas-vindas"
                        reexecutar()
                    else:
                        st.error("Usuário ou senha incorretos.")
                else:
                    st.warning("Preencha todos os campos.")

            # BOTÕES SECUNDÁRIOS DENTRO DO MESMO CARD (AGORA COM TYPE PRIMARY PARA FICAREM AZUIS)
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("Solicitar Cadastro", key="btn_solicitar_cad", use_container_width=True, type="primary"):
                    st.info("Fale com o comercial: (11) 99999-8888.")
            with col_b2:
                if st.button("Esqueci a Senha", key="btn_esqueci_senha", use_container_width=True, type="primary"):
                    st.info("Solicite o reset ao administrador da conta.")


def main():
    aplicar_estilos_customizados()

    st.markdown(
        """
        <style>
            .main .block-container {
                padding-top: 2.2rem !important;
                padding-bottom: 2rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
                max-width: 98% !important;
            }
            [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div {
                gap: 0.35rem !important;
            }
            [data-testid="stSidebar"] .stButton > button {
                padding: 6px 14px !important;
                min-height: 38px !important;
                font-size: 13.5px !important;
                font-weight: 500 !important;
                border-radius: 6px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state["usuario_logado"]:
        tela_login()
        return

    usuario = st.session_state["usuario_logado"]

    if usuario.get("primeiro_acesso", False):
        modal_primeiro_acesso(usuario["username"])
        return

    # BARRA LATERAL
    with st.sidebar:
        # LOGOTIPO PADRONIZADO NO TOPO DA SIDEBAR
        st.markdown(
            """
            <div style="background-color: #1E293B; padding: 12px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 16px; text-align: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                <div style="display: flex; align-items: center; justify-content: center; gap: 8px;">
                    <svg width="24" height="24" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 4L36 32H27L20 18L13 32H4L20 4Z" fill="#3B82F6"/>
                        <path d="M20 18L26 32H21L20 29L19 32H14L20 18Z" fill="#E2E8F0"/>
                    </svg>
                    <span style="font-size: 16px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.5px; font-family: 'Segoe UI', sans-serif;">
                        VANGUARD
                    </span>
                </div>
                <div style="font-size: 8.5px; font-weight: 700; color: #60A5FA; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 3px;">
                    Sistemas de Gestão
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        renderizar_card_usuario(
            nome_empresa=usuario.get('nome', 'Empresa Cliente'),
            usuario=usuario.get('username', 'usuario'),
            setor=usuario.get('setor', 'Geral')
        )

        modulos_permitidos = list(usuario.get("modulos", ["Boas-vindas"]))

        is_empresa_matriz = str(usuario.get("empresa_id")) == "1" or usuario.get("empresa_id") == 1
        is_admin_user = usuario.get("is_admin") or usuario.get("username") == "admin"

        if is_empresa_matriz and is_admin_user:
            if "Painel SaaS Master" not in modulos_permitidos:
                modulos_permitidos.append("Painel SaaS Master")

        st.markdown("<span style='color: #94A3B8; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;'>Navegação</span>", unsafe_allow_html=True)

        mapa_modulos = {
            "Boas-vindas": ("Boas-vindas", "boas_vindas"),
            "Comercial": ("Comercial", "comercial"),
            "Recursos Humanos": ("Recursos Humanos", "rh"),
            "Técnico": ("Técnico", "tecnico"),
            "Financeiro": ("Financeiro", "financeiro"),
            "Administrativo": ("Administrativo", "admin"),
            "Painel SaaS Master": ("Painel SaaS Master", "saas_master"),
        }

        for mod_key in modulos_permitidos:
            if mod_key in mapa_modulos:
                label, _ = mapa_modulos[mod_key]
                is_active = st.session_state["modulo_ativo"] == mod_key
                btn_type = "primary" if is_active else "secondary"
                prefix = "• " if is_active else ""

                if st.button(f"{prefix}{label}", key=f"nav_{mod_key}", use_container_width=True, type=btn_type):
                    if st.session_state["modulo_ativo"] != mod_key:
                        st.session_state["modulo_ativo"] = mod_key
                        reexecutar()

        st.markdown("---")
        if st.button("🚪 Sair do Sistema", key="btn_logout", use_container_width=True):
            st.session_state["usuario_logado"] = None
            st.session_state["modulo_ativo"] = "Boas-vindas"
            reexecutar()

        # ASSINATURA NO RODAPÉ
        st.markdown(
            """
            <div style="margin-top: 35px; padding-top: 12px; border-top: 1px solid #1E293B; text-align: center;">
                <div style="font-size: 9.5px; color: #94A3B8; font-style: italic; margin-bottom: 5px;">
                    "Controle absoluto. Operação simples."
                </div>
                <div style="font-size: 10px; color: #F1F5F9; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px;">
                    Vanguard ERP © 2026
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ÁREA CENTRAL
    modulo_selecionado = st.session_state.get("modulo_ativo", "Boas-vindas")

    if modulo_selecionado in mapa_modulos:
        _, pasta_modulo = mapa_modulos[modulo_selecionado]
        try:
            modulo = importlib.import_module(f"modulos.{pasta_modulo}.render")
            modulo.render()
        except ModuleNotFoundError:
            st.title(f"Módulo {modulo_selecionado}")
            st.info("Este módulo está em desenvolvimento.")
        except Exception as e:
            st.error(f"Erro ao carregar o módulo '{modulo_selecionado}': {e}")


if __name__ == "__main__":
    main()
