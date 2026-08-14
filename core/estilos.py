import streamlit as st


def aplicar_estilos_customizados():
    """CSS Global Vanguard - Estilo SaaS Enterprise Clean."""
    st.markdown(
        """
        <style>
        /* ESPAÇAMENTO GLOBAL DA PÁGINA */
        [data-testid="stMainBlockContainer"], 
        .main .block-container {
            padding-top: 1.8rem !important;
            padding-bottom: 2rem !important;
            max-width: 1240px !important;
        }

        /* MENU LATERAL (SLATE VANGUARD) */
        [data-testid="stSidebar"] {
            background-color: #0F172A !important;
            border-right: 1px solid #1E293B !important;
        }
        
        [data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }

        /* Botões da Sidebar */
        [data-testid="stSidebar"] div.stButton > button {
            width: 100% !important;
            background-color: #1E293B !important;
            color: #CBD5E1 !important;
            border: 1px solid #334155 !important;
            border-radius: 6px !important;
            padding: 8px 12px !important;
            font-size: 13.5px !important;
            font-weight: 500 !important;
            text-align: left !important;
            margin-bottom: 4px !important;
            box-shadow: none !important;
            transition: all 0.2s ease-in-out !important;
        }

        [data-testid="stSidebar"] div.stButton > button:hover {
            background-color: #2563EB !important;
            border-color: #3B82F6 !important;
            color: #FFFFFF !important;
        }

        /* TÍTULOS E TEXTOS PRINCIPAIS */
        section.main h1, section.main h2, section.main h3 {
            color: #0F172A !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px !important;
        }

        section.main p, .stMarkdown p {
            color: #334155 !important;
        }

        /* INPUTS DA ÁREA PRINCIPAL */
        section.main div[data-baseweb="input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 6px !important;
        }

        section.main div[data-baseweb="input"] input {
            color: #0F172A !important;
            background-color: #FFFFFF !important;
        }

        /* FILE UPLOADER BRANCO CLEAN */
        section.main [data-testid="stFileUploader"],
        section.main [data-testid="stFileUploaderDropzone"],
        section.main section[data-testid="stFileUploadDropzone"],
        section.main div[data-testid="stFileUploader"] section {
            background-color: #FFFFFF !important;
            border: 2px dashed #2563EB !important;
            border-radius: 8px !important;
        }

        section.main [data-testid="stFileUploader"] *,
        section.main [data-testid="stFileUploaderDropzone"] *,
        section.main section[data-testid="stFileUploadDropzone"] * {
            background-color: transparent !important;
            color: #0F172A !important;
        }

        section.main [data-testid="stFileUploader"] button,
        section.main [data-testid="stFileUploaderDropzone"] button {
            background-color: #F1F5F9 !important;
            color: #0F172A !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
        }

        /* Métricas */
        [data-testid="stMetricValue"] {
            color: #0F172A !important;
            font-weight: 800 !important;
        }

        [data-testid="stMetricLabel"] {
            color: #475569 !important;
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def aplicar_fundo_login():
    """Tela de Login Vanguard sem Emojis."""
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%) !important;
        }

        header, footer { visibility: hidden; }

        .stApp h1, .stApp h2, .stApp h3 {
            color: #0F172A !important;
        }
        
        .stApp p, .stApp span, .stApp label {
            color: #475569 !important;
            font-weight: 500 !important;
        }

        /* CARD CENTRAL DE LOGIN */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
            padding: 32px !important;
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08) !important;
        }

        /* INPUTS */
        div[data-baseweb="input"], 
        div[data-baseweb="base-input"] {
            background-color: #F8FAFC !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 6px !important;
        }

        div[data-baseweb="input"] input {
            color: #0F172A !important;
            background-color: transparent !important;
        }

        div[data-baseweb="input"] * {
            background-color: transparent !important;
        }

        div[data-baseweb="input"] svg {
            fill: #64748B !important;
        }

        /* BOTÃO ENTRAR */
        div[data-testid="stFormSubmitButton"] > button {
            width: 100% !important;
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border-radius: 6px !important;
            border: none !important;
            padding: 10px 16px !important;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.25) !important;
            transition: all 0.2s ease !important;
        }

        div[data-testid="stFormSubmitButton"] > button:hover {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
        }

        /* BOTÕES AUXILIARES */
        .stApp section.main div.stButton > button {
            width: 100% !important;
            background-color: #FFFFFF !important;
            color: #475569 !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 6px !important;
            padding: 8px 12px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            margin-top: 4px !important;
            margin-bottom: 4px !important;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03) !important;
            transition: all 0.2s ease-in-out !important;
        }

        .stApp section.main div.stButton > button:hover {
            background-color: #F1F5F9 !important;
            border-color: #2563EB !important;
            color: #2563EB !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def renderizar_card_usuario(nome_empresa: str, usuario: str, setor: str):
    """Card do usuário na barra lateral."""
    inicial = nome_empresa[0].upper() if nome_empresa else "V"

    st.sidebar.markdown(
        f"""
        <div style="
            background-color: #1E293B;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 16px;
        ">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="
                    width: 36px; height: 36px; border-radius: 6px;
                    background: linear-gradient(135deg, #2563EB, #1D4ED8);
                    display: flex; align-items: center; justify-content: center;
                    font-weight: 700; color: #FFFFFF; font-size: 15px; flex-shrink: 0;
                ">
                    {inicial}
                </div>
                <div style="overflow: hidden;">
                    <div style="font-weight: 600; color: #F8FAFC; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{nome_empresa}">
                        {nome_empresa}
                    </div>
                    <div style="color: #93C5FD; font-size: 11px;">@{usuario}</div>
                </div>
            </div>
            <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid #334155; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #94A3B8; font-size: 10px;">Setor:</span>
                <span style="background: #0F172A; color: #60A5FA; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">
                    {setor}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )