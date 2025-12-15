import streamlit as st
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Admin Dashboard",
    layout="wide"
)

st.title("📊 Admin Dashboard – Feedback Analysis")

# ---------------- CHECK DATA ----------------
if not os.path.exists("feedback.csv"):
    st.warning("No feedback data available yet.")
    st.stop()

# ---------------- LOAD DATA ----------------
df = pd.read_csv("feedback.csv")

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Feedback", len(df))
col2.metric("Average Rating", round(df["Rating"].mean(), 2))
col3.metric("Low Ratings (≤ 2)", len(df[df["Rating"] <= 2]))

st.divider()

# ---------------- FILTER ----------------
st.subheader("Filter Feedback")

rating_filter = st.selectbox(
    "Select Rating",
    ["All", 1, 2, 3, 4, 5]
)

if rating_filter != "All":
    df = df[df["Rating"] == rating_filter]

# ---------------- TABLE ----------------
st.subheader("Feedback Records")
st.dataframe(df, use_container_width=True)

st.divider()

# ---------------- DOWNLOAD ----------------
st.download_button(
    label="📥 Download Feedback CSV",
    data=df.to_csv(index=False),
    file_name="feedback.csv",
    mime="text/csv"
)