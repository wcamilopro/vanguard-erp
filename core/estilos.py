import streamlit as st

def aplicar_estilos_customizados():
    """Estilos gerais do sistema."""
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] { background-color: #0B1120 !important; }
            .stApp { background-color: #050810 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    """Reset total da tela de login para garantir o padrão visual."""
    st.markdown(
        """
        <style>
            /* 1. Força o fundo da tela para preto profundo */
            .stApp {
                background-color: #050810 !important;
            }

            /* 2. Força o Card de Login para azul escuro sólido (diferente do fundo) */
            [data-testid="stContainer"] {
                background-color: #1E293B !important;
                border: 1px solid #334155 !important;
                border-radius: 12px !important;
                padding: 30px !important;
                box-shadow: 0 10px 25px rgba(0,0,0,0.5) !important;
            }

            /* 3. Força TODOS os botões dentro do card a serem azuis corporativos */
            [data-testid="stContainer"] button {
                background-color: #1E40AF !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 6px !important;
                font-weight: 600 !important;
            }
            
            /* 4. Efeito de Hover */
            [data-testid="stContainer"] button:hover {
                background-color: #1D4ED8 !important;
                color: #FFFFFF !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def renderizar_card_usuario(nome_empresa, usuario, setor):
    """Renderiza o cartão do usuário na barra lateral."""
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
