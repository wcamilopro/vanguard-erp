import streamlit as st

def aplicar_estilos_customizados():
    """CSS apenas para estruturação. As cores vêm do config.toml."""
    st.markdown(
        """
        <style>
            .block-container { padding-top: 2rem !important; }
            header { visibility: hidden !important; }
            #MainMenu { visibility: hidden !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

def aplicar_fundo_login():
    """Mantido apenas para compatibilidade de importação no app.py"""
    pass

def renderizar_card_usuario(nome_empresa, usuario, setor):
    """Renderiza o cartão do usuário na barra lateral."""
    st.markdown(
        f"""
        <div style="background-color: #0F172A; padding: 14px; border-radius: 8px; border: 1px solid #334155; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);">
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
                <span style="background-color: #050810; color: #E2E8F0; font-size: 10px; padding: 2px 8px; border-radius: 4px; font-weight: 600;">
                    {setor}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
