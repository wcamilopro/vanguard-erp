import streamlit as st

def aplicar_estilos_customizados():
    """
    Injeta o CSS global ajustando a barra lateral (sidebar) para um tom escuro 
    elegante e corrigindo o espaçamento dos componentes.
    """
    st.markdown(
        """
        <style>
            /* ESCURECE A BARRA LATERAL (SIDEBAR) EM UM TOM SÓBRIO CORPORATIVO */
            [data-testid="stSidebar"] {
                background-color: #0B1120 !important;
                border-right: 1px solid #1E293B !important;
            }

            /* Garante que os textos e elementos da sidebar fiquem legíveis */
            [data-testid="stSidebar"] p, 
            [data-testid="stSidebar"] span, 
            [data-testid="stSidebar"] label {
                color: #F8FAFC !important;
            }

            /* Ajuste das abas (Tabs) */
            .stTabs [data-baseweb="tab-highlight"] {
                background-color: #1E40AF !important;
            }
            .stTabs [data-baseweb="tab"][aria-selected="true"] p {
                color: #1E40AF !important;
                font-weight: 700 !important;
            }
            .stTabs [data-baseweb="tab"] p {
                font-weight: 600 !important;
            }

            /* Botões primários */
            button[kind="primary"], 
            .stFormSubmitButton > button[kind="primary"],
            [data-testid="baseButton-primary"] {
                background-color: #1E40AF !important;
                background: #1E40AF !important;
                color: #FFFFFF !important;
                border: 1px solid #1E40AF !important;
                font-weight: 600 !important;
                transition: all 0.2s ease;
            }
            button[kind="primary"]:hover, 
            .stFormSubmitButton > button[kind="primary"]:hover,
            [data-testid="baseButton-primary"]:hover {
                background-color: #1D4ED8 !important;
                background: #1D4ED8 !important;
                color: #FFFFFF !important;
            }

            input {
                border-radius: 6px !important;
            }
            
            .block-container {
                padding-top: 2.2rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    """Fundo neutro e limpo para a tela de login."""
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
    Renderiza o cartão do usuário perfeitamente ajustado para o fundo escuro da barra lateral.
    """
    st.markdown(
        f"""
        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <div style="background-color: #1E40AF; color: white; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px;">
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
