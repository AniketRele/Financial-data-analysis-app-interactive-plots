# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:25:26 2021

@author: aniket.rele
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from chart_studio import plotly
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data=pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\Output.csv")
    return data

st.title('US Bitcoin Market Analysis- Bitcoin, Litcoin & Etherium')
st.title('-----------------------------------------------')

fig_open = px.area(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Open_Gold','Open_dollar','Open_sap500'],
                  labels={'Date':'Date', 'value':'Open'},title='Comparison of Open for the currencies')
fig_open.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig_close = px.area(load_data(),x='Date',y=['Close_Bitcoin','Close_Litcoin','Close_Etherium','Close_Gold','Close_dollar','Close_sap500'],
                   labels={'Date':'Date', 'value':'Close'},title='Comparison of Close for the currencies')
fig_close.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig_low = px.area(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','Low_Gold','Low_dollar','Low_sap500'],
                 labels={'Date':'Date', 'value':'Low'},title='Comparison of Low for the currencies')
fig_low.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig_high = px.area(load_data(),x='Date',y=['High_Bitcoin','High_Litcoin','High_Etherium','High_Gold','High_dollar','High_sap500'],
                  labels={'Date':'Date', 'value':'High'},title='Comparison of High for the currencies')
fig_high.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig_ac = px.area(load_data(),x='Date',y=['Adj Close_Bitcoin','Adj Close_Litcoin','Adj Close_Etherium','Adj Close_Gold','Adj Close_dollar','Adj Close_sap500'],
                labels={'Date':'Date', 'value':'Adjacent Close'},title='Comparison of Adjacent Close for the currencies')
fig_ac.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig_vol = px.area(load_data(),x='Date',y=['Volume_Bitcoin','Volume_Litcoin','Volume_Etherium','Volume_Gold','Volume_dollar','Volume_sap500'],
                 labels={'Date':'Date', 'value':'Volume'}, title='Comparison of Volume for the currencies')
fig_vol.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


st.plotly_chart(fig_open, use_container_width=True)
st.plotly_chart(fig_close, use_container_width=True)
st.plotly_chart(fig_low, use_container_width=True)
st.plotly_chart(fig_high, use_container_width=True)
st.plotly_chart(fig_ac, use_container_width=True)
st.plotly_chart(fig_vol, use_container_width=True)