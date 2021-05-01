#!/usr/bin/env python
# coding: utf-8

# ## The currencies on which the analysis has been done is Bitcoin, Gold, Dollar and S&P500.

# # 1. Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
from chart_studio import plotly
import plotly.express as px


# # 2. Reading Files

# In[2]:


bitcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\bitcoin.csv")
litcoin = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\litcoin.csv")
eth = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\etherium.csv")
gold = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\gold.csv")
dollar = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\dollar.csv")
sap500 = pd.read_csv(r"C:\Users\Aniket.Rele\Desktop\upwork\data\data\S&P500.csv")


# In[3]:


bitcoin.dropna(inplace=True)
litcoin.dropna(inplace=True)
eth.dropna(inplace=True)
gold.dropna(inplace=True)
dollar.dropna(inplace=True)
sap500.dropna(inplace=True)


# In[4]:


bitcoin.shape, litcoin.shape, eth.shape, gold.shape, dollar.shape, sap500.shape


# # 3. Converting Date columns to Datetime

# In[5]:


bitcoin['Date'] = pd.to_datetime(bitcoin['Date'])
litcoin['Date'] = pd.to_datetime(litcoin['Date'])
eth['Date'] = pd.to_datetime(eth['Date'])
gold['Date'] = pd.to_datetime(gold['Date'])
dollar['Date'] = pd.to_datetime(dollar['Date'])
sap500['Date'] = pd.to_datetime(sap500['Date'])


# In[6]:


print('Start Date for Bitcoin' , bitcoin['Date'].min().strftime('%d-%m-%Y'))
print('Start Date for Litcoin' , litcoin['Date'].min().strftime('%d-%m-%Y'))
print('Start Date for Etherium' , eth['Date'].min().strftime('%d-%m-%Y'))
print('Start Date for Gold' , gold['Date'].min().strftime('%d-%m-%Y'))
print('Start Date for Dollar' , dollar['Date'].min().strftime('%d-%m-%Y'))
print('Start Date for S&P500' , sap500['Date'].min().strftime('%d-%m-%Y'))


# In[7]:


print('End Date for Bitcoin' , bitcoin['Date'].max().strftime('%d-%m-%Y'))
print('End Date for Litcoin' , litcoin['Date'].max().strftime('%d-%m-%Y'))
print('End Date for Etherium' , eth['Date'].max().strftime('%d-%m-%Y'))
print('End Date for Gold' , gold['Date'].max().strftime('%d-%m-%Y'))
print('End Date for Dollar' , dollar['Date'].max().strftime('%d-%m-%Y'))
print('End Date for S&P500' , sap500['Date'].max().strftime('%d-%m-%Y'))


# - From the above 2 cells we notice that the start date for all the Bitcoins and Currencies is from 1st April 2016 and end date   is 31st March 2021, except for Bitcoins which has 1st April 2021 (A day more than the currencies)

# - Converting the String columns of S&P500 dataset to float columns.

# In[8]:


cols = ['Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']
for col in cols:
    sap500[col] = sap500[col].str.replace(",","")


# In[9]:


sap500[['Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']] = sap500[['Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']].apply(pd.to_numeric)


# ## P1. Plotting all variables for Bitcoin

# In[10]:


