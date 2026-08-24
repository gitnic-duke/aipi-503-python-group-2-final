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
    if data['c'] == 0:
        print("Invalid Stock Ticker")
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
    column_number = len(data)
    if column_number == 0:
        print("No News Available. Check again tomorrow.")
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
    if data == []:
        print("Invalid Stock Ticker")
    return data

def main():
    print("Welcome to the Stock Market App")
    print("Track stock prices, view company info, and stay on top of the market, all in one place:")
    
    symbol = ""
    valid_symbol = False
    while valid_symbol !=True:
        symbol = input("Which stock ticker would you like to see? ")
        data = get_stock_quote(symbol)
        if data['c'] == 0:
            continue
        else:
           valid_symbol = True             

    stock_menu = """
    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    Exit
    """
    option = ""
    while option.lower() != "exit":
        option = input(stock_menu)
        if option == "1":
            print(get_stock_quote(symbol))
        elif option == "2":
            print(get_company_news(symbol))
        elif option == "3":
            print(get_recommendations(symbol))
        else:
            print("Entry is invalid")



if __name__ == "__main__":
    main()
