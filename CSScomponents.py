import streamlit as st
def local_css():
    st.markdown("""
    <style>
        /* Main page styling */
        .main {
            background-color: #f8f9fa;
            color: #212529;
            font-family: 'Roboto', sans-serif;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: #212529;
            font-weight: 700;
        }
        
        /* Section styling */
        .section-header {
            font-size: 24px;
            padding-bottom: 10px;
            /*border-bottom: 2px solid #0066cc;*/
            margin-bottom: 20px;
        }
        
        /* Card styling for projects and experiences */
        .card {
            background-color: grey;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Contact info */
        .contact-info {
            background-color: #0066cc;
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        /* Skills */
        .skill-tag {
            background-color: #e9ecef;
            color: #212529;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 5px;
            display: inline-block;
        }
        
        /* Progress bars */
        .progress-container {
            width: 100%;
            background-color: #e9ecef;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        
        .progress-bar {
            background-color: #0066cc;
            color: white;
            padding: 3px 0;
            text-align: center;
            border-radius: 10px;
        }
        
        /* Social links */
        .social-links {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
        }
        
        .social-icon {
            font-size: 24px;
            color: #0066cc;
        }
        
        /* Timeline */
        .timeline-item {
            padding-left: 20px;
            /*border-left: 2px solid #0066cc;*/
            margin-bottom: 20px;
            position: relative;
        }
        
        .timeline-item:before {
            content: "";
            position: absolute;
            left: -7px;
            top: 0;
            width: 12px;
            height: 12px;
            background-color: #0066cc;
            border-radius: 50%;
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .animated {
            animation: fadeIn 1s ease;
        }
        
        /* Custom tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: white;
            border-radius: 5px 5px 0 0;
            padding: 10px 16px;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #0066cc;
            color: white;
        }
        
        /* For mobile responsiveness */
        @media screen and (max-width: 768px) {
            .section-header {
                font-size: 20px;
            }
            
            .card {
                padding: 15px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Add FontAwesome for icons
def load_fontawesome():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)