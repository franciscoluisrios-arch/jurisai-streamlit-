import streamlit as st
import time

INACTIVITY_TIMEOUT = 15 * 60  # 15 minutos

def check_session():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.last_activity = time.time()

    if st.session_state.authenticated:
        if time.time() - st.session_state.last_activity > INACTIVITY_TIMEOUT:
            logout()

def update_activity():
    st.session_state.last_activity = time.time()

def login(password):
    if password == "admin123":  # troque depois
        st.session_state.authenticated = True
        update_activity()
        return True
    return False

def logout():
    st.session_state.clear()
    st.rerun()
