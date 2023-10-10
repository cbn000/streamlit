import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.write("Hello World!")

a = st.sidebar.radio('Select one:', [1, 2])


col1, col2 = st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

st.checkbox("Yes")
st.multiselect("Buy", ["milk", "apple", "potatoes"])


nrows = 100
nrows = st.slider("Pick a number", 0, 1000)

st.write(nrows)

st.time_input("Meeting time")


@st.cache_data
def load_data(DATA_URL_, nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data.rename(columns={'Lat': 'LAT', 'Lon': 'LON'})
    return data


DATA_URL = (
    'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

data = load_data(DATA_URL, nrows)


# st.bar_chart(data)
st.dataframe(data)
st.map(data.loc[:, ['LAT', 'LON']])

df = px.data.tips()
fig = px.histogram(data, x="LAT")

st.plotly_chart(fig)
