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
    data=pd.read_csv("Output.csv")
    return data

st. set_page_config(layout="wide")
st.title('US Bitcoin Market Analysis- Bitcoin, Litcoin & Etherium')

#st.title('-------------------------------------------------------------------------------')
fig_open = px.line(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Open_Gold','Open_dollar','Open_sap500'],
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

fig_close = px.line(load_data(),x='Date',y=['Close_Bitcoin','Close_Litcoin','Close_Etherium','Close_Gold','Close_dollar','Close_sap500'],
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


fig_low = px.line(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','Low_Gold','Low_dollar','Low_sap500'],
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


fig_high = px.line(load_data(),x='Date',y=['High_Bitcoin','High_Litcoin','High_Etherium','High_Gold','High_dollar','High_sap500'],
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


fig_ac = px.line(load_data(),x='Date',y=['Adj Close_Bitcoin','Adj Close_Litcoin','Adj Close_Etherium','Adj Close_Gold','Adj Close_dollar','Adj Close_sap500'],
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


fig_vol = px.line(load_data(),x='Date',y=['Volume_Bitcoin','Volume_Litcoin','Volume_Etherium','Volume_Gold','Volume_dollar','Volume_sap500'],
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
st.subheader('- The Digital currencies showed exponential increase from September 2020 and showed maximum in April 2021 except for all aspects, except for Volume.')
st.subheader('- According to analysis, Bitcoin showed better performance in all the aspects.')
st.subheader('- The graphs show that the Bitcoin mainly emerged into the market from January 2018, while others showed slow increase in trend.')
st.subheader('- There was a dip in all the currencies during March 2020 to May 2020 due to Covid-19 Pandemic. But, soon after that the market seemed to recover at a faster pace.')
st.subheader('- Below are the interactive graphs and the comparison between the currencies.')
st.header('Comparison of Open for the currencies')
st.plotly_chart(fig_open, use_container_width=True)
st.subheader('As seen above, the Open price for Bitcoin was below Gold and S&P500 till May 2017, after which it should gradual and consistent increase in the Open price, which moreover grew exponentially after end of 2020')
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
st.subheader('- The volume of Gold was majorly being sold in the months November, Januray, March, May and July')
st.subheader('- Out of all the Bitcoins, we can see that Bitcoin was at the maximum volume traded comparatively in the month of February 2021 with the volume of 350.96 billion.')
st.subheader('- Volume of dollar is zero throughout')