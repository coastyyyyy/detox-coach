import streamlit as st
import pandas as pd
import os
from PIL import Image

# File to store user data
DATA_FILE = "users_data.csv"
if os.path.exists(DATA_FILE):
    users_df = pd.read_csv(DATA_FILE)
else:
    users_df = pd.DataFrame(columns=["username", "points", "activity", "photo"])

st.title("📱 AI Social Media Detox Coach")

# 1️⃣ User Input
username = st.text_input("Enter your name:")

st.subheader("Enter your daily app usage")
app_name = st.text_input("App name (e.g., Instagram)")
minutes = st.number_input("Minutes spent", min_value=0)

if st.button("Submit Usage") and username:
    st.success(f"Data recorded: {app_name} - {minutes} minutes")
    
    # 2️⃣ AI Suggestions
    if minutes > 60:
        st.info("💡 Suggestion: Take a short walk, meditate, or read a book for 15 mins")
    else:
        st.info("💡 Suggestion: Good balance! Keep it up!")

# 3️⃣ Photo upload
st.subheader("Upload photo of activity completion")
uploaded_file = st.file_uploader("Upload image", type=["png","jpg","jpeg"])

if uploaded_file is not None and username:
    image = Image.open(uploaded_file)
    st.image(image, caption="Activity completed!", use_column_width=True)
    
    # 4️⃣ Give points
    new_points = 10
    st.success(f"🎉 You earned {new_points} points!")
    
    # Save to CSV
    users_df = pd.concat([users_df, pd.DataFrame({
        "username":[username],
        "points":[new_points],
        "activity":["Completed Activity"],
        "photo":[uploaded_file.name]
    })], ignore_index=True)
    
    users_df.to_csv(DATA_FILE, index=False)

# 5️⃣ Leaderboard
st.subheader("🏆 Leaderboard")
if not users_df.empty:
    leaderboard = users_df.groupby("username")["points"].sum().sort_values(ascending=False).reset_index()
    st.table(leaderboard)
