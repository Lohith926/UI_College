import streamlit as st

def get_fee_structure(course=None):
    fee_data = {
        "B.E COMPUTER SCIENCE": [375000, 350000, 350000, 355000],
        "B.E CSE AI & ML": [450000, 425000, 425000, 430000],
        "B.E CSE AI": [425000, 400000, 400000, 405000],
        "B.E CSE AI & DATA SCIENCE": [425000, 400000, 400000, 405000],
        "B.E CSE DATA SCIENCE": [425000, 400000, 400000, 405000],
        "B.E CSE AI & ROBOTICS": [425000, 400000, 400000, 405000],
        "B.E CSE CYBER SECURITY": [425000, 400000, 400000, 405000],
        "B.E CSE INTERNET OF THINGS": [425000, 400000, 400000, 405000],
        "B.E MECHANICAL ENGINEERING": [160000, 150000, 150000, 155000],
        "B.TECH CHEMICAL ENGINEERING": [160000, 150000, 150000, 155000],
        "B.E AERONAUTICAL ENGINEERING": [160000, 150000, 150000, 155000],
        "B.E ECE": [250000, 225000, 225000, 230000],
        "B.E ECE WITH DATA SCIENCE": [250000, 225000, 225000, 230000],
        "B.TECH INFORMATION TECHNOLOGY": [375000, 350000, 350000, 355000],
        "B.TECH BIO TECHNOLOGY": [325000, 300000, 300000, 305000],
        "B.TECH BIO MEDICAL ENGINEERING": [250000, 225000, 225000, 220000],
        "B.E MECHATRONICS": [185000, 175000, 175000, 170000],
        "B.E EEE": [160000, 150000, 150000, 155000],
        "B.E CIVIL ENGINEERING": [160000, 150000, 150000, 155000],
        "BSC NURSING": [200000, 200000, 200000, 200000],
        "B-PHARM": [250000, 225000, 225000, 220000],
        "PHARMACY D (6 Years)": [375000, 375000, 375000, 375000],
        "MBA (Semester Fees)": [175000, 175000, 175000, 175000],
        "B.ARCH": [275000, 250000, 250000, 255000],
        "B.DES": [300000, 275000, 275000, 280000],
        "BBA": [180000, 175000, 175000, None],  # N/A for 4th Year
        "B.COM": [175000, 170000, 170000, None],  # N/A for 4th Year
        "B.SC COMPUTER SCIENCE": [200000, 190000, 190000, None],  # N/A for 4th Year
    }

    if course:
        return fee_data.get(course, ["Not Available"] * 4)
    return list(fee_data.keys())  # Returns all department names if no course is provided


def main():
    st.set_page_config(page_title="Sathyabama University Fee Calculator", page_icon="🎓", layout="centered")
    st.title("Sathyabama University Fee Structure 2025-26")

    # Fetching all department names
    courses = get_fee_structure()
    selected_course = st.selectbox("Select Your Course", courses)

    if st.button("Get Fee Details"):
        fees = get_fee_structure(selected_course)
        if fees[0] == "Not Available":
            st.error("No fee structure available for the selected course.")
        else:
            st.success(f"Fee Structure for {selected_course}:")
            st.write(f"📌 **1st Year:** ₹{fees[0]:,}")
            st.write(f"📌 **2nd Year:** ₹{fees[1]:,}")
            st.write(f"📌 **3rd Year:** ₹{fees[2]:,}")
            if fees[3] is not None:
                st.write(f"📌 **4th Year:** ₹{fees[3]:,}")
            else:
                st.write("📌 **4th Year:** Not Applicable")

    # Displaying hostel fees
    st.subheader("🏠 Hostel Fees")
    st.write("**Non-AC Hostel Fee:** ₹1,20,000 per year")


if __name__ == "__main__":
    main()
