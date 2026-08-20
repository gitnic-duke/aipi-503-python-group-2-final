"""
AIPI 503: group project(Hasan Al-Quaid, Raul Cepin, Mihir Kosuri, Caleb McNeill, Nicholas Wang, Daniel Yaari)
=================================================
We have created a stocks streamlit page
    - Uses the Finnhub API
    - ADD ANY FEATURES YOU HAVE IMPLEMENTED HERE 
    
"""


import streamlit as st
import API

def main():
    ticker = st.text_input("Enter in the stock ticker that you would like to see:")
    if st.button("Stock Day Data"):
        API.get_stock_quote(ticker)

if __name__ == "__main__":
    st.title("Welcome to the Stock Market App")
    st.subheader("Track stock prices, view company info, and stay on top of the market, all in one place:")
    main()
