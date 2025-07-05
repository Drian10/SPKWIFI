# pages/criteria_input.py
import time
import numpy as np
import streamlit as st

def show():
    """Input for DEMATEL criteria analysis"""
    st.title("DEMATEL Criteria Analysis")
    
    if not st.session_state.criteria:
        st.warning("Please add criteria first")
        return
    
    st.subheader("Direct Relation Matrix Between Criteria")
    st.write("Determine the influence level between criteria using the following scale:")
    st.write("0 - No influence, 1 - Low influence, 2 - Medium influence, 3 - High influence, 4 - Very high influence")
    
    # Display matrix input
    cols = st.columns(len(st.session_state.criteria) + 1)
    with cols[0]:
        st.write("Influencing →")
    
    for i, crit in enumerate(st.session_state.criteria):
        with cols[i+1]:
            st.write(crit["name"])
            st.write(f"({crit['type']})")
    
    for i, crit1 in enumerate(st.session_state.criteria):
        cols = st.columns(len(st.session_state.criteria) + 1)
        with cols[0]:
            st.write(crit1["name"])
        
        for j, crit2 in enumerate(st.session_state.criteria):
            with cols[j+1]:
                if i == j:
                    st.write("—")
                else:
                    st.session_state.direct_relation_matrix[i][j] = st.number_input(
                        f"{crit1['name']} → {crit2['name']}",
                        min_value=0,
                        max_value=4,
                        value=int(st.session_state.direct_relation_matrix[i][j]),
                        key=f"matrix_{i}_{j}"
                    )
    
    if st.button("Calculate DEMATEL Weights"):
        with st.spinner("Calculating weights..."):
            time.sleep(1)  # Simulate calculation
            
            # DEMATEL calculation
            n = len(st.session_state.criteria)
            matrix = st.session_state.direct_relation_matrix
            
            # Normalize matrix
            max_sum = max([sum(row) for row in matrix])
            normalized_matrix = matrix / max_sum if max_sum > 0 else np.zeros((n, n))
            
            # Simplified calculation for demonstration
            row_sums = [sum(row) for row in normalized_matrix]
            col_sums = [sum(col) for col in zip(*normalized_matrix)]
            
            prominence = [r + c for r, c in zip(row_sums, col_sums)]
            relation = [r - c for r, c in zip(row_sums, col_sums)]
            
            # Normalize weights
            total_prominence = sum(prominence)
            new_weights = {}
            
            for i, criterion in enumerate(st.session_state.criteria):
                new_weights[criterion["id"]] = prominence[i] / total_prominence if total_prominence > 0 else 1 / n
            
            st.session_state.criteria_weights = new_weights
            st.success("Weights calculated successfully!")
    
    if st.button("Reset Matrix"):
        size = len(st.session_state.criteria)
        st.session_state.direct_relation_matrix = np.zeros((size, size))
        st.rerun()
    
    # Display results
    if st.session_state.criteria_weights:
        st.subheader("Criteria Weights (DEMATEL Results)")
        for criterion in st.session_state.criteria:
            weight = st.session_state.criteria_weights.get(criterion["id"], 0)
            st.write(f"{criterion['name']}: {weight*100:.2f}%")
            st.progress(weight)