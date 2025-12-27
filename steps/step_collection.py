import streamlit as st
from utils.auth import update_activity

def step_collection():
    st.header("📥 Coleta do Contexto Jurídico")

    with st.form("context_form"):
        processo = st.text_area("Resumo do Processo")
        pedidos = st.text_area("Pedidos")
        provas = st.text_area("Provas")
        submitted = st.form_submit_button("Analisar")

    if submitted:
        update_activity()
        return {
            "processo": processo,
            "pedidos": pedidos,
            "provas": provas
        }

    return None

