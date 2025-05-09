import streamlit as st
from PIL import Image
from pathlib import Path
from CSScomponents import local_css, load_fontawesome
from webpages import *

st.set_page_config(
    page_title="Glenn Mathews | Portfolio",
    page_icon="💻",
    layout="wide",
)

local_css()
load_fontawesome()

def sidebar():
    with st.sidebar:
        st.markdown("# Portfolio")
        st.markdown("---")
        
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
        if st.button("👨‍💻 About Me", use_container_width=True):
            st.session_state.page = "about"
        if st.button("🎓 Education", use_container_width=True):
            st.session_state.page = "education"
        if st.button("🛠️ Skills", use_container_width=True):
            st.session_state.page = "skills"
        if st.button("📊 Projects", use_container_width=True):
            st.session_state.page = "projects"
        if st.button("🏆 Achievements", use_container_width=True):
            st.session_state.page = "achievements"
        if st.button("📞 Contact", use_container_width=True):
            st.session_state.page = "contact"
        
        st.markdown("---")
        st.markdown("""
        <div class="social-links">
            <a href="https://github.com/GurenMashu" target="_blank"><i class="fab fa-github social-icon"></i></a>
            <a href="https://www.linkedin.com/in/glenn-mathews-0a9641253/" target="_blank"><i class="fab fa-linkedin social-icon"></i></a>
            <a href="https://leetcode.com/u/_Glenn_Matthews/" target="_blank"><i class="fas fa-code social-icon"></i></a>
        </div>
        """, unsafe_allow_html=True)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

def main():
    sidebar()
    
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "about":
        about()
    elif st.session_state.page == "education":
        education()
    elif st.session_state.page == "skills":
        skills()
    elif st.session_state.page == "projects":
        projects()
    elif st.session_state.page == "achievements":
        achievements()
    elif st.session_state.page == "contact":
        contact()

if __name__ == "__main__":
    main()