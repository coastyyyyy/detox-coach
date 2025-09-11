import streamlit as st
import pandas as pd
import os
import bcrypt

# ---------- FILES ----------
USER_FILE = "users.csv"
DATA_FILE = "users_data.csv"

# Create users.csv if missing
if not os.path.exists(USER_FILE):
    pd.DataFrame(columns=["name", "email", "password"]).to_csv(USER_FILE, index=False)

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["username", "points", "activity"]).to_csv(DATA_FILE, index=False)


# ---------- AUTH FUNCTIONS ----------
def signup(name, email, password, confirm_password):
    users_df = pd.read_csv(USER_FILE)

    if email in users_df["email"].values:
        return False, "Email already registered!"
    if password != confirm_password:
        return False, "Passwords do not match!"

    # Hash password
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Save to CSV
    users_df = pd.concat([users_df, pd.DataFrame({
        "name": [name],
        "email": [email],
        "password": [hashed_pw.decode()]
    })], ignore_index=True)
    users_df.to_csv(USER_FILE, index=False)
    return True, "Signup successful! Please login."


def login(email, password):
    users_df = pd.read_csv(USER_FILE)

    if email not in users_df["email"].values:
        return False, "Email not registered!"

    stored_pw = users_df.loc[users_df["email"] == email, "password"].values[0]

    if bcrypt.checkpw(password.encode(), stored_pw.encode()):
        name = users_df.loc[users_df["email"] == email, "name"].values[0]
        return True, name
    else:
        return False, "Incorrect password!"


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Detox Coach", page_icon="📱")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if not st.session_state.logged_in:
    choice = st.sidebar.radio("Login/Signup", ["Login", "Signup"])

    if choice == "Signup":
        st.subheader("🔑 Create a new account")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.button("Signup"):
            success, msg = signup(name, email, password, confirm_password)
            st.info(msg)

    else:
        st.subheader("🔓 Login to your account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            success, result = login(email, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.username = result
                st.success(f"Welcome {result}! 🎉")
                st.rerun()
            else:
                st.error(result)

else:
    # ---------- MAIN APP ----------
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

    st.title(f"📱 Welcome {st.session_state.username}!")
    st.subheader("Tell us about your screen time")

    app_name = st.text_input("App name (e.g., Instagram)")
    minutes = st.number_input("Minutes spent", min_value=0)
    hobbies = st.text_area("What hobbies do you enjoy? (e.g., reading, music, sports)")

    if st.button("Submit Usage"):
        if minutes > 60:
            suggestion = f"💡 Try reducing {app_name} by {minutes//2} minutes and spend that time on {hobbies or 'your hobbies'}."
        else:
            suggestion = "✅ Good balance! Keep it up!"
        st.info(suggestion)

        # Save points for activity
        points = 10 if minutes > 60 else 5
        df = pd.read_csv(DATA_FILE)
        df = pd.concat([df, pd.DataFrame({
            "username": [st.session_state.username],
            "points": [points],
            "activity": [f"Reduced {app_name} usage"]
        })], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)

        st.success(f"🎉 You earned {points} points!")

    st.subheader("🏆 Leaderboard")
    df = pd.read_csv(DATA_FILE)
    if not df.empty:
        leaderboard = df.groupby("username")["points"].sum().sort_values(ascending=False).reset_index()
        st.table(leaderboard)
