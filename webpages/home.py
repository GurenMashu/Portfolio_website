import streamlit as st
def home():
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # You'll need to replace with your actual image
        st.markdown("""
        <div style="background-color: #0066cc; height: 200px; width: 200px; border-radius: 50%; display: flex; justify-content: center; align-items: center; margin: 0 auto;">
            <h1 style="color: white; font-size: 48px;">GM</h1>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; margin-top: 20px;'>Glenn Mathews</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Computer Science Engineering Student</p>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<h1 class='animated'>Hello, I'm Glenn Mathews</h1>", unsafe_allow_html=True)
        st.markdown("""
        <p class='animated' style='font-size: 18px; line-height: 1.6;'>
            I'm a Computer Science Engineering student specializing in Artificial Intelligence and Machine Learning. 
            I'm passionate about building innovative solutions using cutting-edge technologies.
        </p>
        <p class='animated' style='font-size: 18px; line-height: 1.6;'>
            Currently pursuing my B.Tech at Sree Chitra Thirunal College Of Engineering with a focus on AI/ML applications.
        </p>
        """, unsafe_allow_html=True)
        
        # Quick links
        st.markdown("<div class='animated'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <i class="fas fa-laptop-code" style="font-size: 24px; color: #0066cc;"></i>
                <h4>Python Developer</h4>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <i class="fas fa-robot" style="font-size: 24px; color: #0066cc;"></i>
                <h4>ML Enthusiast</h4>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="card" style="text-align: center;">
                <i class="fas fa-database" style="font-size: 24px; color: #0066cc;"></i>
                <h4>Data Analyst</h4>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
