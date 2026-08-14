import streamlit as st

def aplicar_estilos_customizados():
    """
    Injeta o CSS global da aplicação. 
    Aqui nós matamos o vermelho padrão e o azul "cheguei", substituindo pelo Dark Slate corporativo.
    """
    st.markdown(
        """
        <style>
            /* 1. MATA O VERMELHO DAS ABAS (TABS) E USA DARK SLATE */
            .stTabs [data-baseweb="tab-highlight"] {
                background-color: #0F172A !important;
            }
            .stTabs [data-baseweb="tab"][aria-selected="true"] p {
                color: #0F172A !important;
                font-weight: 700 !important;
            }
            .stTabs [data-baseweb="tab"] p {
                font-weight: 600 !important;
            }

            /* 2. MATA O AZUL/VERMELHO DOS BOTÕES E USA DARK SLATE */
            .stFormSubmitButton > button[kind="primary"],
            .stButton > button[kind="primary"] {
                background-color: #0F172A !important;
                color: #FFFFFF !important;
                border: 1px solid #0F172A !important;
                font-weight: 600 !important;
                transition: all 0.3s ease;
            }
            .stFormSubmitButton > button[kind="primary"]:hover,
            .stButton > button[kind="primary"]:hover {
                background-color: #1E293B !important;
                border: 1px solid #1E293B !important;
                color: #FFFFFF !important;
            }

            /* 3. Ajuste de fontes e inputs globais */
            input {
                border-radius: 6px !important;
            }
            
            /* Remove a margem superior indesejada em algumas telas */
            .block-container {
                padding-top: 2.2rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    """
    Aplica um fundo neutro, limpo e profissional para a tela de login, 
    removendo qualquer fundo colorido forte que estivesse antes.
    """
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #F8FAFC !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def renderizar_card_usuario(nome_empresa, usuario, setor):
    """
    Renderiza o cartão com os dados do usuário na barra lateral.
    Visual Dark Slate, combinando com o novo padrão.
    """
    st.markdown(
        f"""
        <div style="background-color: #0F172A; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 24px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <div style="background-color: #2563EB; color: white; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px;">
                    {str(nome_empresa)[0].upper()}
                </div>
                <div>
                    <div style="color: #F8FAFC; font-weight: 700; font-size: 13px; line-height: 1.2;">
                        {nome_empresa}
                    </div>
                    <div style="color: #94A3B8; font-size: 11px; margin-top: 2px;">
                        @{usuario}
                    </div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px; padding-top: 8px; border-top: 1px solid #1E293B;">
                <span style="color: #64748B; font-size: 10px;">Setor:</span>
                <span style="background-color: #1E293B; color: #E2E8F0; font-size: 10px; padding: 2px 8px; border-radius: 4px; font-weight: 600;">
                    {setor}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
