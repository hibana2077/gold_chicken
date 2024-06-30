import streamlit as st
import requests
import os
import pandas as pd
import numpy as np

from plotly import express as px

st.title('Dashboard')

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Profit", "$1,234", "2%")
col2.metric("Max Drawdown", "3%", "-1%")
col3.metric("Win Rate", "70%", "1%")

st.divider()

st.subheader("Profit Chart")
data = pd.DataFrame({
    "Date": pd.date_range("2024-03-01", periods=100),
    "Profit": np.random.randn(100).cumsum() * 1000
})
fig = px.line(data, x="Date", y="Profit")
st.plotly_chart(fig)