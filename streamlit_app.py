import pandas as pd
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/gauravyogesh/Track/main/saved.csv')
st.dataframe(df)