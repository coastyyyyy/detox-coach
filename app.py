import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("📱 AI Social Media Detox Coach")

# Path to CSV
DATA_PATH = "data/usage_sample.csv"

# Safe loading: check if file exists and has content
if os.path.exists(DATA_PATH):
    try:
        df = pd.read_csv(DATA_PATH)
        if df.empty:
            st.warning("⚠️ CSV file is empty. Upload data to see stats.")
    except pd.errors.EmptyDataError:
        st.warning("⚠️ CSV file is empty or corrupted.")
        df = pd.DataFrame(columns=["date", "app", "minutes", "hour_block", "text"])
else:
    st.warning("⚠️ CSV file not found. Upload data to see stats.")
    df = pd.DataFrame(columns=["date", "app", "minutes", "hour_block", "text"])

# Only plot if df is not empty
if not df.empty:
    df['date'] = pd.to_datetime(df['date']).dt.date
    st.subheader("📊 Usage Stats by App")
    st.bar_chart(df.groupby('app')['minutes'].sum())
    st.subheader("📈 Daily Usage")
    st.line_chart(df.groupby('date')['minutes'].sum())
