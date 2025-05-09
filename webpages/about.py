import streamlit as st
def about():
    st.markdown("<h1 class='section-header'>About Me</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card animated">
        <p style='font-size: 18px; line-height: 1.8;'>
            I'm an optimistic engineering undergraduate and coder who considers myself responsible and flexible, always ready to learn. 
            With a keen interest in machine learning, I am actively improving my skills through hands-on learning and experiments.
        </p>
        <p style='font-size: 18px; line-height: 1.8;'>
            My career objective is to secure a challenging position in an innovative and forward-thinking company that will allow me to utilize my 
            skills and experience in new and exciting ways, leading to continuous personal and professional growth.
        </p>
        <p style='font-size: 18px; line-height: 1.8;'>
            I'm particularly passionate about Python programming, Machine Learning applications, and data structures & algorithms. 
            Currently, I'm focusing on implementing ML models in Kaggle competitions and expanding my knowledge in data science.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Languages section
    st.markdown("<h2 class='section-header'>Languages</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card">
            <h4 style="text-align: center;">English</h4>
            <div class="progress-container">
                <div class="progress-bar" style="width: 95%;">95%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h4 style="text-align: center;">Hindi</h4>
            <div class="progress-container">
                <div class="progress-bar" style="width: 80%;">80%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card">
            <h4 style="text-align: center;">Malayalam</h4>
            <div class="progress-container">
                <div class="progress-bar" style="width: 100%;">100%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
