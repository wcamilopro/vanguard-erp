import streamlit as st


def aplicar_estilos_customizados():
    """CSS geral do sistema (Menu lateral e painel administrativo)."""
    st.markdown(
        """
        <style>
            /* Elementos padrão do Streamlit */
            .block-container { padding-top: 2rem !important; }
            header { visibility: hidden !important; }
            #MainMenu { visibility: hidden !important; }
            .main { background-color: #F0F4F8 !important; }

            /* MENU LATERAL (SIDEBAR ESCURO EXCLUSIVO) */
            section[data-testid="stSidebar"] {
                background-color: #0F172A !important;
                border-right: 1px solid #1E293B !important;
            }
            
            section[data-testid="stSidebar"] p, 
            section[data-testid="stSidebar"] span, 
            section[data-testid="stSidebar"] div,
            section[data-testid="stSidebar"] label {
                color: #94A3B8 !important;
            }

            section[data-testid="stSidebar"] .stButton > button {
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid #334155 !important;
                border-radius: 6px !important;
                font-weight: 500 !important;
                width: 100% !important;
            }

            section[data-testid="stSidebar"] .stButton > button:hover {
                background-color: #334155 !important;
                color: #FFFFFF !important;
                border-color: #2563EB !important;
            }

            section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
                background-color: #2563EB !important;
                color: #FFFFFF !important;
                border: none !important;
                font-weight: 700 !important;
            }

            /* INPUTS E FORMULÁRIOS DA TELA PRINCIPAL */
            .stTextInput input, .stPasswordInput input, .stNumberInput input, .stSelectbox select {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 6px !important;
            }

            div[data-baseweb="input"] {
                background-color: #FFFFFF !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 6px !important;
            }

            div[data-testid="stForm"], 
            div[data-testid="stDialog"],
            div[data-baseweb="modal"] {
                background-color: #FFFFFF !important;
                border-radius: 8px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def aplicar_fundo_login():
    """Define o estilo de fundo e contraste perfeito para a tela de login."""
    st.markdown(
        """
        <style>
            /* Fundo suave que destaca a logo branca/azul perfeitamente */
            .stApp, [data-testid="stAppViewContainer"], .main { 
                background-color: #334155 !important;  #(#E2E8F0)
            }
            
            /* Cartão central do formulário de login bem destacado */
            div[data-testid="stForm"] {
                background-color: #FFFFFF !important;
                border: 1px solid #CBD5E1 !important;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1) !important;
                border-radius: 12px !important;
                padding: 10px !important;
            }

            /* Garante que os rótulos (labels) dos inputs de login fiquem escuros e legíveis */
            .stTextInput label, .stPasswordInput label {
                color: #334155 !important;
                font-weight: 600 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def renderizar_card_usuario(nome_empresa, usuario, setor):
    """Renderiza o cartão do usuário na barra lateral."""
    st.markdown(
        f"""
        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <div style="background-color: #2563EB; color: white; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px;">
                    {str(nome_empresa)[0].upper()}
                </div>
                <div style="overflow: hidden;">
                    <div style="color: #F8FAFC; font-weight: 700; font-size: 13px; line-height: 1.2; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                        {nome_empresa}
                    </div>
                    <div style="color: #94A3B8; font-size: 11px; margin-top: 2px;">
                        @{usuario}
                    </div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px; padding-top: 8px; border-top: 1px solid #334155;">
                <span style="color: #94A3B8; font-size: 10px;">Setor:</span>
                <span style="background-color: #0F172A; color: #E2E8F0; font-size: 10px; padding: 2px 8px; border-radius: 4px; font-weight: 600;">
                    {setor}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
