import streamlit as st

# Fee structure data
fee_data = {
    "BCA + Artificial Intelligence & Machine Learning": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BCA + Cloud Computing & Ethical Hacking": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BCA Global (With International Study Tour)": [45000, 150000, 45000, 95000, 45000, 45000, 20000, 445000],
    "BCA With IBM Global Certification in AI (With International Study Tour)": [45000, 150000, 60000, 95000, 60000, 60000, 25000, 495000],
    "BBA Aviation": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BBA Aviation + Logistics & Supply Chain Management": [45000, 150000, 45000, 45000, 45000, 45000, 20000, 395000],
    "BBA Aviation + Logistics & Supply Chain Management Global (With International Study Tour)": [45000, 150000, 45000, 95000, 45000, 45000, 20000, 445000],
    "BBA + Logistics & Supply Chain Management": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BBA + Digital & Social Media Marketing": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BBA + Entrepreneurship": [45000, 150000, 40000, 40000, 40000, 40000, 20000, 375000],
    "BBA Global (With International Study Tour)": [45000, 150000, 45000, 95000, 45000, 45000, 20000, 445000],
    "BBA With IBM Global Certification in Business Analyst (With International Study Tour)": [45000, 150000, 60000, 95000, 60000, 60000, 25000, 495000],
    "B.COM + SAP": [45000, 75000, 35000, 35000, 35000, 35000, 35000, 295000],
    "B.COM + Accounting & Taxation": [45000, 75000, 35000, 35000, 35000, 35000, 35000, 295000],
    "B.COM + Tally with GST": [45000, 75000, 35000, 35000, 35000, 35000, 35000, 295000],
}

# Additional Fees
additional_fees = {
    "Uniform Fee (2 Sets + 1 Blazer)": 6900,
    "University Registration Fee": "As per university guidelines",
    "Examination & Convocation Fee": "Not included in tuition fee",
    "Refund Policy": "Fees once paid are neither refundable nor transferable"
}

# Streamlit App
st.set_page_config(page_title="IZEE Business School - Fee Structure", page_icon="🎓", layout="centered")
st.title("🎓 IZEE Business School")
st.subheader("Select Your Course to View Fees")

# Course selection dropdown
selected_course = st.selectbox("Select Your Course", list(fee_data.keys()))

# Display fee structure based on selection
if st.button("Get Fee Details"):
    fees = fee_data[selected_course]
    st.success(f"**Fee Structure for {selected_course}:**")
    st.write(f"📌 **Admission Fee:** ₹{fees[0]:,}")
    st.write(f"📌 **1st Semester:** ₹{fees[1]:,}")
    st.write(f"📌 **2nd Semester:** ₹{fees[2]:,}")
    st.write(f"📌 **3rd Semester:** ₹{fees[3]:,}")
    st.write(f"📌 **4th Semester:** ₹{fees[4]:,}")
    st.write(f"📌 **5th Semester:** ₹{fees[5]:,}")
    st.write(f"📌 **6th Semester:** ₹{fees[6]:,}")
    st.write(f"💰 **Total Fees:** ₹{fees[7]:,}")

# Additional Fees
st.subheader("📌 Additional Fees & Important Notes")
for fee_name, amount in additional_fees.items():
    st.write(f"🔹 **{fee_name}:** {amount}")

# Footer
st.write("")
