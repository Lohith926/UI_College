import streamlit as st

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
        .fee-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f4f4f4;
            text-align: center;
            font-size: 22px;
            color: #2E8B57;
            font-weight: bold;
        }
        .table-container {
            text-align: center;
        }
        .highlight {
            color: #d9534f;
            font-size: 22px;
            font-weight: bold;
        }
        .macbook-offer {
            background-color: #FFD700;
            padding: 10px;
            border-radius: 8px;
            font-size: 20px;
            text-align: center;
            font-weight: bold;
            color: #000;
        }
        .placements {
            background-color: #DFF0D8;
            padding: 10px;
            border-radius: 8px;
            font-size: 18px;
            text-align: center;
            font-weight: bold;
            color: #008000;
        }
        .collaborations {
            background-color: #E6E6FA;
            padding: 10px;
            border-radius: 8px;
            font-size: 18px;
            text-align: center;
            font-weight: bold;
            color: #4B0082;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display University Name & Title
st.markdown('<h1 class="title">🎓 NIMS University - Global B.Tech CS Fee Structure (2025)</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">With US Degree</h2>', unsafe_allow_html=True)

# Fee Structure Table Data
fee_data = {
    "1st Year": ["₹2,27,500", "₹1,60,000"],
    "2nd Year": ["₹2,27,500", "₹1,60,000"],
    "3rd Year": ["₹2,27,500", "₹1,60,000"],
    "4th Year": ["₹2,27,500", "₹1,60,000"],
    "Total (4 Years)": ["₹9,10,000", "₹6,40,000"],
    "Grand Total": ["₹15,50,000"]
}

# Display Fee Structure Table
st.markdown('<div class="table-container">', unsafe_allow_html=True)
st.table({
    "Year": ["1st Year", "2nd Year", "3rd Year", "4th Year", "Total (4 Years)", "Grand Total"],
    "Tuition Fees": ["₹2,27,500", "₹2,27,500", "₹2,27,500", "₹2,27,500", "₹9,10,000", "₹15,50,000"],
    "Hostel Fees": ["₹1,60,000", "₹1,60,000", "₹1,60,000", "₹1,60,000", "₹6,40,000", "-"]
})
st.markdown('</div>', unsafe_allow_html=True)

# Free MacBook Offer
st.markdown('<div class="macbook-offer">🎁 Free MacBook for Students Enrolled in this Course!</div>', unsafe_allow_html=True)

# Placements Information
st.markdown('<div class="placements">🚀 45,000+ Placements Offered</div>', unsafe_allow_html=True)

# International Collaborations
st.markdown(
    '<div class="collaborations">🌍 International Study Opportunities: USA, UK, Australia, Europe, Philippines, Japan, Russia, Mexico, China, Uganda, Thailand</div>',
    unsafe_allow_html=True
)
