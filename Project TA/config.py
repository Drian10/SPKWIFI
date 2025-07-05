import numpy as np
import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    defaults = {
        'providers': [
        {"id": "indihome", "name": "Indihome", "color": "bg-red-500", "icon": "🏠"},
        {"id": "iconet", "name": "Iconet", "color": "bg-blue-500", "icon": "🌐"},
        {"id": "firstmedia", "name": "Firstmedia (Fast-Net)", "color": "bg-green-500", "icon": "⚡"},
        {"id": "myrepublic", "name": "MyRepublic", "color": "bg-purple-500", "icon": "🚀"},
        {"id": "biznet", "name": "Biznet", "color": "bg-orange-500", "icon": "💼"},
        {"id": "megavision", "name": "Mega Vision", "color": "bg-pink-500", "icon": "👁️"},
        ],
        'criteria': [
        {"id": "installation_cost", "name": "Biaya Pemasangan", "type": "cost", "icon": "💰", "color": "text-red-500"},
        {"id": "monthly_cost", "name": "Biaya Bulanan", "type": "cost", "icon": "📅", "color": "text-red-500"},
        {"id": "customer_type", "name": "Jenis Pelanggan", "type": "benefit", "icon": "👥", "color": "text-green-500"},
        {"id": "package_type", "name": "Jenis Paket", "type": "benefit", "icon": "📦", "color": "text-green-500"},
        {"id": "speed", "name": "Kecepatan", "type": "benefit", "icon": "🚀", "color": "text-green-500"},
        {"id": "signal_stability", "name": "Kestabilan Sinyal", "type": "benefit", "icon": "📶", "color": "text-green-500"},
        ],
        'active_tab': "Overview",
        'dematel_results': None,
        'criteria_weights': {},
        'alternative_scores': {},
        'direct_relation_matrix': np.zeros((6, 6))  # Default size
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

COLOR_OPTIONS = [
    {"label": "Red", "value": "bg-red-500"},
    {"label": "Blue", "value": "bg-blue-500"},
    {"label": "Green", "value": "bg-green-500"},
    {"label": "Yellow", "value": "bg-yellow-500"},
    {"label": "Purple", "value": "bg-purple-500"},
    {"label": "Pink", "value": "bg-pink-500"},
    {"label": "Indigo", "value": "bg-indigo-500"},
    {"label": "Orange", "value": "bg-orange-500"},
]

ICON_OPTIONS = ["🏠", "🌐", "⚡", "🚀", "💼", "👁️", "📶", "💰", "📅", "👥", "📦"]