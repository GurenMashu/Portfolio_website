import streamlit as st
def achievements():
    st.markdown("<h1 class='section-header'>Achievements & Certifications</h1>", unsafe_allow_html=True)
    
    achievements_list = [
        {
            "title": "Hugging Face (ML) Workshop",
            "description": "Completed comprehensive training in ML model development and deployment using Hugging Face's transformer library."
        },
        {
            "title": "GDSC Machine Learning Beginner Track",
            "description": "Participated in Google Developer Student Clubs' Machine Learning beginner track, gaining fundamental ML knowledge."
        },
        {
            "title": "YIP-KDISC (Young Innovators Program)",
            "description": "Successfully completed the Young Innovators Program conducted by Kerala Development & Innovation Strategic Council."
        },
        {
            "title": "Smart India Hackathon 2024",
            "description": "Participated in Smart India Hackathon 2024, developing innovative solutions to real-world problems."
        },
        {
            "title": "ICSET 2024",
            "description": "Participated in the International Conference on Science, Engineering, and Technology 2024."
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, achievement in enumerate(achievements_list):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="card animated">
                <h3>{achievement["title"]}</h3>
                <p>{achievement["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
