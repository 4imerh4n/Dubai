import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Dubai.csv')
avg_rent_per_location = df.groupby('Location')['Rent'].mean().reset_index()


fig_treemap = px.treemap(
    avg_rent_per_location, 
    path=['Location'], 
    values='Rent', 
    title='Giá Thuê Trung Bình Theo Địa Điểm Cụ Thể',
    width=1200,
    height=600)
fig_treemap.layout.font = dict(family='serif', size=12)


st.title("Treemap Example")
st.plotly_chart(fig_treemap)
