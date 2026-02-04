import streamlit as st
import base64
if "page" not in st.session_state:
    st.session_state.page = "home"


st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([8,1,1])

with col2:
    if st.button("ABOUT US"):
        st.session_state.page = "about"

with col3:
    st.button("CONTACT US")

def get_base64(img):
    with open(img, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
logo= get_base64("Spider_logo.png")

if st.session_state.page == "home": 
 st.markdown("""<style id = "newstyle">
             
if st.session_state.page == "about":
    st.markdown("""
<style>
.about-box {
    margin: 12vh auto;
    width: 70%;
    color: #EAF2FF;
    font-family: "Segoe UI", Consolas, monospace;
    line-height: 1.9;
    font-size: 24px;
    text-align: center;
}
.about-title {
    font-size: 64px;
    letter-spacing: 8px;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-box">
    <div class="about-title">🕷️ ABOUT SPIDER</div>

    Spider, the official Research and Development Club of the National Institute of Technology, Trichy, is a student-run
    technical organization dedicated to innovation in AI/ML, electronics, IoT, robotics, and web/app development.

    Founded in 2004, the club focuses on industry-relevant, practical projects through its core domains:

    <br><br>
    <b>Algorithms • Tronix • App Development • Web Development</b>
</div>
""", unsafe_allow_html=True)

if st.button("⬅ BACK"):
    st.session_state.page = "home"


<style id = "newstyle">




div[data-testid="stAppViewContainer"] {
    background-color: #000000 !important;
}



.logo{
            {
            position: fixed;
            top: 28px;
            left: 35px;
            width: 110px;
            }
            }
.cool-header {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 9999;

    font-family: 'Segoe UI', consolas, monospace !important;
    font-size: 90px;
    letter-spacing: 4px;
    text-align: center;

    color: #4DA3FF;

   
}
.bottom-btn {
    position: fixed !important;
    left: 50% !important;
    bottom: 30px !important;
    transform: translateX(-50%) !important;
    z-index: 99999 !important;

    padding: 14px 38px;
    border-radius: 40px;

    font-family: "Segoe UI", Consolas, monospace;
    font-size: 20px;
    letter-spacing: 2px;

    color: #000000;
    background-color: #EAF2FF;

    border: none;
    cursor: pointer;

    transition: all 0.3s ease;
}

.bottom-btn:hover {
    background-color: #7FDBFF;
    transform: translateX(-50%) scale(1.05);
}


</style>
""", unsafe_allow_html=True)

st.markdown('<div class="cool-header">WELCOME TO SPIDER WORKSHOP</div>', unsafe_allow_html=True)
st.markdown('<button class="bottom-btn">ENTER THE ARENA ---></button>', unsafe_allow_html=True)


