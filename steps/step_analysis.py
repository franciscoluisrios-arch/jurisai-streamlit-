import streamlit as st

def step_analysis(diagnosis):
    st.header("🔎 Análise Jurídica")

    if not diagnosis:
        st.info("Gerando análise...")
    else:
        st.markdown(diagnosis)

    return st.button("Prosseguir para Minuta")
