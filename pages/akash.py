import streamlit as st

# Fee structure data
fee_data = {
    "BE - Computer Science & Engineering": [275000, 150000, 150000, 150000, 725000],
    "BE - Computer Science Engineering (AI & ML)": [275000, 150000, 150000, 150000, 725000],
    "BE - Artificial Intelligence & Data Science": [275000, 150000, 150000, 150000, 725000],
    "BE - Computer Science Engineering (Cyber Security)": [275000, 150000, 150000, 150000, 725000],
    "BE - Computer Science Engineering (Data Science)": [275000, 150000, 150000, 150000, 725000],
    "BE - Information Science & Engineering": [225000, 100000, 100000, 100000, 525000],
    "BE - Electronics & Communication Engineering": [250000, 100000, 100000, 100000, 600000],
    "BE - Mechanical Engineering": [175000, 50000, 50000, 50000, 325000],
}

# Fee structure for lateral entry students
fee_data_lateral = {
    "BE - Computer Science & Engineering": [190000, 100000, 100000, 390000],
    "BE - Computer Science Engineering (AI & ML)": [190000, 100000, 100000, 390000],
    "BE - Artificial Intelligence & Data Science": [190000, 75000, 75000, 340000],
    "BE - Computer Science Engineering (Cyber Security)": [175000, 75000, 75000, 325000],
    "BE - Computer Science Engineering (Data Science)": [150000, 75000, 75000, 300000],
    "BE - Information Science & Engineering": [150000, 75000, 75000, 300000],
    "BE - Electronics & Communication Engineering": [175000, 75000, 75000, 325000],
}

# Additional Fees
additional_fees = {
    "Application Fee": 1000,
    "University Registration Fee": 14000,
    "Books & Uniform Fee": 14000,
    "Soft Skills Training (per year)": 7500,
}

# Hostel Fees
hostel_fees = {
    "4 Sharing Veg": 110000,
    "4 Sharing Non-Veg": 120000,
    "3 Sharing Veg": 135000,
    "3 Sharing Non-Veg": 150000,
}

# Streamlit App
st.set_page_config(page_title="Akash Institutions - Fee Structure", page_icon="🎓", layout="centered")
st.title("🎓 Akash Group of Institutions")
st.subheader("Select Your Course to View Fees")

# Choose Regular or Lateral Entry
entry_type = st.radio("Choose Admission Type:", ["Regular", "Lateral Entry"])

# Course selection dropdown
if entry_type == "Regular":
    course_list = list(fee_data.keys())
else:
    course_list = list(fee_data_lateral.keys())

selected_course = st.selectbox("Select Your Course", course_list)

# Display fee structure based on selection
if st.button("Get Fee Details"):
    if entry_type == "Regular":
        fees = fee_data[selected_course]
        st.success(f"**Fee Structure for {selected_course} (Regular Entry):**")
        st.write(f"📌 **1st Year:** ₹{fees[0]:,}")
        st.write(f"📌 **2nd Year:** ₹{fees[1]:,}")
        st.write(f"📌 **3rd Year:** ₹{fees[2]:,}")
        st.write(f"📌 **4th Year:** ₹{fees[3]:,}")
        st.write(f"💰 **Total Fees:** ₹{fees[4]:,}")
    else:
        fees = fee_data_lateral[selected_course]
        st.success(f"**Fee Structure for {selected_course} (Lateral Entry):**")
        st.write(f"📌 **2nd Year:** ₹{fees[0]:,}")
        st.write(f"📌 **3rd Year:** ₹{fees[1]:,}")
        st.write(f"📌 **4th Year:** ₹{fees[2]:,}")
        st.write(f"💰 **Total Fees:** ₹{fees[3]:,}")

# Additional Fees
st.subheader("📌 Other Fees Details")
for fee_name, amount in additional_fees.items():
    st.write(f"🔹 **{fee_name}:** ₹{amount:,}")

# Hostel Fees
st.subheader("🏠 Hostel Fees - Inside the Campus")
for hostel_type, amount in hostel_fees.items():
    st.write(f"🏡 **{hostel_type}:** ₹{amount:,} per year")

st.info("📢 *Note: Refundable Hostel Caution Deposit ₹10,000 (Only in First Year)*")

# Footer
st.write("💡 *For more details, visit the official website or contact the admissions office!*")
