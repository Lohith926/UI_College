import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="B.Tech Admissions 2025-26", page_icon="🎓", layout="centered")
    
    st.markdown(
        """
        <style>
            .stApp {
                animation: gradientBG 10s ease infinite;
                background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
                background-size: 400% 400%;
            }
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            .main-container {
                text-align: center;
                color: black;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                margin: auto;
                width: 60%;
            }
            .result-box {
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                background-color: #ffdde1;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }
        </style>
        <div class='main-container'>
            <h1>B.Tech Admissions 2025-26</h1>
            <h3>Select Your College and Course to Proceed</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    colleges = [
        "Veltech University", "Sai University", "SRM University", "Saveetha University", "Kanchi University",
        "Takshila University", "Dhanalakshmi University", "Mgr University", "Marwadi University (Rajkot, Gujarat)",
        "Bennett University (Greater Noida)", "Alliance University (Bangalore)", "Akash (Bangalore)",
        "Acharya (Bangalore)", "Uttaranchal University (Dehradun)", "PP Savani University (Surat, Gujarat)",
        "Sandeep University (Maharashtra, Nasik)", "ITM University (Gwalior, Madhya Pradesh)", "Joy University",
        "NIMS University"
    ]
    
    courses = [
        "Choose", "Computer Science and Engineering","Computer Science and Engineering(AI & ML)","Computer Science and Engineering(CS)","Computer Science and Engineering(DS)", "AI & ML", "AI & DS","IT", "CSD",
        "Electronics and Communication Engineering", "Bio-Tech", "AERO", "MECH", "EEE", "CIVIL", "BIO MED"
    ]
    
    fee_structure = {
        "Computer Science and Engineering": {
            "90-100": {"I,II": (123750, "25%"), "III": (131250, "25%")} ,
            "70-89.9": {"I,II": (131250, "25%"), "III": (145500, "10%")} ,
            "45-69.9": {"I,II": (195000, "0%"), "III": (195000, "0%")} 
        },
      "Computer Science and Engineering(AI & ML)": {
            "90-100": {"I,II": (123750, "25%"), "III": (131250, "25%")} ,
            "70-89.9": {"I,II": (131250, "25%"), "III": (145500, "10%")} ,
            "45-69.9": {"I,II": (195000, "0%"), "III": (195000, "0%")} 
        },
      "Computer Science and Engineering(CS)": {
            "90-100": {"I,II": (123750, "25%"), "III": (131250, "25%")} ,
            "70-89.9": {"I,II": (131250, "25%"), "III": (145500, "10%")} ,
            "45-69.9": {"I,II": (195000, "0%"), "III": (195000, "0%")} 
        },
      "Computer Science and Engineering(DS)": {
            "90-100": {"I,II": (123750, "25%"), "III": (131250, "25%")} ,
            "70-89.9": {"I,II": (131250, "25%"), "III": (145500, "10%")} ,
            "45-69.9": {"I,II": (195000, "0%"), "III": (195000, "0%")} 
        },
        "AI & ML": {
            "90-100": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "70-89.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} ,
            "45-69.9": {"I,II": (105000, "25%"), "III": (123750, "25%")} 
        },
        "AI & DS": {
            "90-100": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "70-89.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} ,
            "45-69.9": {"I,II": (105000, "25%"), "III": (123750, "25%")} 
        },
      "IT": {
            "90-100": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "70-89.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} ,
            "45-69.9": {"I,II": (105000, "25%"), "III": (123750, "25%")} 
        },
        "Electronics and Communication Engineering": {
            "90-100": {"I,II": (60000, "75%"), "III": (87500, "50%")} ,
            "70-89.9": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "45-69.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} 
        },

      "CSD": {
            "90-100": {"I,II": (60000, "75%"), "III": (87500, "50%")} ,
            "70-89.9": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "45-69.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} 
        },
        "Bio-Tech": {
            "90-100": {"I,II": (60000, "75%"), "III": (87500, "50%")} ,
            "70-89.9": {"I,II": (87500, "50%"), "III": (92500, "50%")} ,
            "45-69.9": {"I,II": (92500, "50%"), "III": (105000, "50%")} 
        },
        "AERO": {
            "90-100": {"I,II": (51250, "75%"), "III": (53750, "50%")} ,
            "70-89.9": {"I,II": (53750, "50%"), "III": (60000, "50%")} ,
            "45-69.9": {"I,II": (60000, "50%"), "III": (87500, "50%")} 
        },

       

        "MECH": {
            "90-100": {"I,II": (51250, "75%"), "III": (53750, "50%")} ,
            "70-89.9": {"I,II": (53750, "50%"), "III": (60000, "50%")} ,
            "45-69.9": {"I,II": (60000, "50%"), "III": (87500, "50%")} 
        },

        "EEE": {
            "90-100": {"I,II": (51250, "75%"), "III": (53750, "50%")} ,
            "70-89.9": {"I,II": (53750, "50%"), "III": (60000, "50%")} ,
            "45-69.9": {"I,II": (60000, "50%"), "III": (87500, "50%")} 
        },

        "CIVIL": {
            "90-100": {"I,II": (51250, "75%"), "III": (53750, "50%")} ,
            "70-89.9": {"I,II": (53750, "50%"), "III": (60000, "50%")} ,
            "45-69.9": {"I,II": (60000, "50%"), "III": (87500, "50%")} 
        },

        "BIO MED": {
            "90-100": {"I,II": (51250, "75%"), "III": (53750, "50%")} ,
            "70-89.9": {"I,II": (53750, "50%"), "III": (60000, "50%")} ,
            "45-69.9": {"I,II": (60000, "50%"), "III": (87500, "50%")} 
        },

    }
    
    selected_college = st.selectbox("Choose your preferred college", colleges)
    selected_course = st.selectbox("Choose which course you are interested in?", courses, index=0)
    student_percentage = st.number_input("Enter your PCM percentage", min_value=0.0, max_value=100.0, step=0.1)
    
    if st.button("Get Your Benefit"):
        if selected_course in fee_structure:
            phase = "I,II" if student_percentage >= 70 else "III"
            for range_key, phases in fee_structure[selected_course].items():
                if float(range_key.split("-")[0]) <= student_percentage <= float(range_key.split("-")[1]):
                    fee, scholarship = phases[phase]
                    st.markdown(f"""
                    <div class='result-box'>
                        The semester fee for <b>{selected_course}</b> at <b>{selected_college}</b> is <b>INR {fee}</b> based on your percentage. You fall under <b>Phase {phase}</b> with a <b>{scholarship} scholarship</b>.
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("Please select a valid course to view the fee structure.")
            
if __name__ == "__main__":
    main()
