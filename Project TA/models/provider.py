# models/provider.py
import time
import streamlit as st
from config import COLOR_OPTIONS, ICON_OPTIONS

def handle_providers_update(new_providers):
    """Update providers and reset dependent data"""
    st.session_state.providers = new_providers
    
    # Reset alternative scores when providers change
    new_alternative_scores = {}
    for provider in new_providers:
        new_alternative_scores[provider["id"]] = {}
        for criterion in st.session_state.criteria:
            new_alternative_scores[provider["id"]][criterion["id"]] = 0
    
    st.session_state.alternative_scores = new_alternative_scores
    st.session_state.dematel_results = None

def set_editing_provider(provider):
    """Set provider for editing"""
    st.session_state.editing_provider = provider
    st.session_state.show_edit_provider = True

def delete_provider(provider):
    """Delete a provider with validation"""
    if len(st.session_state.providers) <= 2:
        st.error("Minimum 2 providers required for DEMATEL analysis!")
    else:
        st.session_state.providers = [p for p in st.session_state.providers if p["id"] != provider["id"]]
        st.success(f"Provider {provider['name']} deleted successfully!")
        st.rerun()