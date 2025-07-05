# pages/overview.py
import streamlit as st

def show():
    """Application overview page"""
    st.title("WiFi Provider Decision Support System")
    st.write("Revolusioner dalam pemilihan provider WiFi dengan teknologi DEMATEL yang memberikan analisis mendalam dan rekomendasi terpercaya")
    
    # Stats cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Providers", len(st.session_state.providers))
    with col2:
        st.metric("Total Criteria", len(st.session_state.criteria))
    with col3:
        st.metric("Analysis Method", "DEMATEL")
    
    # Providers section
    st.subheader("Premium WiFi Providers")
    for provider in st.session_state.providers:
        st.write(f"{provider['icon']} {provider['name']}")
    
    # Criteria section
    st.subheader("Evaluation Criteria")
    for criterion in st.session_state.criteria:
        st.write(f"{criterion['icon']} {criterion['name']} ({criterion['type']})")
    
    # About DEMATEL
    st.subheader("About DEMATEL Technology")
    st.write("""
    DEMATEL is an advanced methodology that uses complex mathematical analysis to identify causal relationships between criteria, 
    providing deep insights that cannot be obtained from conventional methods.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Deep Influence Analysis**")
        st.write("Identifies the most influential criteria with high precision")
        
        st.write("**Automatic Weight Determination**")
        st.write("Calculates criteria weights based on influence level automatically")
    
    with col2:
        st.write("**Real-time Causal Analysis**")
        st.write("Understands cause-effect relationships between criteria in real-time")
        
        st.write("**Ultra Accurate Ranking**")
        st.write("Produces rankings based on comprehensive multi-dimensional analysis")