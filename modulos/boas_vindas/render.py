import streamlit as st


def render():
    # 1. INDICADORES DO TOPO (CARDS CLEAN)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div style="background: #FFFFFF; padding: 14px 16px; border-radius: 8px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <div style="color: #64748B; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Status do Plano</div>
                <div style="color: #16A34A; font-size: 18px; font-weight: 800; margin-top: 4px;">● ATIVO</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="background: #FFFFFF; padding: 14px 16px; border-radius: 8px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <div style="color: #64748B; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Módulos Contratados</div>
                <div style="color: #0F172A; font-size: 18px; font-weight: 800; margin-top: 4px;">4 Módulos</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style="background: #FFFFFF; padding: 14px 16px; border-radius: 8px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <div style="color: #64748B; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Vencimento</div>
                <div style="color: #0F172A; font-size: 18px; font-weight: 800; margin-top: 4px;">Dia 10</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div style="background: #FFFFFF; padding: 14px 16px; border-radius: 8px; border: 1px solid #E2E8F0; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <div style="color: #64748B; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Forma de Pagamento</div>
                <div style="color: #0F172A; font-size: 18px; font-weight: 800; margin-top: 4px;">Boleto Bancário</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # 2. TÍTULO E GRID DE MÓDULOS
    st.markdown(
        """
        <div style="border-bottom: 2px solid #E2E8F0; padding-bottom: 8px; margin-bottom: 20px;">
            <h2 style="margin:0; font-size: 20px; color: #0F172A; font-weight: 700;">Módulos e Recursos Habilitados</h2>
            <p style="margin: 4px 0 0 0; color: #64748B; font-size: 13px;">Abaixo estão os acessos ativos para o perfil da sua empresa. Utilize o menu lateral para navegar.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    m_col1, m_col2, m_col3 = st.columns(3)

    with m_col1:
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-weight: 700; color: #0F172A; font-size: 15px; margin-bottom: 6px;">Módulo Comercial</div>
                    <p style="color: #475569; font-size: 13px; line-height: 1.4; margin: 0;">Gestão de propostas, orçamentos, contratos e carteira de clientes.</p>
                </div>
                <div style="margin-top: 16px;">
                    <span style="background: #EFF6FF; color: #2563EB; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; border: 1px solid #BFDBFE;">
                        Disponível
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m_col2:
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-weight: 700; color: #0F172A; font-size: 15px; margin-bottom: 6px;">Recursos Humanos (RH)</div>
                    <p style="color: #475569; font-size: 13px; line-height: 1.4; margin: 0;">Gestão de colaboradores, equipes, cargos e contatos operacionais.</p>
                </div>
                <div style="margin-top: 16px;">
                    <span style="background: #EFF6FF; color: #2563EB; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; border: 1px solid #BFDBFE;">
                        Disponível
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m_col3:
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div style="font-weight: 700; color: #0F172A; font-size: 15px; margin-bottom: 6px;">Central Administrativa</div>
                    <p style="color: #475569; font-size: 13px; line-height: 1.4; margin: 0;">Configurações do sistema, logo corporativa para laudos e gestão de acessos.</p>
                </div>
                <div style="margin-top: 16px;">
                    <span style="background: #EFF6FF; color: #2563EB; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; border: 1px solid #BFDBFE;">
                        Disponível
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # 3. SEÇÕES INFORMATIVAS
    a_col1, a_col2 = st.columns([1.6, 1])

    with a_col1:
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                <h3 style="margin-top:0; font-size: 15px; color: #0F172A; font-weight: 700; border-bottom: 1px solid #F1F5F9; padding-bottom: 8px;">
                    Avisos & Atualizações do Sistema
                </h3>
                <ul style="color: #475569; font-size: 13px; line-height: 1.6; padding-left: 18px; margin-bottom: 0;">
                    <li><strong>Personalização de Documentos:</strong> Cadastre a logomarca da sua empresa no módulo Administrativo para aplicar nos relatórios.</li>
                    <li><strong>Segurança da Conta:</strong> Mantenha as senhas individuais dos usuários atualizadas e evite compartilhamento de logins.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with a_col2:
        st.markdown(
            """
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px;">
                <h3 style="margin-top:0; font-size: 15px; color: #0F172A; font-weight: 700; border-bottom: 1px solid #E2E8F0; padding-bottom: 8px;">
                    Atendimento e Suporte
                </h3>
                <p style="color: #475569; font-size: 13px; line-height: 1.4; margin-bottom: 12px;">
                    Precisa alterar seu plano ou adicionar novos usuários?
                </p>
                <div style="font-size: 12px; font-weight: 600; color: #0F172A; background: #FFFFFF; padding: 8px 12px; border-radius: 6px; border: 1px solid #CBD5E1; text-align: center;">
                    suporte@vanguardgestao.com.br
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )