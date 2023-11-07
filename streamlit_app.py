import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

uploaded_file = st.file_uploader("Choose a file")
df = pd.DataFrame({'name': ['ben'], 'assosiation': ['me'], 'is_cool': [True]})
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)




csv = convert_df(edited_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='df.csv',
    mime='text/csv',
)

