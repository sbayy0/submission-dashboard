import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("dashboard/main_data.csv")

# Judul Dashboard
st.title("Dashboard Analisis Data")

# Menampilkan beberapa baris pertama data
st.subheader("Data Awal")
st.write(df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.write("Selamat datang di dashboard ini!")
