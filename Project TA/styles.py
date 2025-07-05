# styles.py
import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles"""
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #1e293b, #6b21a8, #1e293b);
        color: white;
    }
    .stButton>button {
        background: linear-gradient(to right, #4f46e5, #7c3aed);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #4338ca, #6d28d9);
    }
    .stSelectbox>div>div>select {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    .stNumberInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)