import streamlit as st

def aplicar_estilos_customizados():
    """
    Injeta o CSS global com o Azul Corporativo Sóbrio (#1E40AF), 
    mantendo a interface limpa, profissional e leve.
    """
    st.markdown(
        """
        <style>
            /* Variáveis e destaque das abas (Tabs) */
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

            /* Botões primários com Azul Corporativo Equilibrado */
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
    """Cartão do usuário na barra lateral harmonizado."""
    st.markdown(
        f"""
        <div style="background-color: #0F172A; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 24px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <div style="background-color: #1E40AF; color: white; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px;">
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
