import streamlit as st

# Page Config
st.set_page_config(page_title="Detox Coach", page_icon="📱", layout="centered")

# Background Style (matches your design)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.ibb.co/dQkbW8W/background.jpg"); /* Replace with your bg image */
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
.login-box {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>📱 Detox Coach</h1>", unsafe_allow_html=True)

# Login / Signup tabs
tab1, tab2 = st.tabs(["🔑 Login", "🆕 Sign Up"])

with tab1:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email and password:
            st.session_state["user"] = email
            st.switch_page("pages/dashboard.py")  # Go to dashboard
        else:
            st.error("Please enter both email and password.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    name = st.text_input("Full Name")
    signup_email = st.text_input("Email (for signup)")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Sign Up"):
        if new_password == confirm_password and signup_email and name:
            st.success("Account created! Please login.")
        else:
            st.error("Passwords do not match or fields are empty.")
    st.markdown("</div>", unsafe_allow_html=True)
