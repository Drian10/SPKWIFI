# pages/results.py
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import streamlit as st

def show():
    """Display DEMATEL results"""
    st.title("Analysis Results")
    
    if not st.session_state.dematel_results:
        st.warning("No calculation results available yet")
        return
    
    st.subheader("WiFi Provider Ranking")
    for provider in st.session_state.dematel_results["ranked_providers"]:
        provider_name = next((p["name"] for p in st.session_state.providers if p["id"] == provider["providerId"]), provider["providerId"])
        col1, col2 = st.columns(2)
        col1.write(f"#{provider['rank']} {provider_name}")
        col2.write(f"Score: {provider['score']:.4f}")
    

    
    st.subheader("Recommendation")
    top_provider = st.session_state.dematel_results["ranked_providers"][0]
    top_name = next((p["name"] for p in st.session_state.providers if p["id"] == top_provider["providerId"]), top_provider["providerId"])
    st.success(f"Top Provider: {top_name} with score {top_provider['score']:.4f}")
    
    if st.button("Export Results as Image"):
        # Create a figure for the visualization
        import matplotlib.pyplot as plt
        
        # Prepare data for visualization
        providers = []
        scores = []
        for provider in st.session_state.dematel_results["ranked_providers"]:
            provider_name = next((p["name"] for p in st.session_state.providers if p["id"] == provider["providerId"]), provider["providerId"])
            providers.append(provider_name)
            scores.append(provider['score'])
        
        # Create bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(providers[::-1], scores[::-1], color='purple')
        ax.set_xlabel('Score')
        ax.set_title('WiFi Provider Ranking')
        
        # Add score labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 0.01, bar.get_y() + bar.get_height()/2,
                   f'{width:.4f}',
                   ha='left', va='center')
        
        plt.tight_layout()
        
        # Save the figure to a temporary file
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
            fig.savefig(tmpfile.name, format='png', dpi=300)
            plt.close(fig)
            
            # Create download button
            with open(tmpfile.name, "rb") as file:
                btn = st.download_button(
                    label="Download PNG",
                    data=file,
                    file_name="wifi_provider_ranking.png",
                    mime="image/png"
                )