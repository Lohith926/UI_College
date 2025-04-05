import streamlit as st


def get_fee_structure(percentage, course):
    fee_data = {
        "CSE / AIDS / AIML & CSE Specialization": [(90, 250000), (80, 302500), (70, 355000), (65, 407500), (60, 460000)],
        "IT": [(85, 200000), (75, 233750), (70, 267500), (65, 301250), (60, 335000)],
        "Bio-info / Bio-tech / ECE": [(85, 200000), (75, 230000), (70, 260000), (65, 290000), (60, 320000)],
        "EEE, MECH, CIVIL, BME, DENTAL": [(0, 160000)],
    }

    for min_percentage, fee in fee_data.get(course, []):
        if percentage >= min_percentage:
            return fee
    return "Not Available"


def main():
    st.set_page_config(page_title="Saveetha University Fee Calculator", page_icon="🎓", layout="centered")

    st.title("Saveetha University Fee Structure 2025-26")
    st.subheader("Enter your details to check the applicable fee")

    courses = [
        "CSE / AIDS / AIML & CSE Specialization",
        "IT",
        "Bio-info / Bio-tech / ECE",
        "EEE, MECH, CIVIL, BME, DENTAL"
    ]

    selected_course = st.selectbox("Select Your Course", courses)
    student_percentage = st.number_input("Enter Your Percentage", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Get Fee Details"):
        if student_percentage < 60:
            st.error("You are not eligible as your percentage is below 60%.")
        else:
            fee = get_fee_structure(student_percentage, selected_course)
            if fee == "Not Available":
                st.error("No fee structure available for this percentage range.")
            else:
                st.success(f"Your applicable fee for {selected_course} is ₹{fee}")


if __name__ == "__main__":
    main()
