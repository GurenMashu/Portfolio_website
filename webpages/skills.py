import streamlit as st
import pandas as pd
def skills():
    st.markdown("<h1 class='section-header'>Skills</h1>", unsafe_allow_html=True)
    
    # Technical Skills
    st.markdown("<h2>Technical Skills</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Programming & Tools</h3>
            <div class="skill-tag">Python3</div>
            <div class="skill-tag">C</div>
            <div class="skill-tag">MySQL</div>
            <div class="skill-tag">Data Structures and Algorithms</div>
            <div class="skill-tag">Linux Systems</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Machine Learning</h3>
            <div class="skill-tag">Machine Learning</div>
            <div class="skill-tag">Scikit-Learn</div>
            <div class="skill-tag">Data Science</div>
            <div class="skill-tag">Kaggle Competitions</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Skill visualization
    st.markdown("<h2>Skill Proficiency</h2>", unsafe_allow_html=True)
    
    skills_data = {
        "Skill": ["Python", "Machine Learning", "Scikit-Learn", "Data Structures", "C", "MySQL", "Linux"],
        "Proficiency": [90, 85, 80, 85, 75, 80, 70]
    }
    
    df = pd.DataFrame(skills_data)
    
    for index, row in df.iterrows():
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <p style="margin-bottom: 5px;">{row['Skill']}</p>
            <div class="progress-container">
                <div class="progress-bar" style="width: {row['Proficiency']}%;">{row['Proficiency']}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
