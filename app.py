import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("📱 AI Social Media Detox Coach")

DATA_PATH = "data/usage_sample.csv"

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    st.warning("⚠️ CSV file not found. Upload your data to see stats.")
    df = pd.DataFrame(columns=["date","app","minutes","hour_block","text"])

if not df.empty:
    df['date'] = pd.to_datetime(df['date']).dt.date

    st.subheader("📊 Usage Stats by App")
    st.bar_chart(df.groupby('app')['minutes'].sum())

    st.subheader("📈 Daily Usage")
    st.line_chart(df.groupby('date')['minutes'].sum())
