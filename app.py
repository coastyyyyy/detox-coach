import streamlit as st

# -------------------------
# Simulated Database
# -------------------------
users = {}
if "user" not in st.session_state:
    st.session_state.user = None


# -------------------------
# Signup Page
# -------------------------
def signup():
    st.title("Detox Coach 🌱")
    st.subheader("Create your account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if email in users:
            st.error("❌ Email already registered!")
        elif password != confirm_password:
            st.error("❌ Passwords do not match!")
        else:
            users[email] = {"name": name, "password": password, "points": 0}
            st.success("✅ Signup successful! Please login.")
            st.session_state.user = email
            st.rerun()


# -------------------------
# Login Page
# -------------------------
def login():
    st.title("Detox Coach 🌱")
    st.subheader("Welcome Back")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in users and users[email]["password"] == password:
            st.success(f"✅ Welcome {users[email]['name']}!")
            st.session_state.user = email
            st.rerun()
        else:
            st.error("❌ Invalid credentials!")


# -------------------------
# Main Detox Page (After Login)
# -------------------------
def detox_page():
    st.title("📱 Detox Coach Dashboard")
    st.write(f"Hello, **{users[st.session_state.user]['name']}** 👋")

    st.subheader("Enter Your Screen Time (in hours per day)")
    app_name = st.text_input("App Name (e.g., Instagram, YouTube, etc.)")
    screen_time = st.number_input("Screen Time (hours)", min_value=0.0, step=0.5)

    st.subheader("Your Hobbies")
    hobbies = st.text_area("List your hobbies (comma separated)")

    if st.button("Get Recommendations"):
        if app_name and screen_time > 0:
            st.info(f"⚡ You spend {screen_time} hours on {app_name}.")
            st.success("💡 Recommendation: Try replacing some screen time with your hobbies.")
            if hobbies:
                hobby_list = hobbies.split(",")
                st.write("👉 Suggested Alternatives:")
                for hobby in hobby_list:
                    st.write(f"- {hobby.strip()}")
            else:
                st.write("👉 Suggested: Try walking, reading, or exercise.")
        else:
            st.warning("Please fill out your screen time and app name.")

    st.subheader("Upload proof & earn points 🎯")
    uploaded = st.file_uploader("Upload a photo of you doing your hobby/activity")
    if uploaded:
        users[st.session_state.user]["points"] += 10
        st.success("✅ Proof uploaded! +10 points earned.")

    st.subheader("🏆 Leaderboard")
    leaderboard = sorted(users.items(), key=lambda x: x[1]["points"], reverse=True)
    for rank, (email, data) in enumerate(leaderboard, start=1):
        st.write(f"{rank}. {data['name']} - {data['points']} points")

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()


# -------------------------
# App Flow
# -------------------------
if st.session_state.user is None:
    choice = st.radio("Choose an option:", ["Login", "Signup"], horizontal=True)
    if choice == "Login":
        login()
    else:
        signup()
else:
    detox_page()
