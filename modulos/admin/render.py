import streamlit as st


def render():
    # Estilo agressivo e isolado para garantir visibilidade total dos textos e métricas nesta tela
    st.markdown(
        """
        <style>
            /* Força todas as fontes, labels e valores de métricas para um tom escuro legível */
            .main div[data-testid="stMetricValue"], 
            .main div[data-testid="stMetricLabel"],
            .main p, .main span, .main h1, .main h2, .main h3, .main label {
                color: #0F172A !important;
            }
            /* Garante destaque correto nos valores das métricas */
            div[data-testid="stMetricValue"] {
                font-size: 26px !important;
                font-weight: 700 !important;
                color: #0F172A !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Cabeçalho da Central Administrativa
    st.markdown(
        """
        <div style="padding: 10px 0;">
            <h2 style="color: #0F172A; margin: 0; font-family: 'Segoe UI', sans-serif;">⚙️ Central Administrativa & Licenciamento</h2>
            <p style="color: #475569; font-size: 14px; margin-top: 5px;">Gestão de assinaturas, usuários, permissões, faturas e dados da conta.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # DADOS DA SESSÃO
    empresa_nome = st.session_state.get(
        "empresa_nome", "Master - CMDTCSERVIÇOS LTDA"
    )

    # RESUMO DO PLANO E LICENÇA
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="Plano Ativo", value="Enterprise Pro", delta="SaaS Unlimited"
        )
    with c2:
        st.metric(
            label="Valor Mensal", value="R$ 490,00", delta="Venc. Dia 10"
        )
    with c3:
        st.metric(label="Situação", value="Ativo", delta="Regular")
    with c4:
        st.metric(label="Forma Pagamento", value="Boleto / PIX")

    st.markdown("<br>", unsafe_allow_html=True)

    # ABAS DE GESTÃO FINANCEIRA, USUÁRIOS E DADOS
    tab_faturas, tab_usuarios, tab_logo, tab_dados = st.tabs(
        [
            "💳 Faturas & Boletos",
            "👥 Gestão de Usuários & Senhas",
            "🖼️ Logo da Empresa",
            "🏢 Dados Cadastrais",
        ]
    )

    with tab_faturas:
        st.subheader("📄 Histórico de Faturas & Pagamentos")
        st.markdown(
            "<p style='color: #475569; font-size: 13px;'>Acompanhe o status dos pagamentos mensais da sua assinatura.</p>",
            unsafe_allow_html=True,
        )

        faturas = [
            {
                "Ref": "08/2026",
                "Vencimento": "10/08/2026",
                "Valor": "R$ 490,00",
                "Status": "Pago",
                "Acao": "Comprovante",
            },
            {
                "Ref": "09/2026",
                "Vencimento": "10/09/2026",
                "Valor": "R$ 490,00",
                "Status": "A Vencer",
                "Acao": "Imprimir Boleto",
            },
        ]

        for fat in faturas:
            with st.container():
                col_ref, col_venc, col_val, col_stat, col_btn = st.columns(
                    [1, 1.2, 1, 1.2, 1.5]
                )
                col_ref.markdown(f"**Ref:** {fat['Ref']}")
                col_venc.markdown(f"{fat['Vencimento']}")
                col_val.markdown(f"**{fat['Valor']}**")

                if fat["Status"] == "Pago":
                    col_stat.markdown(
                        "<span style='color: #059669; font-weight: 600;'>🟢 Pago</span>",
                        unsafe_allow_html=True,
                    )
                else:
                    col_stat.markdown(
                        "<span style='color: #D97706; font-weight: 600;'>🟡 A Vencer</span>",
                        unsafe_allow_html=True,
                    )

                if col_btn.button(
                    f"📄 {fat['Acao']}", key=f"btn_fat_{fat['Ref']}"
                ):
                    st.info(
                        f"Simulação: Gerando PDF referente à fatura {fat['Ref']}..."
                    )
            st.markdown(
                "<hr style='margin: 8px 0; border: 0; border-top: 1px solid #CBD5E1;'>",
                unsafe_allow_html=True,
            )

    with tab_usuarios:
        st.subheader("👥 Controle de Usuários e Privilégios")
        st.markdown(
            "<p style='color: #475569; font-size: 13px;'>Cadastre novos colaboradores, configure permissões de acesso aos módulos e gerencie o reset de senhas.</p>",
            unsafe_allow_html=True,
        )

        with st.expander("➕ Cadastrar Novo Usuário", expanded=False):
            with st.form("form_novo_usuario_admin"):
                col_u1, col_u2 = st.columns(2)
                with col_u1:
                    novo_username = st.text_input("Nome de Usuário / Login")
                    novo_setor = st.text_input("Setor / Função", value="Geral")
                with col_u2:
                    modulos_escolhidos = st.multiselect(
                        "Módulos Permitidos",
                        options=[
                            "Comercial",
                            "Recursos Humanos",
                            "Técnico",
                            "Financeiro",
                            "Administrativo",
                        ],
                        default=["Comercial"],
                    )

                st.info(
                    "🔑 **Regra de Segurança:** O usuário será cadastrado com a senha provisória padrão (**Trocar123**) e será obrigado a redefini-la no primeiro acesso."
                )

                btn_cadastrar_usuario = st.form_submit_button(
                    "Salvar Novo Usuário", type="primary"
                )

                if btn_cadastrar_usuario:
                    if novo_username:
                        # Aqui você integrará com a função do banco que cadastra o usuário com primeiro_acesso = True e senha "Trocar123"
                        st.success(
                            f"Usuário '{novo_username}' cadastrado com sucesso! Senha provisória: `Trocar123`"
                        )
                    else:
                        st.warning(
                            "Por favor, informe o nome de usuário/login."
                        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### 📋 Usuários Ativos na Empresa")

        # Exemplo simulado de listagem de usuários vinculados
        usuarios_cadastrados = [
            {
                "username": "admin",
                "setor": "Administrativo",
                "status": "Ativo",
                "primeiro_acesso": "Não",
            },
            {
                "username": "joao.comercial",
                "setor": "Comercial",
                "status": "Ativo",
                "primeiro_acesso": "Não",
            },
            {
                "username": "maria.rh",
                "setor": "Recursos Humanos",
                "status": "Aguardando Troca",
                "primeiro_acesso": "Sim",
            },
        ]

        for u in usuarios_cadastrados:
            col_info1, col_info2, col_info3, col_acao = st.columns(
                [1.5, 1, 1, 1.5]
            )
            col_info1.markdown(
                f"👤 **{u['username']}**<br><span style='font-size:11px; color:#64748B;'>Setor: {u['setor']}</span>",
                unsafe_allow_html=True,
            )
            col_info2.markdown(f"Status: **{u['status']}**")
            col_info3.markdown(f"Trocar Senha: **{u['primeiro_acesso']}**")

            if col_acao.button(
                f"🔄 Resetar Senha", key=f"reset_{u['username']}"
            ):
                # Aqui você chamará a função do banco para redefinir para "Trocar123" e setar primeiro_acesso = True
                st.success(
                    f"Senha de '{u['username']}' redefinida para 'Trocar123'. O usuário deverá trocá-la no próximo login."
                )

            st.markdown(
                "<hr style='margin: 6px 0; border: 0; border-top: 1px solid #CBD5E1;'>",
                unsafe_allow_html=True,
            )

    with tab_logo:
        st.subheader("🎨 Personalização de Logomarca")
        uploaded_logo = st.file_uploader(
            "Envie a logo da empresa (PNG ou JPG)", type=["png", "jpg", "jpeg"]
        )
        if uploaded_logo is not None:
            st.image(
                uploaded_logo,
                width=180,
                caption="Pré-visualização da Logo",
            )
            if st.button("💾 Salvar Logomarca", type="primary"):
                st.success("Logo salva com sucesso!")

    with tab_dados:
        st.subheader("🏢 Dados Cadastrais da Empresa")
        st.text_input("Razão Social", value=empresa_nome)
        st.text_input("CNPJ", value="00.000.000/0001-00")
        st.text_input("E-mail Financeiro", value="financeiro@empresa.com.br")
        if st.button("💾 Atualizar Dados", type="primary"):
            st.success("Dados cadastrais atualizados com sucesso!")
