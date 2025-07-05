# pages/alternatives.py
import streamlit as st

def show():
    """Input for alternative evaluation with enhanced sample data"""
    st.title("Evaluasi Provider WiFi")
    
    if not st.session_state.providers or not st.session_state.criteria:
        st.warning("Silakan tambahkan provider dan kriteria terlebih dahulu")
        return
    
    st.subheader("Matriks Evaluasi Provider")
    
    # Enhanced sample data options with Indonesian names and descriptions
    sample_data_options = {
        "scenario1": {
            "name": "Pengguna Hemat Budget",
            "description": "Fokus pada harga murah dengan performa cukup",
            "data": {
                "indihome": {"installation_cost": 150000, "monthly_cost": 350000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "iconet": {"installation_cost": 100000, "monthly_cost": 300000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
                "firstmedia": {"installation_cost": 200000, "monthly_cost": 400000, "customer_type": 3, "package_type": 3, "speed": 4, "signal_stability": 3},
                "myrepublic": {"installation_cost": 120000, "monthly_cost": 280000, "customer_type": 2, "package_type": 2, "speed": 3, "signal_stability": 2},
                "biznet": {"installation_cost": 250000, "monthly_cost": 450000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "megavision": {"installation_cost": 180000, "monthly_cost": 320000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
            }
        },
        "scenario2": {
            "name": "Pengguna Butuh Performa Tinggi",
            "description": "Prioritaskan kecepatan dan stabilitas jaringan",
            "data": {
                "indihome": {"installation_cost": 180000, "monthly_cost": 450000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "iconet": {"installation_cost": 150000, "monthly_cost": 400000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "firstmedia": {"installation_cost": 220000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 5, "signal_stability": 4},
                "myrepublic": {"installation_cost": 200000, "monthly_cost": 420000, "customer_type": 3, "package_type": 3, "speed": 4, "signal_stability": 3},
                "biznet": {"installation_cost": 250000, "monthly_cost": 550000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "megavision": {"installation_cost": 230000, "monthly_cost": 400000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
            }
        },
        "scenario3": {
            "name": "Paket Usaha Kecil",
            "description": "Solusi seimbang untuk usaha kecil",
            "data": {
                "indihome": {"installation_cost": 200000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "iconet": {"installation_cost": 180000, "monthly_cost": 450000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "firstmedia": {"installation_cost": 250000, "monthly_cost": 600000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "myrepublic": {"installation_cost": 220000, "monthly_cost": 480000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "biznet": {"installation_cost": 240000, "monthly_cost": 650000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "megavision": {"installation_cost": 210000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
            }
        },
        "scenario4": {
            "name": "Paket Keluarga Dasar",
            "description": "Paket dasar untuk penggunaan keluarga",
            "data": {
                "indihome": {"installation_cost": 120000, "monthly_cost": 250000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
                "iconet": {"installation_cost": 100000, "monthly_cost": 200000, "customer_type": 1, "package_type": 1, "speed": 1, "signal_stability": 1},
                "firstmedia": {"installation_cost": 150000, "monthly_cost": 300000, "customer_type": 2, "package_type": 2, "speed": 3, "signal_stability": 2},
                "myrepublic": {"installation_cost": 110000, "monthly_cost": 220000, "customer_type": 1, "package_type": 1, "speed": 2, "signal_stability": 1},
                "biznet": {"installation_cost": 200000, "monthly_cost": 350000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "megavision": {"installation_cost": 130000, "monthly_cost": 240000, "customer_type": 1, "package_type": 1, "speed": 1, "signal_stability": 1},
            }
        },
        "scenario5": {
            "name": "Paket Gamer/Streamer",
            "description": "Performa tinggi untuk gaming dan streaming",
            "data": {
                "indihome": {"installation_cost": 220000, "monthly_cost": 550000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "iconet": {"installation_cost": 200000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "firstmedia": {"installation_cost": 250000, "monthly_cost": 600000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "myrepublic": {"installation_cost": 230000, "monthly_cost": 550000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "biznet": {"installation_cost": 240000, "monthly_cost": 700000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "megavision": {"installation_cost": 210000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
            }
        },
        "scenario6": {
            "name": "Solusi Daerah Pedesaan",
            "description": "Pilihan dengan jangkauan terbaik di daerah",
            "data": {
                "indihome": {"installation_cost": 150000, "monthly_cost": 350000, "customer_type": 3, "package_type": 3, "speed": 2, "signal_stability": 4},
                "iconet": {"installation_cost": 120000, "monthly_cost": 300000, "customer_type": 2, "package_type": 2, "speed": 1, "signal_stability": 3},
                "firstmedia": {"installation_cost": 200000, "monthly_cost": 400000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 4},
                "myrepublic": {"installation_cost": 180000, "monthly_cost": 320000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 3},
                "biznet": {"installation_cost": 250000, "monthly_cost": 450000, "customer_type": 4, "package_type": 4, "speed": 3, "signal_stability": 5},
                "megavision": {"installation_cost": 160000, "monthly_cost": 280000, "customer_type": 2, "package_type": 2, "speed": 1, "signal_stability": 3},
            }
        },
        "scenario7": {
            "name": "Paket Premium Perkotaan",
            "description": "Paket premium untuk pengguna di kota",
            "data": {
                "indihome": {"installation_cost": 200000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "iconet": {"installation_cost": 180000, "monthly_cost": 450000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "firstmedia": {"installation_cost": 250000, "monthly_cost": 600000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "myrepublic": {"installation_cost": 220000, "monthly_cost": 480000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "biznet": {"installation_cost": 240000, "monthly_cost": 650000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "megavision": {"installation_cost": 210000, "monthly_cost": 500000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
            }
        },
        "scenario8": {
            "name": "Paket Pelajar",
            "description": "Pilihan terjangkau untuk pelajar",
            "data": {
                "indihome": {"installation_cost": 120000, "monthly_cost": 280000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
                "iconet": {"installation_cost": 100000, "monthly_cost": 220000, "customer_type": 1, "package_type": 1, "speed": 1, "signal_stability": 1},
                "firstmedia": {"installation_cost": 150000, "monthly_cost": 320000, "customer_type": 2, "package_type": 2, "speed": 3, "signal_stability": 2},
                "myrepublic": {"installation_cost": 110000, "monthly_cost": 250000, "customer_type": 1, "package_type": 1, "speed": 2, "signal_stability": 1},
                "biznet": {"installation_cost": 200000, "monthly_cost": 350000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "megavision": {"installation_cost": 130000, "monthly_cost": 240000, "customer_type": 1, "package_type": 1, "speed": 1, "signal_stability": 1},
            }
        },
        "scenario9": {
            "name": "Solusi Perusahaan",
            "description": "Paket kelas enterprise untuk bisnis",
            "data": {
                "indihome": {"installation_cost": 250000, "monthly_cost": 800000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "iconet": {"installation_cost": 240000, "monthly_cost": 750000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "firstmedia": {"installation_cost": 250000, "monthly_cost": 900000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "myrepublic": {"installation_cost": 230000, "monthly_cost": 800000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "biznet": {"installation_cost": 250000, "monthly_cost": 1000000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
                "megavision": {"installation_cost": 220000, "monthly_cost": 750000, "customer_type": 5, "package_type": 5, "speed": 5, "signal_stability": 5},
            }
        },
        "scenario10": {
            "name": "Paket Keluarga",
            "description": "Solusi seimbang untuk keluarga",
            "data": {
                "indihome": {"installation_cost": 180000, "monthly_cost": 350000, "customer_type": 3, "package_type": 3, "speed": 3, "signal_stability": 3},
                "iconet": {"installation_cost": 150000, "monthly_cost": 300000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
                "firstmedia": {"installation_cost": 200000, "monthly_cost": 400000, "customer_type": 3, "package_type": 3, "speed": 4, "signal_stability": 3},
                "myrepublic": {"installation_cost": 160000, "monthly_cost": 320000, "customer_type": 2, "package_type": 2, "speed": 3, "signal_stability": 2},
                "biznet": {"installation_cost": 250000, "monthly_cost": 450000, "customer_type": 4, "package_type": 4, "speed": 4, "signal_stability": 4},
                "megavision": {"installation_cost": 170000, "monthly_cost": 330000, "customer_type": 2, "package_type": 2, "speed": 2, "signal_stability": 2},
            }
        }
    }
    
    # Display sample data selector with descriptions
    selected_scenario = st.selectbox(
        "Pilih Skenario Contoh", 
        list(sample_data_options.keys()), 
        format_func=lambda x: sample_data_options[x]["name"],
        help="Pilih skenario yang sudah disiapkan untuk mengisi data otomatis"
    )
    
    # Show scenario description
    st.caption(f"Deskripsi: {sample_data_options[selected_scenario]['description']}")
    
    if st.button("Muat Data Contoh"):
        st.session_state.alternative_scores = sample_data_options[selected_scenario]["data"]
        st.success(f"Berhasil memuat data skenario: {sample_data_options[selected_scenario]['name']}!")
        st.rerun()
    
    # Initialize scores if not exists
    if "alternative_scores" not in st.session_state:
        st.session_state.alternative_scores = {}
        for provider in st.session_state.providers:
            st.session_state.alternative_scores[provider["id"]] = {}
            for criterion in st.session_state.criteria:
                st.session_state.alternative_scores[provider["id"]][criterion["id"]] = 0
    
    # Input matrix
    for provider in st.session_state.providers:
        st.subheader(provider["name"])
        cols = st.columns(len(st.session_state.criteria))
        
        for i, criterion in enumerate(st.session_state.criteria):
            with cols[i]:
                current_value = st.session_state.alternative_scores.get(provider["id"], {}).get(criterion["id"], 0)
                
                if criterion["type"] == "benefit":
                    new_value = st.number_input(
                        f"{criterion['name']} (1-5)",
                        min_value=1,
                        max_value=5,
                        value=int(current_value) if current_value else 1,
                        key=f"score_{provider['id']}_{criterion['id']}_{i}",
                        help="1 = sangat buruk, 5 = sangat bagus"
                    )
                else:
                    new_value = st.number_input(
                        f"{criterion['name']} (Rp)",
                        min_value=0,
                        value=int(current_value) if current_value else 0,
                        step=1000,
                        key=f"score_{provider['id']}_{criterion['id']}_{i}",
                        help="Biaya dalam Rupiah"
                    )
                
                if provider["id"] not in st.session_state.alternative_scores:
                    st.session_state.alternative_scores[provider["id"]] = {}
                st.session_state.alternative_scores[provider["id"]][criterion["id"]] = new_value
    
    if st.button("Simpan Nilai"):
        st.success("Nilai berhasil disimpan!")