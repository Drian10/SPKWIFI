import streamlit as st
from streamlit_option_menu import option_menu
from config import initialize_session_state
from styles import apply_custom_styles
from pages import overview, criteria_input, alternatives, calculation, results

def main():
    """Main application function"""
    initialize_session_state()  # Pastikan ini dipanggil pertama!
    apply_custom_styles()
    
    # Sidebar navigation
    with st.sidebar:
        st.title("WiFi Provider DSS")
        
        menu_options = ["Overview", "Criteria", "Alternatives", "Calculation", "Results"]
        
        selected = option_menu(
            menu_title=None,
            options=menu_options,
            icons=["house", "gear", "wifi", "calculator", "trophy"],
            default_index=menu_options.index(st.session_state.active_tab) if st.session_state.active_tab in menu_options else 0,
        )
        
        st.session_state.active_tab = selected
    
    # Main content routing
    if st.session_state.active_tab == "Overview":
        overview.show()
    elif st.session_state.active_tab == "Criteria":
        criteria_input.show()
    elif st.session_state.active_tab == "Alternatives":
        alternatives.show()
    elif st.session_state.active_tab == "Calculation":
        calculation.show()
    elif st.session_state.active_tab == "Results":
        results.show()

if __name__ == "__main__":
    main()