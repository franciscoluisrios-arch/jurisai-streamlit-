import sys
import os

# Garante que a raiz do projeto esteja no path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st

from services.gemini_service import GeminiService
from utils.auth import check_session, login, logout, update_activity
from steps.step_collection import step_collection
from steps.step_analysis import step_analysis
from steps.step_draft import step_draft


st.set_page_config(page_title="JurisAI", layout="wide")

check_session()

if not st.session_state.authenticated:
    st.title("🔐 JurisAI – Acesso Restrito")
    pwd = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if login(pwd):
            st.success("Acesso autorizado")
            st.rerun()
        else:
            st.error("Senha incorreta")
    st.stop()

update_activity()

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.context = None
    st.session_state.diagnosis = ""
    st.session_state.draft = ""

st.sidebar.button("Logout", on_click=logout)

gemini = GeminiService()

if st.session_state.step == 1:
    context = step_collection()
    if context:
        st.session_state.context = context
        st.session_state.diagnosis = gemini.generate_analysis(context)
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    if step_analysis(st.session_state.diagnosis):
        st.session_state.draft = gemini.generate_draft(
            st.session_state.context,
            st.session_state.diagnosis
        )
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    step_draft(st.session_state.draft)



