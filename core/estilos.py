import streamlit as st

def aplicar_estilos_customizados():
    st.markdown(
        """
        <style>
            /* SIDEBAR */
            [data-testid="stSidebar"] {
                background-color: #0B1120 !important;
                border-right: 1px solid #1E293B !important;
            }
            [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #F8FAFC !important; }
            
            /* GERAL */
            .stApp { background-color: #0F172A !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    st.markdown(
        """
        <style>
            /* Fundo da Página */
            .stApp {
                background-color: #0F172A !important;
            }
            
            /* Container do Login - Aumentando a especificidade para garantir a sobreposição */
            div.stApp div[data-testid="stContainer"] {
                background-color: #1E293B !important;
                border-radius: 16px !important;
                border: 1px solid #334155 !important;
                box-shadow: 0 25px 35px -5px rgba(0, 0, 0, 0.7) !important;
                padding: 30px !important;
            }

            /* Labels */
            div.stApp div[data-testid="stContainer"] label p {
                color: #F8FAFC !important;
                font-weight: 600 !important;
            }

            /* BOTÕES - PADRONIZAÇÃO TOTAL (Primary e Secondary ficam iguais) */
            div.stApp div[data-testid="stContainer"] .stButton > button {
                background-color: #1E40AF !important; /* Azul Corporativo */
                color: #FFFFFF !important;
                border: 1px solid #1E40AF !important;
                font-weight: 600 !important;
                border-radius: 6px !important;
                width: 100% !important;
            }
            
            div.stApp div[data-testid="stContainer"] .stButton > button:hover {
                background-color: #1D4ED8 !important; /* Azul mais claro no hover */
                border: 1px solid #2563EB !important;
                color: #FFFFFF !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def renderizar_card_usuario(nome_empresa, usuario, setor):
    st.markdown(
        f"""
        <div style="background-color: #1E293B; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="background-color: #1E40AF; color: white; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                    {str(nome_empresa)[0].upper()}
                </div>
                <div>
                    <div style="color: #F8FAFC; font-weight: 700; font-size: 13px;">{nome_empresa}</div>
                    <div style="color: #94A3B8; font-size: 11px;">@{usuario}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
