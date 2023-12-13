import streamlit as st 
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/gauravyogesh/Track/main/saved.csv')

st.dataframe(df)