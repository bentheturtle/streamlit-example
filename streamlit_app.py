import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

df = pd.Dataframe(columns=['name', 'assosiation', 'is cool?'])
with st.form("my_form"):
   st.write("Inside the form")
   name = st.text_area("name")
   ass = st.text_area("assosiation")
   cooling = st.checkbox("is cool?")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       df.loc[len(df.index)] = [name, ass, cooling] 

st.write(df)
