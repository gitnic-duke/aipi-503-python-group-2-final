"""
AIPI 503: Stock Quote Fetcher
=================================================
This module provides functions that interact and retrieve data 
from the Finnhub API.

    - get_stock_quote(symbol): displays current price, change, high,
      low, open, and previous close data, and displays in graph
    - ADD ANY ADDITIONAL FUNCTIONS HERE
"""
import os
import requests
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
load_dotenv()
API_KEY = os.getenv("STOCK_API_KEY")

def get_stock_quote(symbol):
    """
    Retrieves the current stock quote for a given ticker symbol,
    created a bar chart of the data as well as a table of the open/high/low/current/prev close

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/quote"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    
    col1, col2 = st.columns(2)
    chart_data = pd.DataFrame({
    "Price": [data['o'], data['h'], data['l'], data['c'], data['pc']]
    }, index=["Open", "High", "Low", "Current", "Prev Close"])

    with col1:
        st.subheader(f"{symbol}: Stock Data for Today")
        st.bar_chart(chart_data)
    with col2:
        st.subheader(f"{symbol}: Stock Data Table")
        st.dataframe(chart_data)

def get_company_news(symbol):
    """
    Retrieves link to latest Company news data from Finnhub and displays as a selector button with retreived image.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/company-news"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            data[0]['image'],
            use_container_width=True
            )
        st.link_button(data[0]['headline'], data[0]['url'])
    with col2:
        st.image(
            data[1]['image'],
            use_container_width=True
            )
        st.link_button(data[1]['headline'], data[1]['url'])
    with col3:
        st.image(
            data[2]['image'],
            use_container_width=True
            )
        st.link_button(data[2]['headline'], data[2]['url'])
    return data["pc"], data["c"] #to calculate returns
