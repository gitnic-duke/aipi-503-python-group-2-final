"""
AIPI 503: Stock Quote Fetcher
=================================================
This module provides functions that interact and retrieve data 
from the Finnhub API.

    - get_stock_quote(symbol): displays current price, change, high,
      low, open, and previous close data, and displays in graph
    - get_company_news(symbol): displays up to 3 of the latest news stories
        with images and provides link to the story webpages
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
    return data["pc"], data["c"] #to calculate returns

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

    column_number = len(data)

    # Troubleshoot Columns
    #st.write(f"Column Number:", {column_number})
    #st.write(data)

    if column_number == 0:
        st.header("No News Available. Check again tomorrow.")

    elif column_number >= 1:
        columns = st.columns(column_number)
        for col in columns:
            if data[columns.index(col)]['image'] == "":
                pass
            else:
                st.image(
                data[columns.index(col)]['image'],
                use_container_width=True
                )
            st.link_button(data[columns.index(col)]['headline'], data[columns.index(col)]['url'])
            if columns.index(col) > 3:
                break
        
