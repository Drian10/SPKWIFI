# pages/calculation.py
import time
import streamlit as st

def show():
    """Perform DEMATEL calculation"""
    st.title("DEMATEL Calculation")
    
    if not st.session_state.criteria_weights or not st.session_state.alternative_scores:
        st.warning("Please complete criteria weights and alternative scores first")
        return
    
    if st.button("Start Calculation"):
        with st.spinner("Calculating..."):
            time.sleep(2)  # Simulate calculation
            
            # Normalize scores
            normalized_scores = {}
            for criterion in st.session_state.criteria:
                values = [scores.get(criterion["id"], 0) for scores in st.session_state.alternative_scores.values()]
                max_val = max(values)
                min_val = min(values)
                
                for provider_id, scores in st.session_state.alternative_scores.items():
                    if provider_id not in normalized_scores:
                        normalized_scores[provider_id] = {}
                    
                    original_value = scores.get(criterion["id"], 0)
                    if criterion["type"] == "benefit":
                        normalized_scores[provider_id][criterion["id"]] = (original_value - min_val) / (max_val - min_val) if max_val != min_val else 0.5
                    else:
                        normalized_scores[provider_id][criterion["id"]] = (max_val - original_value) / (max_val - min_val) if max_val != min_val else 0.5
            
            # Apply weights
            weighted_scores = {}
            for provider_id, scores in normalized_scores.items():
                weighted_scores[provider_id] = {}
                for criterion in st.session_state.criteria:
                    weight = st.session_state.criteria_weights.get(criterion["id"], 1/len(st.session_state.criteria))
                    weighted_scores[provider_id][criterion["id"]] = scores[criterion["id"]] * weight
            
            # Calculate final scores
            final_scores = {}
            for provider_id, scores in weighted_scores.items():
                final_scores[provider_id] = sum(scores.values())
            
            # Rank providers
            ranked_providers = sorted(
                [(pid, score) for pid, score in final_scores.items()],
                key=lambda x: x[1],
                reverse=True
            )
            
            st.session_state.dematel_results = {
                "normalized_scores": normalized_scores,
                "weighted_scores": weighted_scores,
                "final_scores": final_scores,
                "ranked_providers": [{"providerId": pid, "score": score, "rank": i+1} for i, (pid, score) in enumerate(ranked_providers)]
            }
            
            st.success("Calculation completed successfully!")
    
    if st.session_state.dematel_results:
        st.subheader("Calculation Steps")
        steps = [
            {"title": "Step 1: Data Normalization", "description": "Convert raw values to normalized values (0-1)"},
            {"title": "Step 2: DEMATEL Weight Application", "description": "Multiply normalized values by criteria weights"},
            {"title": "Step 3: Final Score Calculation", "description": "Sum all weighted values for each alternative"},
            {"title": "Step 4: Ranking", "description": "Sort alternatives by final score"},
        ]
        
        for step in steps:
            with st.expander(step["title"]):
                st.write(step["description"])
        
        st.subheader("Final Results")
        for provider in st.session_state.dematel_results["ranked_providers"]:
            provider_name = next((p["name"] for p in st.session_state.providers if p["id"] == provider["providerId"]), provider["providerId"])
            st.write(f"#{provider['rank']} {provider_name}: {provider['score']:.4f}")