import streamlit as st
import base64

st.set_page_config(layout="wide")
def get_base64(img):
    with open(img, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
logo= get_base64("Spider_logo.png")


st.markdown("""
<style>


div[data-testid="stAppViewContainer"] {
    background-color: #0B1F3A !important;
}


<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@700&display=swap" rel="stylesheet">


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

    font-family: 'Rajdhani', sans-serif !important;
    font-size: 90px;
    letter-spacing: 4px;
    text-align: center;

    color: #EAF2F;

    text-shadow:
        0 0 10px #EAF2F,
        0 0 20px #EAF2F,
        0 0 40px #EAF2F,
        0 0 80px #EAF2F;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="cool-header">WELCOME TO SPIDER WORKSHOP</div>', unsafe_allow_html=True)



