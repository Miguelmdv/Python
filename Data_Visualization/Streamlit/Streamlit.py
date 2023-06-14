import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(".../Kaggle_Data/vgsales.csv")

fig = px.scatter(
  data_frame=df, x="Year", y="Global_Sales")

st.plotly_chart(fig)