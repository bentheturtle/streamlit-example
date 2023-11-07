import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.text_area("Form text")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
