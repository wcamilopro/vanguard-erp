import streamlit as st

# 1. Configuração Básica da Página
st.set_page_config(
    page_title="Vanguard | ERP",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estado de Sessão (Login)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

# ==========================================
# TELA DE LOGIN
# ==========================================
if not st.session_state.logged_in:
    _, col_login, _ = st.columns([1, 1, 1])
    
    with col_login:
        st.write("<br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center;'>🔷 VANGUARD</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: gray;'>SISTEMAS DE GESTÃO</p>", unsafe_allow_html=True)
            st.caption('*"Controle absoluto. Operação simples."*')
            
            st.text_input("Usuário / Login", key="input_user")
            st.text_input("Senha", type="password", key="input_pass")
            
            st.write("")
            if st.button("Entrar no Sistema", use_container_width=True):
                st.session_state.logged_in = True
                st.rerun()

# ==========================================
# PAINEL PRINCIPAL (LOGADO)
# ==========================================
else:
    # BARRA LATERAL (SIDEBAR NATIVA E LIMPA)
    with st.sidebar:
        st.title("🔷 VANGUARD")
        st.caption("SISTEMAS DE GESTÃO")
        st.divider()
        
        st.markdown("**Master - CMDTC SERVIÇOS LTDA**")
        st.caption("Usuário: @user | Setor: Diretoria")
        st.divider()
        
        menu = st.radio(
            "NAVEGAÇÃO",
            ["Boas-vindas", "Comercial", "Recursos Humanos", "Administrativo", "Financeiro"]
        )
        
        st.divider()
        if st.button("🚪 Sair do Sistema", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # CONTEÚDO PRINCIPAL
    if menu == "Boas-vindas":
        st.title("🔷 VANGUARD ERP")
        st.caption("Painel de Controle e Gestão Integrada")
        st.write("")

        # 1. Indicadores Superiores (Componente Nativo st.metric)
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.metric(label="STATUS DO PLANO", value="🟢 ATIVO")
        with k2:
            st.metric(label="MÓDULOS CONTRATADOS", value="4 Módulos")
        with k3:
            st.metric(label="VENCIMENTO", value="Dia 10")
        with k4:
            st.metric(label="FORMA DE PAGAMENTO", value="Boleto")

        st.write("")
        st.divider()

        # 2. Cards dos Módulos
        st.subheader("Módulos Habilitados")
        st.caption("Acessos disponíveis para o perfil da sua empresa:")
        st.write("")

        m1, m2, m3 = st.columns(3)
        
        with m1:
            with st.container(border=True):
                st.markdown("### 📈 Comercial")
                st.write("Gestão de propostas, orçamentos, contratos e carteira de clientes.")
                st.success("Módulo Ativo")

        with m2:
            with st.container(border=True):
                st.markdown("### 👥 Recursos Humanos")
                st.write("Gestão de colaboradores, equipes, cargos e contatos operacionais.")
                st.success("Módulo Ativo")

        with m3:
            with st.container(border=True):
                st.markdown("### ⚙️ Administrativo")
                st.write("Configurações do sistema, logo corporativa e gestão de acessos.")
                st.success("Módulo Ativo")

        st.write("")
        st.divider()

        # 3. Informações de Rodapé
        c_info1, c_info2 = st.columns([2, 1])
        
        with c_info1:
            st.info("""
            **📢 Avisos & Atualizações**
            * **Personalização de Documentos:** Cadastre a logomarca da sua empresa no módulo Administrativo.
            * **Segurança:** Mantenha as senhas individuais dos usuários sempre atualizadas.
            """)

        with c_info2:
            st.success("""
            **🛠️ Atendimento e Suporte**  
            Dúvidas ou novos usuários?  
            `suporte@vanguarderp.com.br`
            """)

    else:
        st.title(f"Módulo {menu}")
        st.info("Área pronta para receber as telas de cadastro e tabelas deste módulo.")
