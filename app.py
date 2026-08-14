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

# Configuração Oficial da Marca Vanguard
st.set_page_config(
    page_title="Vanguard | Sistemas de Gestão",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializa o Banco de Dados
init_db()


def reexecutar():
    """Garante compatibilidade de recarregamento no Streamlit."""
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()


def modal_primeiro_acesso(username):
    """Modal obrigatório para redefinição de senha no primeiro acesso."""
    st.warning("🔒 Primeiro Acesso Detectado")
    st.info("Por razões de segurança, você precisa cadastrar uma nova senha para continuar.")

    with st.form("form_primeiro_acesso"):
        nova_senha = st.text_input("Nova Senha", type="password")
        confirma_senha = st.text_input("Confirme a Nova Senha", type="password")
        btn_salvar = st.form_submit_button("Atualizar Senha e Acessar")

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
    """Tela de Login Corporativa Vanguard (Vetor SVG Minimalista)."""
    aplicar_fundo_login()

    col_esq, col_centro, col_dir = st.columns([1, 1.2, 1])

    with col_centro:
        # LOGO VETORIAL SVG CLEAN
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 6px;">
                    <svg width="42" height="42" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 4L36 32H27L20 18L13 32H4L20 4Z" fill="#2563EB"/>
                        <path d="M20 18L26 32H21L20 29L19 32H14L20 18Z" fill="#0F172A"/>
                    </svg>
                    <span style="font-size: 32px; font-weight: 800; color: #0F172A; letter-spacing: -1px; font-family: 'Segoe UI', sans-serif;">
                        VANGUARD
                    </span>
                </div>
                <div style="font-size: 11px; font-weight: 700; color: #2563EB; text-transform: uppercase; letter-spacing: 2.5px;">
                    SISTEMAS DE GESTÃO
                </div>
                <div style="font-size: 12.5px; color: #64748B; margin-top: 8px; font-style: italic;">
                    "Controle absoluto. Operação simples."
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # FORMULÁRIO DE ACESSO
        with st.form("form_login"):
            usuario_input = st.text_input("Usuário / Login")
            senha_input = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar no Sistema")

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

        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

        # BOTÕES AUXILIARES GHOST
        if st.button("Solicitar Cadastro de Empresa", key="btn_solicitar_cad"):
            st.info("Entre em contato com a equipe comercial Vanguard pelo WhatsApp (11) 99999-8888.")

        if st.button("Esqueci minha senha", key="btn_esqueci_senha"):
            st.info("Solicite o reset de senha ao administrador da sua empresa.")


def main():
    aplicar_estilos_customizados()

    if "usuario_logado" not in st.session_state or not st.session_state["usuario_logado"]:
        tela_login()
        return

    usuario = st.session_state["usuario_logado"]

    if usuario.get("primeiro_acesso", False):
        modal_primeiro_acesso(usuario["username"])
        return

    # BARRA LATERAL (SIDEBAR)
    with st.sidebar:
        # LOGO DE TOPO NA SIDEBAR (VETORIAL SVG)
        st.markdown(
            """
            <div style="padding: 4px 0px 16px 0px; text-align: center; border-bottom: 1px solid #1E293B; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
                    <svg width="26" height="26" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 4L36 32H27L20 18L13 32H4L20 4Z" fill="#3B82F6"/>
                        <path d="M20 18L26 32H21L20 29L19 32H14L20 18Z" fill="#FFFFFF"/>
                    </svg>
                    <span style="font-size: 18px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.5px; font-family: 'Segoe UI', sans-serif;">
                        VANGUARD
                    </span>
                </div>
                <div style="font-size: 9px; font-weight: 700; color: #60A5FA; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 3px;">
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

        if usuario.get("empresa_id") == 1 and usuario.get("is_admin"):
            if " Painel SaaS Master" not in modulos_permitidos:
                modulos_permitidos.append(" Painel SaaS Master")

        if "modulo_ativo" not in st.session_state:
            st.session_state["modulo_ativo"] = modulos_permitidos[0] if modulos_permitidos else "Boas-vindas"

        st.markdown("<span style='color: #94A3B8; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;'>Navegação</span>", unsafe_allow_html=True)

        mapa_modulos = {
            "Boas-vindas": ("Boas-vindas", "boas_vindas"),
            "Comercial": ("Comercial", "comercial"),
            "Recursos Humanos": ("Recursos Humanos", "rh"),
            "Técnico": ("Técnico", "tecnico"),
            "Financeiro": ("Financeiro", "financeiro"),
            "Administrativo": ("Administrativo", "admin"),
            " Painel SaaS Master": ("Painel SaaS Master", "saas_master"),
        }

        for mod_key in modulos_permitidos:
            if mod_key in mapa_modulos:
                label, _ = mapa_modulos[mod_key]
                is_active = st.session_state["modulo_ativo"] == mod_key
                prefix = "• " if is_active else ""

                if st.button(f"{prefix}{label}", key=f"nav_{mod_key}"):
                    st.session_state["modulo_ativo"] = mod_key
                    reexecutar()

        st.markdown("---")
        if st.button("Sair do Sistema", key="btn_logout"):
            st.session_state["usuario_logado"] = None
            st.session_state["modulo_ativo"] = None
            reexecutar()

    # ÁREA CENTRAL / RENDERIZAÇÃO
    modulo_selecionado = st.session_state.get("modulo_ativo", "Boas-vindas")

    if modulo_selecionado in mapa_modulos:
        _, pasta_modulo = mapa_modulos[modulo_selecionado]
        try:
            modulo = importlib.import_module(f"modulos.{pasta_modulo}.render")
            modulo.render()
        except ModuleNotFoundError:
            st.title(f"Módulo {modulo_selecionado}")
            st.info("Este módulo está em desenvolvimento ou a pasta correspondente não foi encontrada.")
        except Exception as e:
            st.error(f"Erro ao carregar o módulo '{modulo_selecionado}': {e}")


if __name__ == "__main__":
    main()