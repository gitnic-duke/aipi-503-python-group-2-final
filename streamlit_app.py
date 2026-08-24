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
import matplotlib.pyplot as plt
import pandas as pd


def display_stock_day_data(symbol):
    """
    Retrieves the current stock quote for a given ticker symbol,
    created a bar chart of the data as well as a table of the open/high/low/current/prev close

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    data = API.get_stock_quote(symbol)
    if data['c'] == 0:
        st.subheader("Invalid Stock Ticker")
        return
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

    display_price_alert(symbol, percent_return)

def display_company_news(symbol):
    """
    Retrieves link to latest Company news data from Finnhub and displays as a selector button with retreived image.

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    data = API.get_company_news(symbol)
    column_number = len(data)

    # Troubleshoot Columns
    #st.write(f"Column Number:", {column_number})
    #st.write(data)

    if column_number == 0:
        st.header("No News Available. Check again tomorrow.")

    elif column_number >= 1:
        columns = st.columns(column_number)
        for col in columns:
            if "error" in data:
                st.subheader(data["error"])
                break
            elif data[columns.index(col)]['image'] == "":
                pass
            else:
                st.image(
                data[columns.index(col)]['image'],
                use_container_width=True
                )
            st.link_button(data[columns.index(col)]['headline'], data[columns.index(col)]['url'])
            if columns.index(col) > 3:
                break

def display_expert_recommendations(symbol):
    """
    Retrives expert recommendations for a given ticker symbol for this month

    Parameters:
            symbol (str): Stock ticker symbol.
    """
    if API.get_recommendations(symbol) == []:
        st.subheader("Invalid Stock Ticker")
        return
    current_recommendations = API.get_recommendations(symbol)[0]
    # if current_recommendations.empty():
    #     st.subheader("Invalid Stock Ticker")
    #     return
    timestamp = current_recommendations["period"]
    recommendation_categories = ["strongBuy", "buy", "hold", "sell", "strongSell"]
    recommendation_counts_dict = {k: current_recommendations[k] for k in recommendation_categories}
    total_recommendations = sum(recommendation_counts_dict.values())
    st.subheader(f"Expert recommendations for {symbol} on {timestamp}")

    # Display most recommended action
    most_recommended_action, most_recommended_action_count = max(recommendation_counts_dict.items(), key=lambda item: item[1])
    st.write(f"Most experts ({most_recommended_action_count}/{total_recommendations}) recommend this stock as a {most_recommended_action}.")

    # Pie chart for recommendation distributions
    fig, ax = plt.subplots()
    ax.pie(
        recommendation_counts_dict.values(),
        labels=recommendation_counts_dict.keys(),
        autopct=lambda pct: f'{int(pct * total_recommendations / 100)} ({pct:.1f}%)' # show percentage and number of recommendations
    )
    ax.set_title(f"Expert Recommendations for {symbol} on {timestamp}")
    st.pyplot(fig)

def display_price_alert(symbol, percent_change):
    """
    Displays an alert if the stock's price change exceeds a specified threshold for the day.

    Parameters:
        symbol (str): Stock ticker symbol.
        percent_change (float): Percentage change in price from previous close.
    """
    threshold = 2.0
    if percent_change >= threshold:
        st.success(f"{symbol} is up {percent_change:.2f}% today")
    elif percent_change <= -threshold:
        st.error(f"{symbol} is down {abs(percent_change):.2f}% today")
    else:
        st.info(f"{symbol} is roughly flat today")

def main():
    st.title("Welcome to the Stock Market App")
    st.subheader("Track stock prices, view company info, and stay on top of the market, all in one place:")
    ticker = st.text_input("Which stock ticker would you like to see?")

    if st.button("Stock Day Data"):
        display_stock_day_data(ticker)
        
    if st.button("Company News"):
        display_company_news(ticker)

    if st.button("Expert Recommendations"):
        display_expert_recommendations(ticker)




if __name__ == "__main__":
    main()
