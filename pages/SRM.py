import streamlit as st

# Move fee data outside the function so we can access it globally
fee_data = {
    "Civil Engineering": 250000,
    "Electronics and Communication Engineering (AI/ML)": 250000,
    "Electronics and Communication Engineering (Embedded Systems & IoT)": 250000,
    "Electronics and Communication Engineering (VLSI Design)": 250000,
    "Microelectronics and VLSI": 250000,
    "Mechanical Engineering (Automotive Engineering)": 250000,
    "Computer Science and Engineering - AI and Future Technologies": 460000,
    "Computer Science and Engineering - Software Product Engineering": 460000,
    "Civil Engineering (Structural Engineering)": 250000,
    "Computer Science and Engineering": 400000,
    "Computer Science and Engineering (Big Data Analytics)": 360000,
    "Computer Science and Engineering (AI & ML)": 400000,
    "Computer Science and Engineering (Distributed & Cloud Computing)": 360000,
    "Computer Science and Engineering (Cyber Security)": 360000,
    "Computer Science and Engineering (Internet of Things)": 360000,
    "Electrical and Electronics Engineering": 250000,
    "Electrical and Electronics Engineering (Renewable Energy)": 250000,
    "Electronics and Communication Engineering": 250000,
    "Electronics and Communication Engineering (Advanced Communication Systems)": 250000,
    "Mechanical Engineering": 250000,
    "Mechanical Engineering (Robotics and Automation)": 250000,
    "Mechanical Engineering (Additive Manufacturing)": 250000,
    "M.Tech Artificial Intelligence and Machine Learning": 150000,
    "M.Tech Environmental and Sustainable Engineering": 150000,
    "M.Tech Embedded Systems and IoT": 150000,
    "M.Tech Materials and Manufacturing Technology": 150000,
    "M.Tech Cyber Security": 150000,
    "M.Tech Data Science": 150000,
    "M.Tech VLSI": 150000,
    "M.Tech Thermal Engineering": 150000,
    "Integrated M.Tech (Data Science)": 300000,
    "Integrated M.Tech (AI & ML)": 300000,
}

def get_fee_structure(course):
    return fee_data.get(course, "Not Available")

def main():
    st.set_page_config(page_title="SRM AP Fee Calculator", page_icon="🎓", layout="centered")
    st.title("SRM Andhra Pradesh Fee Structure 2025-26")
    st.subheader("Select your course to check the applicable fee")

    courses = list(fee_data.keys())  # now works fine
    selected_course = st.selectbox("Select Your Course", courses)

    if st.button("Get Fee Details"):
        fee = get_fee_structure(selected_course)
        if fee == "Not Available":
            st.error("No fee structure available for the selected course.")
        else:
            st.success(f"The applicable annual fee for {selected_course} is ₹{fee:,}")

if __name__ == "__main__":
    main()
