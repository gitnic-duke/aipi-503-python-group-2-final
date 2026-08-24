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
load_dotenv()
API_KEY = os.getenv("STOCK_API_KEY")

def get_stock_quote(symbol):
    """
    Retrieves the current stock quote for a given ticker symbol,

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/quote"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    return data

def get_company_news(symbol):
    """
    Retrieves link to latest Company news data from Finnhub.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/company-news"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    return data

def get_recommendations(symbol):
    """
    Retrives expert recommendations for a given ticker symbol.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/stock/recommendation"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def get_company_profile(symbol):
    """
    Retrieves the company profile for a given ticker symbol.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    url = "https://finnhub.io/api/v1/stock/profile2"
    params = {"symbol": symbol, "token": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    return data