fig_bit = px.area(bitcoin,x='Date',y=['Open','High','Low','Close','Adj Close','Volume'])
fig_bit.update_xaxes(
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
fig_bit.show()


# ## P2. Plotting all variables for Litcoin

# In[11]:


fig_lit = px.area(litcoin,x='Date',y=['Open','High','Low','Close','Adj Close','Volume'])
fig_lit.update_xaxes(
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
fig_lit.show()


# ## P3. Plotting all variables for Etherium

# In[12]:


fig_eth = px.area(eth,x='Date',y=['Open','High','Low','Close','Adj Close','Volume'])
fig_eth.update_xaxes(
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
fig_eth.show()


# ## P4. Plotting all variables for Gold

# In[13]:


fig_gold = px.area(gold,x='Date',y=['Open','High','Low','Close','Adj Close','Volume'])
fig_gold.update_xaxes(
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
fig_gold.show()


# ## P5. Plotting all variables for Dollar

# In[14]:


fig_dollar = px.histogram(dollar,x='Date',y=['Open','High','Low','Close','Adj Close','Volume'],nbins=10000)
fig_dollar.update_xaxes(
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
fig_dollar.show()


# ## P6. Plotting all variables for S&P500

# In[15]:


fig_sap = px.area(sap500,x='Date',y=['Open','High','Low','Close*','Adj Close**','Volume'])
fig_sap.update_xaxes(
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
fig_sap.show()


# # 4. Merging the datasets to analyse the graphs

# In[16]:


df1 = pd.merge(left = bitcoin,right = gold,how='inner',on=['Date'])


# In[17]:


df1 = df1.rename(columns={'Open_x':'Open_Bitcoin','Open_y':'Open_Gold',
                         'High_x':'High_Bitcoin','High_y':'High_Gold',
                         'Low_x':'Low_Bitcoin','Low_y':'Low_Gold',
                         'Close_x':'Close_Bitcoin','Close_y':'Close_Gold',
                         'Adj Close_x':'Adj Close_Bitcoin','Adj Close_y':'Adj Close_Gold',
                         'Volume_x':'Volume_Bitcoin','Volume_y':'Volume_Gold'})


# In[18]:


df2 = pd.merge(left = dollar,right = sap500,how='inner',on=['Date'])


# In[19]:


df2 = df2.rename(columns={'Open_x':'Open_dollar','Open_y':'Open_sap500',
                         'High_x':'High_dollar','High_y':'High_sap500',
                         'Low_x':'Low_dollar','Low_y':'Low_sap500',
                         'Close':'Close_dollar','Close*':'Close_sap500',
                         'Adj Close':'Adj Close_dollar','Adj Close**':'Adj Close_sap500',
                         'Volume_x':'Volume_dollar','Volume_y':'Volume_sap500'})


# In[20]:


df3 = pd.merge(left = litcoin,right = eth,how='inner',on=['Date'])


# In[21]:


df3 = df3.rename(columns={'Open_x':'Open_Litcoin','Open_y':'Open_Etherium',
                         'High_x':'High_Litcoin','High_y':'High_Etherium',
                         'Low_x':'Low_Litcoin','Low_y':'Low_Etherium',
                         'Close_x':'Close_Litcoin','Close_y':'Close_Etherium',
                         'Adj Close_x':'Adj Close_Litcoin','Adj Close_y':'Adj Close_Etherium',
                         'Volume_x':'Volume_Litcoin','Volume_y':'Volume_Etherium'})


# In[22]:


df4 = pd.merge(left = df1,right = df2,how='inner',on=['Date'])


# In[23]:


df = pd.merge(left = df4,right = df3,how='inner',on=['Date'])


# In[24]:


df.shape


# ## C1. Comparison of Open for the currencies

# In[47]:


fig_open = px.area(df,x='Date',y=['Open_Bitcoin','Open_Litcoin','Open_Etherium','Open_Gold','Open_dollar','Open_sap500'],
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
fig_open.show()


# ## C2. Comparison of Close for the currencies

# In[48]:


fig_close = px.area(df,x='Date',y=['Close_Bitcoin','Close_Litcoin','Close_Etherium','Close_Gold','Close_dollar','Close_sap500'],
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
fig_close.show()


# ## C3. Comparison of Low for the currencies

# In[49]:


fig_low = px.area(df,x='Date',y=['Low_Bitcoin','Low_Litcoin','Low_Etherium','Low_Gold','Low_dollar','Low_sap500'],
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
fig_low.show()


# ## C4. Comparison of High for the currencies

# In[50]:


fig_high = px.area(df,x='Date',y=['High_Bitcoin','High_Litcoin','High_Etherium','High_Gold','High_dollar','High_sap500'],
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
fig_high.show()


# ## C5. Comparison of Adjacent Close for the currencies

# In[51]:


fig_ac = px.area(df,x='Date',y=['Adj Close_Bitcoin','Adj Close_Litcoin','Adj Close_Etherium','Adj Close_Gold','Adj Close_dollar','Adj Close_sap500'],
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
fig_ac.show()


# ## C6. Comparison of Volume for the currencies

# In[52]:


fig_vol = px.area(df,x='Date',y=['Volume_Bitcoin','Volume_Litcoin','Volume_Etherium','Volume_Gold','Volume_dollar','Volume_sap500'],
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
fig_vol.show()


# - The Bitcoin currencies showed drastic increase from September 2020 and showed maximum in April 2021 except for Volume.
# - According to analysis, S&P500 showed better performance in all the aspects.
# - Out of all the Bitcoins, we can see that Etherium was at the maximum volume traded comparatively in the month of February 2021 with the volume of 31.436 billion.
