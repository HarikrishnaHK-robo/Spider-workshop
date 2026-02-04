import streamlit as st
import base64

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([8,1,1])

with col2:
    st.button("ABOUT US")

with col3:
    st.button("CONTACT US")

def get_base64(img):
    with open(img, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
logo= get_base64("Spider_logo.png")


st.markdown("""
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