import streamlit as st

# Hindustan University Fee Structure Data (Extracted from Image)
fee_structure = {
    "Aeronautical Engineering": "₹3,69,500",
    "Aerospace Engineering": "₹3,69,500",
    "Computer Science Engineering": "₹2,72,000",
    "Artificial Intelligence & Data Science": "₹2,72,000",
    "CSE (AI & ML)": "₹3,26,000",
    "CSE (Cyber Security)": "₹3,26,000",
    "CSE (Blockchain Technology)": "₹3,26,000",
    "CSE (Internet of Things)": "₹3,26,000",
    "CSE (Cloud Computing)": "₹3,26,000",
    "Information Technology": "₹2,72,000",
    "Electronics & Communication Engineering": "₹2,23,000",
    "Automobile Engineering (Electric Mobility)": "₹2,85,500",
    "Automobile Engineering": "₹2,23,000",
    "Bio-Technology": "₹2,23,000",
    "Bio-Medical Engineering": "₹2,23,000",
    "Robotics and Artificial Intelligence": "₹2,23,000",
    "Semiconductor Technology": "₹2,23,000",
    "Mechanical Engineering": "₹2,23,000",
    "Mechatronics Engineering": "₹2,23,000",
    "Electrical & Electronics Engineering": "₹2,23,000",
}

# Custom Styling for Better UI
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
st.markdown('<h1 class="title">🎓 Hindustan University - Fee Structure (2025-26)</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">School of Engineering and Technology</h2>', unsafe_allow_html=True)

# Dropdown for course selection
selected_course = st.selectbox("Select a Program", list(fee_structure.keys()))

# Display the selected course fee
st.markdown(f'<div class="fee-box">💰 Fee for {selected_course}: {fee_structure[selected_course]}</div>', unsafe_allow_html=True)
