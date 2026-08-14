import streamlit as st


def render():
    st.title("⚙️ Central Administrativa & Licenciamento")
    st.caption("Gestão de assinaturas, faturas, limites e dados da conta.")
    st.markdown("---")

    # DADOS DA SESSÃO
    empresa_nome = st.session_state.get("empresa_nome", "Master - CMDTCSERVIÇOS LTDA")

    # RESUMO DO PLANO E LICENÇA
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="Plano Ativo",
            value="Enterprise Pro",
            delta="SaaS Unlimited",
        )
    with c2:
        st.metric(
            label="Valor Mensal",
            value="R$ 490,00",
            delta="Venc. Dia 10",
        )
    with c3:
        st.metric(
            label="Situação",
            value="🟢 Ativo",
            delta_color="normal",
        )
    with c4:
        st.metric(
            label="Forma Pagamento",
            value="Boleto / PIX",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ABAS DE GESTÃO FINANCEIRA E DE DADOS
    tab_faturas, tab_logo, tab_dados = st.tabs(
        ["💳 Faturas & Boletos", "🖼️ Logo da Empresa", "🏢 Dados Cadastrais"]
    )

    with tab_faturas:
        st.subheader("📄 Histórico de Faturas & Pagamentos")

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
            col_ref, col_venc, col_val, col_stat, col_btn = st.columns(
                [1, 1.2, 1, 1.2, 1.5]
            )
            col_ref.write(f"**Ref:** {fat['Ref']}")
            col_venc.write(fat["Vencimento"])
            col_val.write(fat["Valor"])

            if fat["Status"] == "Pago":
                col_stat.success("🟢 Pago")
            else:
                col_stat.warning("🟡 A Vencer")

            if col_btn.button(
                f"📄 {fat['Acao']}", key=f"btn_fat_{fat['Ref']}"
            ):
                st.info(f"Simulação: Gerando PDF referente à fatura {fat['Ref']}...")

    with tab_logo:
        st.subheader("🎨 Personalização de Logomarca")
        uploaded_logo = st.file_uploader(
            "Envie a logo da empresa (PNG ou JPG)",
            type=["png", "jpg", "jpeg"],
        )
        if uploaded_logo is not None:
            st.image(
                uploaded_logo,
                width=180,
                caption="Pré-visualização da Logo",
            )
            if st.button("💾 Salvar Logomarca"):
                st.success("Logo salva com sucesso!")

    with tab_dados:
        st.subheader("🏢 Dados Cadastrais da Empresa")
        st.text_input("Razão Social", value=empresa_nome)
        st.text_input("CNPJ", value="00.000.000/0001-00")
        st.text_input("E-mail Financeiro", value="financeiro@empresa.com.br")