import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import warnings

st.title("Data Summarizer Pandas Profiling and GX")
st.sidebar.title("Settings")

uploaded_file = st.sidebar.file_uploader("Upload a CSV or XLSX file", type=["csv", "xls"])

data_type = st.sidebar.radio("Select Data Type:", ("Origination Data", "Monthly Performance Data"))

if uploaded_file is not None:
    
    if data_type == "Origination Data":
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    else:
        df = pd.read_excel(uploaded_file, encoding='utf-8', engine='openpyxl')

    st.subheader("Data Preview:")
    st.write(df)

   
    st.subheader("Pandas Profiling Report:")
    profile = ProfileReport(df, explorative=True)
    st.write(profile.to_widgets())


