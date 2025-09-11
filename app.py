import streamlit as st

st.set_page_config(page_title="Detox Coach", page_icon="🌱", layout="centered")

# Custom CSS to replicate the exact design
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f2f6f9, #e6ebf0);
        font-family: 'Segoe UI', sans-serif;
    }
    .login-card {
        background-color: #fff;
        padding: 40px 30px;
        border-radius: 25px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.1);
        width: 380px;
        margin: 80px auto;
        text-align: center;
    }
    .logo {
        margin-bottom: 15px;
    }
    .title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
    }
    .subtitle {
        font-size: 13px;
        color: #666;
        margin-bottom: 25px;
    }
    .btn {
        padding: 10px 0;
        width: 120px;
        border: none;
        border-radius: 25px;
        font-size: 14px;
        font-weight: bold;
        margin: 10px 8px;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .btn-login {
        background: #6da9e4;
        color: white;
    }
    .btn-login:hover {
        background: #558ed4;
    }
    .btn-signup {
        background: #8ed1a5;
        color: white;
    }
    .btn-signup:hover {
        background: #6bbd89;
    }
    .input-box {
        width: 100%;
        padding: 12px 40px;
        margin: 12px 0;
        border-radius: 12px;
        border: 1px solid #ddd;
        font-size: 14px;
    }
    .forgot {
        text-align: right;
        font-size: 12px;
        margin: 5px 0 20px 0;
    }
    .forgot a {
        color: #6da9e4;
        text-decoration: none;
    }
    .or {
        font-size: 12px;
        color: #888;
        margin: 15px 0;
    }
    .social-icons img {
        margin: 0 8px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# HTML content
st.markdown("""
<div class="login-card">
    <div class="logo">
        <img src="https://img.icons8.com/fluency/48/leaf.png" width="50"/>
    </div>
    <div class="title">DETOX COACH</div>
    <div class="subtitle">Reclaim Your Time</div>

    <button class="btn btn-login">LOGIN</button>
    <button class="btn btn-signup">SIGNUP</button>

    <input type="text" placeholder="Email" class="input-box"/>
    <input type="password" placeholder="Password" class="input-box"/>

    <div class="forgot"><a href="#">Forgot Password?</a></div>

    <div class="or">or continue with</div>
    <div class="social-icons">
        <img src="https://img.icons8.com/color/32/facebook-new.png"/>
        <img src="https://img.icons8.com/color/32/google-logo.png"/>
        <img src="https://img.icons8.com/ios-filled/32/mac-os.png"/>
    </div>
</div>
""", unsafe_allow_html=True)
