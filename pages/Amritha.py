import streamlit as st

def get_fee_structure(campus, course):
    fee_data = {
        "COIMBATORE MAIN": {"CSE, AI, AI&DS, CYBER": (600000, 300000), "E.C.E": (500000, 200000)},
        "BANGALORE": {"CSE, AI, AI&DS, CYBER": (600000, 300000), "E.C.E": (500000, 200000)},
        "AMRITAPURI KERALA": {"CSE, AI, AI&DS, CYBER": (600000, 300000), "E.C.E": (450000, 200000)},
        "CHENNAI": {"CSE, AI, AI&DS, CYBER": (450000, 200000), "E.C.E": (350000, 100000)},
        "AMARAVATI": {"CSE, AI, AI&DS, CYBER": (450000, 200000), "E.C.E": (350000, 100000)},
    }
    return fee_data.get(campus, {}).get(course, (None, None))

def main():
    st.set_page_config(page_title="Amrita University Fee Calculator", page_icon="🎓", layout="centered")
    
    st.title("Amrita University Fee Structure 2025-26")
    st.subheader("Enter your details to check the applicable fee")
    
    campuses = ["COIMBATORE MAIN", "BANGALORE", "AMRITAPURI KERALA", "CHENNAI", "AMARAVATI"]
    courses = ["CSE, AI, AI&DS, CYBER", "E.C.E"]
    
    selected_campus = st.selectbox("Select Your Campus", campuses)
    selected_course = st.selectbox("Select Your Course", courses)
    
    if st.button("Get Fee Details"):
        fee, donation = get_fee_structure(selected_campus, selected_course)
        if fee is None:
            st.error("No fee structure available for the selected options.")
        else:
            st.success(f"Your applicable fee for {selected_course} at {selected_campus} is ₹{fee} with a donation of ₹{donation}.")

if __name__ == "__main__":
    main()
