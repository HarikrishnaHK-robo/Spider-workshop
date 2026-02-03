import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>

/* Premium dark hardware background */
div[data-testid="stAppViewContainer"] {
    background-color: #0B1320 !important;
}

/* Futuristic font */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

/* Center glowing header */
.cool-header {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 9999;

    font-family: 'Orbitron', sans-serif;
    font-size: 90px;
    letter-spacing: 4px;
    text-align: center;

    color: #00F5FF;

    text-shadow:
        0 0 10px #00F5FF,
        0 0 20px #00F5FF,
        0 0 40px #00F5FF,
        0 0 80px #00F5FF;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="cool-header">SPIDER HARDWARE WORKSHOP</div>', unsafe_allow_html=True)
