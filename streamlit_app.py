"""
AIPI 503: group project(Hasan Al-Quaid, Raul Cepin, Mihir Kosuri, Caleb McNeill, Nicholas Wang, Daniel Yaari)
=================================================
We have created a stocks streamlit page
    - Uses the Finnhub API
    - Stock Day Data Button: when selected, displays the stock quote table, graph, and stock returns data
    - Company News Button: when selected, displays the top 3 latest news stories with images and links
    - ADD ANY FEATURES YOU HAVE IMPLEMENTED HERE 
    
"""

import streamlit as st
import API
from day_returns import calculate_returns
import pandas as pd

def display_stock_day_data(symbol):
    """
    Retrieves the current stock quote for a given ticker symbol,
    created a bar chart of the data as well as a table of the open/high/low/current/prev close

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    data = API.get_stock_quote(symbol)
    
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
    previous_close = data["pc"]
    current_price = data["c"]
    total_return, percent_return = calculate_returns(previous_close,current_price) #Daniel's Feature

    st.subheader("Stock Returns")

    st.write(f"Previous Close: ${previous_close:.2f}")
    st.write(f"Current Price: ${current_price:.2f}")
    st.write(f"Price Change: ${total_return:.2f}")
    st.write(f"Percentage Return: {percent_return:.2f}%")

def display_company_news(symbol):
    """
    Retrieves link to latest Company news data from Finnhub and displays as a selector button with retreived image.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    data = API.get_company_news(symbol)
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

def main():
    st.title("Welcome to the Stock Market App")
    st.subheader("Track stock prices, view company info, and stay on top of the market, all in one place:")
    ticker = st.text_input("Which stock ticker would like to see?")

    if st.button("Stock Day Data"):
        display_stock_day_data(ticker)
        
    if st.button("Company News"):
        display_company_news(ticker)




if __name__ == "__main__":
    main()
