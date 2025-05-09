import streamlit as st
def contact():
    st.markdown("<h1 class='section-header'>Contact Me</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card contact-info">
            <h3 style="color: white;">Contact Information</h3>
            <p><i class="fas fa-envelope"></i> glennmathews18@gmail.com</p>
            <p><i class="fas fa-phone"></i> +91 8848693581 (WhatsApp/Calls)</p>
            <p><i class="fas fa-map-marker-alt"></i> NCC Road, Amballamukku, Trivandrum, Kerala</p>
        </div>
        
        <div class="card">
            <h3>Connect With Me</h3>
            <div style="display: flex; gap: 15px; margin-top: 15px;">
                <a href="https://www.linkedin.com/in/glenn-mathews-0a9641253/" target="_blank" style="text-decoration: none;">
                    <div class="skill-tag"><i class="fab fa-linkedin"></i> LinkedIn</div>
                </a>
                <a href="https://github.com/GurenMashu" target="_blank" style="text-decoration: none;">
                    <div class="skill-tag"><i class="fab fa-github"></i> GitHub</div>
                </a>
                <a href="https://leetcode.com/u/_Glenn_Matthews/" target="_blank" style="text-decoration: none;">
                    <div class="skill-tag"><i class="fas fa-code"></i> LeetCode</div>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h3>Send Me a Message</h3>", unsafe_allow_html=True)
        
        # Contact form (note: this is for display only, as Streamlit doesn't process forms natively)
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        if st.button("Send Message", type="primary"):
            st.success("Thank you for your message! I'll get back to you soon.")
            
        st.info("Note: This is a demonstration form. To enable actual email functionality, you would need to integrate with an email service or backend.")
