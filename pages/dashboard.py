import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Check if user logged in
if "user" not in st.session_state:
    st.error("Please login first!")
    st.stop()

st.title(f"Welcome {st.session_state['user']} 👋")
st.subheader("Your Detox Dashboard")

apps = st.text_area("Enter apps you use most (comma separated):")
screen_time = st.number_input("Enter your average screen time (hours/day):", min_value=0, max_value=24)

if st.button("Get Recommendations"):
    if screen_time > 4:
        st.warning("⚠️ You spend a lot of time on screen! Try meditation, outdoor games, or reading.")
    else:
        st.success("✅ Great! You're maintaining healthy screen time.")

hobby = st.text_input("Enter your hobby:")
if hobby:
    st.info(f"💡 Try spending more time on your hobby: {hobby}")

# Points system
if "points" not in st.session_state:
    st.session_state["points"] = 0

if st.button("Upload Proof of Activity (Get Points)"):
    uploaded = st.file_uploader("Upload photo", type=["jpg", "png"])
    if uploaded:
        st.session_state["points"] += 10
        st.success("✅ Proof uploaded! You earned 10 points.")

st.metric("Your Points", st.session_state["points"])
