import numpy as np
import pandas as pd
import streamlit as st

st.title("This is First Assignment!!!")
st.write("All the students do it for cloud computing!!")

data = pd.DataFrame(
    {'Names':["Hamoud","Ali","Abdullah","Hussain","Ahmed","Salman","Mohammad","Ibrahim"],
    "Age":[21,17,19,23,19,21,19,18]})

st.write("fallowing is student details")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=["a","b","c","d"]
)

st.bar_chart(chart_data)