import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Ajuste crucial para TELA CHEIA / WIDE)
st.set_page_config(
    page_title="Vanguard | Sistemas de Gestão",
    page_icon="🔺",
    layout="wide",  # Impede que o layout fique espremido no meio da tela
    initial_sidebar_state="expanded"
)

# 2. ESTILIZAÇÃO CSS CUSTOMIZADA (Fim do visual truncado)
st.markdown("""
<style>
    /* Estilização Geral e Fundo */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Remover margens excessivas do topo no Streamlit */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100% !important;
    }

    /* Cards de Indicadores (Métricas do Topo) */
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #6c757d;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 1.3rem;
        font-weight: 800;
        color: #1e293b;
    }
    .status-active {
        color: #10b981;
    }

    /* Cards dos Módulos Habilitados */
    .module-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .module-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 10px;
    }
    .module-desc {
        font-size: 0.9rem;
        color: #64748b;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    /* Estilização da Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    [data-testid="stSidebar"] * {
        color: #f8fafc;
    }
    
    /* Badges e Tags */
    .badge-available {
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        width: fit-content;
    }
</style>
""", unsafe_allow_html=True)

# 3. ESTADO DA SESSÃO (Simulação de Login para testes)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True  # Padrão logado para visualização do layout

# --- TELA DE LOGIN (se não estiver logado) ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<h2 style='text-align: center; color: #1e293b;'>🔺 VANGUARD</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #64748b;'>SISTEMAS DE GESTÃO</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            user = st.text_input("Usuário / Login")
            password = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar no Sistema", use_container_width=True)
            if submit:
                st.session_state.logged_in = True
                st.rerun()

# --- ÁREA LOGADA / DASHBOARD PRINCIPAL ---
else:
    # BARRA LATERAL (SIDEBAR)
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>🔺 VANGUARD</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #94a3b8;'>SISTEMAS DE GESTÃO</p>", unsafe_allow_html=True)
        st.divider()
        
        # Perfil do Usuário
        st.markdown("""
            <div style='background-color: #1e293b; padding: 12px; border-radius: 8px; margin-bottom: 20px;'>
                <strong style='color: #f8fafc;'>Master - CMDTC SERVIÇOS LTDA</strong><br>
                <small style='color: #94a3b8;'>@user | Setor: Diretoria</small>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### NAVEGAÇÃO")
        menu = st.radio(
            "Selecione a página:",
            ["• Boas-vindas", "Comercial", "Recursos Humanos", "Administrativo", "Financeiro"],
            label_visibility="collapsed"
        )
        
        st.divider()
        if st.button("🚪 Sair do Sistema", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # CONTEÚDO PRINCIPAL (DASHBOARD)
    if menu == "• Boas-vindas":
        # Métricas do Topo em 4 Colunas bem espaçadas
        m1, m2, m3, m4 = st.columns(4)
        
        with m1:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">Status do Plano</div>
                    <div class="metric-value status-active">● ATIVO</div>
                </div>
            """, unsafe_allow_html=True)
            
        with m2:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">Módulos Contratados</div>
                    <div class="metric-value">4 Módulos</div>
                </div>
            """, unsafe_allow_html=True)
            
        with m3:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">Vencimento</div>
                    <div class="metric-value">Dia 10</div>
                </div>
            """, unsafe_allow_html=True)
            
        with m4:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-title">Forma de Pagamento</div>
                    <div class="metric-value">Boleto Bancário</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Módulos e Recursos Habilitados")
        st.caption("Abaixo estão os acessos ativos para o perfil da sua empresa. Utilize o menu lateral para navegar.")

        # Grid de Módulos (3 Colunas)
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.markdown("""
                <div class="module-card">
                    <div>
                        <div class="module-title">Módulo Comercial</div>
                        <div class="module-desc">Gestão de propostas, orçamentos, contratos e carteira de clientes.</div>
                    </div>
                    <span class="badge-available">Disponível</span>
                </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown("""
                <div class="module-card">
                    <div>
                        <div class="module-title">Recursos Humanos (RH)</div>
                        <div class="module-desc">Gestão de colaboradores, equipes, cargos e contatos operacionais.</div>
                    </div>
                    <span class="badge-available">Disponível</span>
                </div>
            """, unsafe_allow_html=True)
            
        with c3:
            st.markdown("""
                <div class="module-card">
                    <div>
                        <div class="module-title">Central Administrativa</div>
                        <div class="module-desc">Configurações do sistema, logo corporativa para laudos e gestão de acessos.</div>
                    </div>
                    <span class="badge-available">Disponível</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Seção Inferior: Avisos e Suporte
        inf1, inf2 = st.columns([2, 1])
        
        with inf1:
            st.info("""
            **Avisos & Atualizações do Sistema**
            * **Personalização de Documentos:** Cadastre a logomarca da sua empresa no módulo Administrativo para aplicar nos relatórios.
            * **Segurança da Conta:** Mantenha as senhas individuais dos usuários atualizadas e evite compartilhamento de logins.
            """)
            
        with inf2:
            st.success("""
            **Atendimento e Suporte**  
            Precisa alterar seu plano ou adicionar novos usuários?  
            📧 **suporte@vanguarderp.com.br**
            """)

    else:
        st.title(f"Módulo: {menu}")
        st.info("Esta seção está pronta para receber os formulários e tabelas de dados.")
