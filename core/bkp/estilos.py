import streamlit as st

def carregar_css_customizado():
    st.markdown("""
    <style>
    /* ==========================================================================
       1. CABEÇALHO E ESTRUTURA GERAL
       ========================================================================== */
    header[data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0px !important;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }

    /* Fundo da Plataforma */
    .stApp {
        background-color: #0F172A !important;
    }

    /* ==========================================================================
       2. MOLDURA ENTERPRISE DA TELA DE LOGIN (CARD FLUTUANTE)
       ========================================================================== */
    /* Container do Login (Coluna Central) */
    div[data-testid="column"]:nth-child(2) {
        background-color: rgba(30, 41, 59, 0.95) !important;
        padding: 35px 30px !important;
        border-radius: 16px !important;
        border: 1px solid rgba(0, 163, 255, 0.4) !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 163, 255, 0.15) !important;
        backdrop-filter: blur(10px) !important;
    }

    /* Campos de Entrada (Inputs) no Login */
    div[data-testid="column"]:nth-child(2) input {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }

    div[data-testid="column"]:nth-child(2) input:focus {
        border-color: #00A3FF !important;
        box-shadow: 0 0 8px rgba(0, 163, 255, 0.4) !important;
    }

    /* Botão Principal de Login */
    div[data-testid="column"]:nth-child(2) button[kind="primary"] {
        background-color: #00A3FF !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.2s ease-in-out !important;
    }

    div[data-testid="column"]:nth-child(2) button[kind="primary"]:hover {
        background-color: #0082CC !important;
        box-shadow: 0 4px 12px rgba(0, 163, 255, 0.4) !important;
    }

    /* ==========================================================================
       3. PAINEL LATERAL E BOTÕES DE NAVEGAÇÃO
       ========================================================================== */
    [data-testid="stSidebar"] {
        background-color: #0B1120 !important;
        border-right: 1px solid #1E293B !important;
    }

    /* Botões de Módulo na Sidebar */
    [data-testid="stSidebar"] div.stButton > button {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        width: 100% !important;
        font-weight: 600 !important;
        text-align: left !important;
        padding: 10px 14px !important;
        margin-bottom: 4px !important;
        transition: all 0.2s ease-in-out !important;
    }

    [data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #334155 !important;
        border-color: #00A3FF !important;
        color: #FFFFFF !important;
    }

    /* Botão Vermelho de Sair */
    [data-testid="stSidebar"] div.stButton > button[key="btn_logout"] {
        background-color: #7F1D1D !important;
        border-color: #991B1B !important;
        color: #FEE2E2 !important;
    }

    [data-testid="stSidebar"] div.stButton > button[key="btn_logout"]:hover {
        background-color: #DC2626 !important;
        color: #FFFFFF !important;
    }

    /* ==========================================================================
       4. ESTILIZAÇÃO DAS ABAS (st.tabs)
       ========================================================================== */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: #94A3B8 !important;
        font-weight: 600 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00A3FF !important;
        border-bottom-color: #00A3FF !important;
    }
    </style>
    """, unsafe_allow_html=True)


def aplicar_estilos_customizados():
    carregar_css_customizado()


def aplicar_fundo_login():
    carregar_css_customizado()