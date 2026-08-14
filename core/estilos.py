import streamlit as st

def aplicar_estilos_customizados():
    """Estilos gerais do sistema (Menu e páginas internas)."""
    st.markdown(
        """
        <style>
            /* Fundo geral da aplicação e sidebar */
            [data-testid="stAppViewContainer"] { background-color: #050810 !important; }
            [data-testid="stSidebar"] { background-color: #0B1120 !important; border-right: 1px solid #1E293B !important; }
            [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #F8FAFC !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    """Estilo exclusivo e cirúrgico para a tela de login."""
    st.markdown(
        """
        <style>
            /* 1. FUNDO DA TELA GERAL (Preto/Azul muito escuro) */
            [data-testid="stAppViewContainer"] {
                background-color: #050810 !important;
            }

            /* 2. O CARD DO LOGIN (Azul acinzentado mais claro para destacar do fundo) */
            /* stVerticalBlockBorderWrapper é a classe interna EXATA do st.container(border=True) */
            [data-testid="stVerticalBlockBorderWrapper"] {
                background-color: #1E293B !important;
                border: 1px solid #334155 !important;
                border-radius: 12px !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.8) !important;
            }

            /* 3. CORES DOS TEXTOS DOS CAMPOS NO LOGIN */
            [data-testid="stVerticalBlockBorderWrapper"] p {
                color: #F8FAFC !important;
            }

            /* 4. TODOS OS BOTÕES DO LOGIN (Matando o vermelho e os brancos) */
            [data-testid="stVerticalBlockBorderWrapper"] button {
                background-color: #1E40AF !important; 
                color: #FFFFFF !important;
                border: 1px solid #1D4ED8 !important;
                border-radius: 6px !important;
                font-weight: 600 !important;
                padding-top: 10px !important;
                padding-bottom: 10px !important;
            }
            
            /* 5. EFEITO AO PASSAR O MOUSE (Hover) */
            [data-testid="stVerticalBlockBorderWrapper"] button:hover {
                background-color: #1D4ED8 !important;
                border: 1px solid #3B82F6 !important;
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
