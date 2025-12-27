import streamlit as st

def step_draft(draft):
    st.header("📝 Minuta Judicial")

    if draft:
        st.text_area("Texto Final", draft, height=400)

    if st.button("Nova Análise"):
        st.session_state.step = 1
        st.session_state.context = None
        st.session_state.diagnosis = ""
        st.session_state.draft = ""
        st.rerun()
