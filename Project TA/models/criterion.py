# models/criterion.py
import time
import streamlit as st
from config import ICON_OPTIONS

def handle_criteria_update(new_criteria):
    """Update criteria and reset dependent data"""
    st.session_state.criteria = new_criteria
    st.session_state.criteria_weights = {}
    
    # Reset alternative scores with new criteria structure
    new_alternative_scores = {}
    for provider in st.session_state.providers:
        new_alternative_scores[provider["id"]] = {}
        for criterion in new_criteria:
            new_alternative_scores[provider["id"]][criterion["id"]] = 0
    
    st.session_state.alternative_scores = new_alternative_scores
    st.session_state.dematel_results = None
    st.session_state.direct_relation_matrix = np.zeros((len(new_criteria), len(new_criteria)))

def set_editing_criterion(criterion):
    """Set criterion for editing"""
    st.session_state.editing_criterion = criterion
    st.session_state.show_edit_criteria = True

def delete_criterion(criterion):
    """Delete a criterion with validation"""
    if len(st.session_state.criteria) <= 2:
        st.error("Minimum 2 criteria required for DEMATEL analysis!")
    else:
        st.session_state.criteria = [c for c in st.session_state.criteria if c["id"] != criterion["id"]]
        st.success(f"Criteria {criterion['name']} deleted successfully!")
        st.rerun()