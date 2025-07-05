# utils/helpers.py
import time

def generate_id(name, existing_ids):
    """Generate unique ID from name"""
    base_id = name.lower().replace(" ", "_")[:15]
    if not base_id:
        return f"item_{int(time.time())}"
    
    final_id = base_id
    counter = 1
    while final_id in existing_ids:
        final_id = f"{base_id}_{counter}"
        counter += 1
    
    return final_id