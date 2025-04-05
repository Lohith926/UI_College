import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 32px;
            color: #FF6347;
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
        .select-label {
            font-size: 18px;
            color: #444;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Course fee data
course_fees = {
    "Computer Science and Engineering": "₹4,00,000",
    "Computer Science and Engineering with AI & ML": "₹4,00,000",
    "Computer Science and Engineering with Big Data Analytics": "₹3,60,000",
    "Computer Science and Engineering with Cyber Security": "₹3,60,000",
    "Computer Science and Engineering with Cloud Computing": "₹3,60,000",
    "Computer Science and Engineering with Internet of Things": "₹3,60,000",
    "Computer Science and Engineering with Software Product Engineering": "₹4,60,000",
    "Computer Science and Engineering with AI and Future Technologies": "₹4,60,000",
    "Electronics and Communication Engineering": "₹2,50,000",
    "Electronics and Communication Engineering with Advanced Communication Systems": "₹2,50,000",
    "Electronics and Communication Engineering with Signal Processing & AI/ML": "₹2,50,000",
    "Electronics and Communication Engineering with Embedded Systems & IoT": "₹2,50,000",
    "Electronics and Communication Engineering with VLSI Design": "₹2,50,000",
    "Mechanical Engineering": "₹2,50,000",
    "Mechanical Engineering with Additive Manufacturing": "₹2,50,000",
    "Mechanical Engineering with Automotive Engineering": "₹2,50,000",
    "Mechanical Engineering with Robotics and Automation": "₹2,50,000",
    "Electrical and Electronics Engineering": "₹2,50,000",
    "Electrical and Electronics Engineering with Renewable Energy": "₹2,50,000",
    "Civil Engineering": "₹2,50,000",
    "Civil Engineering with Computer Aided Structural Engineering": "₹2,50,000",
}

# Centered Title
st.markdown('<h1 class="title">🎓 SRM University-Chennai     Course Fee Structure - 2025</h1>', unsafe_allow_html=True)

# Dropdown for course selection
st.markdown('<p class="select-label">🔽 Select a Course:</p>', unsafe_allow_html=True)
selected_course = st.selectbox("", list(course_fees.keys()))

# Display the selected course fee inside a styled box
st.markdown(f'<div class="fee-box">💰 Fee for <b>{selected_course}</b>: {course_fees[selected_course]}</div>', unsafe_allow_html=True)
