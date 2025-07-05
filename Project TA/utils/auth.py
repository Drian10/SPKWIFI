# utils/auth.py
from datetime import datetime
import streamlit as st

def handle_admin_login(username, password):
    """Handle admin login"""
    if username == "admin" and password == "admin123":
        st.session_state.admin_user = {
            "id": "admin",
            "name": "Super Administrator",
            "role": "Super Admin",
            "loginTime": datetime.now().isoformat()
        }
        st.session_state.show_admin_login = False
        st.rerun()
    else:
        st.error("Username atau password salah!")

def handle_admin_logout():
    """Handle admin logout"""
    st.session_state.admin_user = None
    st.session_state.active_tab = "Overview"
    st.rerun()

def admin_login():
    """Admin login page"""
    st.title("Super Admin Login")
    
    with st.form("login_form"):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.form_submit_button("Login as Super Admin"):
            handle_admin_login(username, password)