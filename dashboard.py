import streamlit as st
import pandas as pd

st.title("📊 Video Analytics Dashboard")

# Load data
df = pd.read_csv("data.csv", names=["time", "count"])

# Convert time column
df["time"] = pd.to_datetime(df["time"])

# Metrics
st.metric("Current Count", int(df["count"].iloc[-1]))
st.metric("Max Count", int(df["count"].max()))

# Line chart
st.subheader("Footfall Over Time")
st.line_chart(df.set_index("time")["count"])

# Table view
st.subheader("Raw Data")
st.dataframe(df.tail(20))