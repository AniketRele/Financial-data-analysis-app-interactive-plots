import streamlit as st
import pandas as pd
from chart_studio import plotly
import plotly.express as px

@st.cache
def load_data():
    data=pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\Output.csv")
    return data
def gold():
    gold = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\gold.csv")
    return gold
def bitcoin():
    bitcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\bitcoin.csv")
    return bitcoin
def litcoin():
    litcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\litcoin.csv")
    return litcoin
def eth():
    eth = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\etherium.csv")
    return eth
def dollar():
    dollar = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\dollar.csv")
    return dollar
def sap500():
    sap500 = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\S&P500.csv")
    return sap500

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

fig_go3 = px.line(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Close_Bitcoin','Close_Litcoin','Close_Etherium','Open_Gold','Close_Gold','Open_dollar','Close_dollar','Open_sap500','Close_sap500'],
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
fig_go3.update_xaxes(
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

#fig_do3 = px.line(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Close_Litcoin','Close_Litcoin','Close_Bitcoin','Open_dollar','Close_dollar'],
#                 labels={'Date':'Date', 'value':'Volume'}, height=700)
#fig_do3.update_xaxes(
#    rangeslider_visible=True,
#    rangeselector=dict(
#        buttons=list([
#            dict(count=1, label="1m", step="month", stepmode="backward"),
#            dict(count=6, label="6m", step="month", stepmode="backward"),
#            dict(count=1, label="YTD", step="year", stepmode="todate"),
#            dict(count=1, label="1y", step="year", stepmode="backward"),
#            dict(step="all")
#        ])
#    )
#)

#fig_so3 = px.line(load_data(),x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Close_Etherium','Close_Litcoin','Close_Bitcoin','Open_sap500','Close_sap500'],
#                 labels={'Date':'Date', 'value':'Volume'}, height=700)
#fig_so3.update_xaxes(
#    rangeslider_visible=True,
#    rangeselector=dict(
#        buttons=list([
#            dict(count=1, label="1m", step="month", stepmode="backward"),
#            dict(count=6, label="6m", step="month", stepmode="backward"),
#            dict(count=1, label="YTD", step="year", stepmode="todate"),
#            dict(count=1, label="1y", step="year", stepmode="backward"),
#            dict(step="all")
#        ])
#    )
#)


fig_go4 = px.line(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','High_Litcoin','High_Litcoin','High_Bitcoin','Low_Gold','High_Gold'],
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
fig_go4.update_xaxes(
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

fig_do4 = px.line(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','High_Litcoin','High_Litcoin','High_Bitcoin','Low_dollar','High_dollar'],
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
fig_do4.update_xaxes(
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

fig_so4 = px.line(load_data(),x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','High_Litcoin','High_Litcoin','High_Bitcoin','Low_sap500','High_sap500'],
                 labels={'Date':'Date', 'value':'Volume'}, height=700)
fig_so4.update_xaxes(
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

fig_bit = px.scatter_matrix(bitcoin())
fig_lit = px.scatter_matrix(litcoin())
fig_eth = px.scatter_matrix(eth())
fig_go = px.scatter_matrix(gold())
fig_do = px.scatter_matrix(dollar())
fig_sap = px.scatter_matrix(sap500())

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
st.header('Comparison of Open and Close for Gold, Dollar and S&P500 with the Digital Currencies')
st.plotly_chart(fig_go3, use_container_width=True)
#st.header('Comparison of Open and Close for Dollar with the Digital Currencies')
#st.plotly_chart(fig_do3, use_container_width=True)
#st.header('Comparison of Open and Close for S&P500 with the Digital Currencies')
#st.plotly_chart(fig_so3, use_container_width=True)
#st.header('Comparison of Low and High for Gold with the Digital Currencies')
#st.plotly_chart(fig_go4, use_container_width=True)
#st.header('Comparison of Low and High for Dollar with the Digital Currencies')
#st.plotly_chart(fig_do4, use_container_width=True)
#st.header('Comparison of Low and High for S&P500 with the Digital Currencies')
#st.plotly_chart(fig_so4, use_container_width=True)
#st.header('Featurewise comparison plot for Bitcoin')
#st.plotly_chart(fig_bit, use_container_width=True)
#st.header('Featurewise comparison plot for Litcoin')
#st.plotly_chart(fig_lit, use_container_width=True)
#st.header('Featurewise comparison plot for Etherium')
#st.plotly_chart(fig_eth, use_container_width=True)
#st.header('Featurewise comparison plot for Gold')
#st.plotly_chart(fig_go, use_container_width=True)
#st.header('Featurewise comparison plot for Dollar')
#st.plotly_chart(fig_do, use_container_width=True)
#st.header('Featurewise comparison plot for S&P500')
#st.plotly_chart(fig_sap, use_container_width=True)