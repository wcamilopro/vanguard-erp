import streamlit as st

# 1. Configuração da Página em Tela Cheia (Wide)
st.set_page_config(
    page_title="Vanguard | Sistemas de Gestão",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilo CSS Mínimo e Seguro (Apenas o essencial para não quebrar a nuvem)
st.markdown("""
<style>
    /* Estilo geral de fundo */
    .stApp {
        background-color: #f8fafc;
    }
    /* Estilo do título da empresa */
    .company-header {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0px;
    }
    .company-sub {
        color: #64748b;
        font-size: 0.85rem;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }
    /* Estilo para a sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Estado de Sessão (Login)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True  # Mantém logado para visualização do painel

# --- TELA DE LOGIN ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; color: #1e293b;'>🔷 VANGUARD</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>SISTEMAS DE GESTÃO</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #94a3b8;'>\"Controle absoluto. Operação simples.\"</p>", unsafe_allow_html=True)
            
            st.text_input("Usuário / Login", key="login_user")
            st.text_input("Senha", type="password", key="login_pass")
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Entrar no Sistema", use_container_width=True, type="primary"):
                st.session_state.logged_in = True
                st.rerun()

# --- TELA PRINCIPAL (LOGADO) ---
else:
    # BARRA LATERAL (SIDEBAR)
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; margin-bottom:0;'>🔷 VANGUARD</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.75rem; color: #94a3b8;'>SISTEMAS DE GESTÃO</p>", unsafe_allow_html=True)
        st.divider()
        
        # Perfil
        with st.container():
            st.markdown("**Master - CMDTC SERVIÇOS LTDA**")
            st.caption("@user | Setor: Diretoria")
        
        st.divider()
        st.markdown("**NAVEGAÇÃO**")
        
        # Menu limpo usando Selectbox nativo (sem bolinhas feias de radio button)
        menu = st.selectbox(
            "Menu Principal",
            ["• Boas-vindas", "Comercial", "Recursos Humanos", "Administrativo", "Financeiro"],
            label_visibility="collapsed"
        )
        
        st.divider()
        if st.button("🚪 Sair do Sistema", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ÁREA DE CONTEÚDO
    if menu == "• Boas-vindas":
        # Cabeçalho da Empresa
        st.markdown("<div class='company-header'>🔷 VANGUARD</div>", unsafe_allow_html=True)
        st.markdown("<div class='company-sub'>SISTEMAS DE GESTÃO — \"Controle absoluto. Operação simples.\"</div>", unsafe_allow_html=True)
        
        # 1. CARDS DE INDICADORES (NATIVOS - NUNCA SUMIRÃO)
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        with kpi1:
            with st.container(border=True):
                st.caption("STATUS DO PLANO")
                st.markdown("### 🟢 ATIVO")
                
        with kpi2:
            with st.container(border=True):
                st.caption("MÓDULOS CONTRATADOS")
                st.markdown("### 4 Módulos")
                
        with kpi3:
            with st.container(border=True):
                st.caption("VENCIMENTO")
                st.markdown("### Dia 10")
                
        with kpi4:
            with st.container(border=True):
                st.caption("FORMA DE PAGAMENTO")
                st.markdown("### Boleto Bancário")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Módulos e Recursos Habilitados")
        st.caption("Abaixo estão os acessos ativos para o perfil da sua empresa. Utilize o menu lateral para navegar.")

        # 2. CARDS DOS MÓDULOS (NATIVOS E ELEGANTES)
        mod1, mod2, mod3 = st.columns(3)
        
        with mod1:
            with st.container(border=True):
                st.markdown("#### Módulo Comercial")
                st.write("Gestão de propostas, orçamentos, contratos e carteira de clientes.")
                st.info("Disponível")
                
        with mod2:
            with st.container(border=True):
                st.markdown("#### Recursos Humanos (RH)")
                st.write("Gestão de colaboradores, equipes, cargos e contatos operacionais.")
                st.info("Disponível")
                
        with mod3:
            with st.container(border=True):
                st.markdown("#### Central Administrativa")
                st.write("Configurações do sistema, logo corporativa para laudos e gestão de acessos.")
                st.info("Disponível")

        st.markdown("<br>", unsafe_allow_html=True)

        # 3. SEÇÃO DE AVISOS E SUPORTE
        inf1, inf2 = st.columns([2, 1])
        
        with inf1:
            with st.container(border=True):
                st.markdown("### 📢 Avisos & Atualizações do Sistema")
                st.markdown("""
                * **Personalização de Documentos:** Cadastre a logomarca da sua empresa no módulo Administrativo para aplicar nos relatórios.
                * **Segurança da Conta:** Mantenha as senhas individuais dos usuários atualizadas e evite compartilhamento de logins.
                """)
            
        with inf2:
            with st.container(border=True):
                st.markdown("### 🛠️ Atendimento e Suporte")
                st.write("Precisa alterar seu plano ou adicionar novos usuários?")
                st.code("suporte@vanguarderp.com.br")

    else:
        st.title(f"Módulo: {menu}")
        st.info("Esta seção está pronta para receber as telas e funcionalidades específicas deste módulo.")
