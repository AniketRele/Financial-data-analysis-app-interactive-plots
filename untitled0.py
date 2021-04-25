# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:25:26 2021

@author: aniket.rele
"""

import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from chart_studio import plotly
import plotly.express as px


@st.cache
def load_data():
    data=pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\Output.csv")
    return data

st. set_page_config(layout="wide")
st.title('US Bitcoin Market Analysis- Bitcoin, Litcoin & Etherium')

#st.title('-------------------------------------------------------------------------------')
fig_open = px.area(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Open_Gold','Open_dollar','Open_sap500'],
                  labels={'Date':'Date', 'value':'Open'}, height=700)
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
                   labels={'Date':'Date', 'value':'Close'}, height=700)
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
                 labels={'Date':'Date', 'value':'Low'}, height=700)
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
                  labels={'Date':'Date', 'value':'High'}, height=700)
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
                labels={'Date':'Date', 'value':'Adjacent Close'}, height=700)
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
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
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

st.subheader('From the data we notice that the start date for all the Digital Currencies and Currencies is from 1st April 2016 and end date is 31st March 2021, except for Digital Currencies which has 1st April 2021 (A day more than the currencies)')
st.subheader('- The Bitcoin currencies showed drastic increase from September 2020 and showed maximum in April 2021 except for Volume.')
st.subheader('- According to analysis, S&P500 showed better performance in all the aspects.')
st.subheader('- The graphs shows that the Digital Currencies mainly got into the market from January 2018.')
st.subheader('- There was a dip in all the currencies during March 2020 to May 2020 due to Covid-19 Pandemic')
st.subheader('- All the features were fluctuating at the similar timespan with similar trend in the data.')
st.subheader('- Below are the interactive graphs and the comparison between the currencies.')
st.header('Comparison of Open for the currencies')
st.plotly_chart(fig_open, use_container_width=True)
st.subheader('There was approximately 2 times increase in Open, Close, Low, High and Adjacent Close within 3 years from Jan 2018 to Jan 2021')
st.header('Comparison of Close for the currencies')
st.plotly_chart(fig_close, use_container_width=True)
st.header('Comparison of Low for the currencies')
st.plotly_chart(fig_low, use_container_width=True)
st.header('Comparison of High for the currencies')
st.plotly_chart(fig_high, use_container_width=True)
st.header('Comparison of Adjacent Close for the currencies')
st.plotly_chart(fig_ac, use_container_width=True)
st.header('Comparison of Volume for the currencies')
st.plotly_chart(fig_vol, use_container_width=True)
st.subheader('- The volume of Gold was majorly being sold in the months November, Januray, March, May and June')
st.subheader('- Out of all the Bitcoins, we can see that Etherium was at the maximum volume traded comparatively in the month of February 2021 with the volume of 31.436 billion.')
st.subheader('- Volume of dollar is zero throughout')