import streamlit as st

# IES University Fee Structure Data (Extracted from Image)
fee_structure = {
    "1st Semester (Including Hostel)": "₹1,73,500.00",
    "2nd Semester": "₹36,000.00",
    "3rd Semester": "₹68,500.00",
    "4th Semester": "₹68,500.00",
    "5th Semester": "₹68,500.00",
    "6th Semester": "₹68,500.00",
    "7th Semester": "₹68,500.00",
    "8th Semester": "₹68,500.00",
    "Total Package (4 Years Including Hostel, Food & Accommodation)": "₹6.28 Lakh"
}

# Custom Styling for Enhanced UI
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 32px;
            color: #B22222;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #333;
            font-weight: bold;
        }
        .dropdown {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .fee-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f4f4f4;
            text-align: center;
            font-size: 22px;
            color: #2E8B57;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display University Name & Title
st.markdown('<h1 class="title">🏫 IES University - Fee Structure (2025-26)</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">B.Tech Program - Fees per Semester</h2>', unsafe_allow_html=True)

# Dropdown for semester selection
selected_semester = st.selectbox("Select a Semester", list(fee_structure.keys()))

# Display the selected semester fee
st.markdown(f'<div class="fee-box">💰 Fee for {selected_semester}: {fee_structure[selected_semester]}</div>', unsafe_allow_html=True)
