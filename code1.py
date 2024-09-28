import streamlit as st
import pandas as pd
import plotly.express as px

df['Posted_date'] = pd.to_datetime(df['Posted_date'])
prices_month_mean = df[["Posted_date", "Rent"]].groupby("Posted_date")["Rent"].mean().reset_index()
fig = px.line(prices_month_mean, x='Posted_date', y="Rent", color_discrete_sequence=["darkolivegreen"], title="Giá Thuê Nhà Theo Thời Gian")

fig.update_layout(
    title_font=dict(color="darkolivegreen"),
    xaxis_title="Ngày Đăng",
    yaxis_title="Giá Thuê (triệu VND)",
    font=dict(
        family="serif",
        size=14,
        color="darkolivegreen"))

st.plotly_chart(fig, use_container_width=True)
