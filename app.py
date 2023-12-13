import streamlit as st 
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/gauravyogesh/Chech_update/main/saved.csv')

st.dataframe(df)