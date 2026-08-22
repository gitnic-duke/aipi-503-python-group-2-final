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

def main():
    ticker = st.text_input("Which stock ticker would like to see?")

    if st.button("Stock Day Data"):
        previous_close, current_price = API.get_stock_quote(ticker)
        total_return, percent_return = calculate_returns(previous_close,current_price) #Daniel's Feature

        st.subheader("Stock Returns")

        st.write(f"Previous Close: ${previous_close:.2f}")
        st.write(f"Current Price: ${current_price:.2f}")
        st.write(f"Price Change: ${total_return:.2f}")
        st.write(f"Percentage Return: {percent_return:.2f}%")
    if st.button("Company News"):
        API.get_company_news(ticker)




if __name__ == "__main__":
    st.title("Welcome to the Stock Market App")
    st.subheader("Track stock prices, view company info, and stay on top of the market, all in one place:")
    main()
