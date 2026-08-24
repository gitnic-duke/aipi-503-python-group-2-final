"""
AIPI 503: group project(Hasan Al-Quaid, Raul Cepin, Mihir Kosuri, Caleb McNeill, Nicholas Wang, Daniel Yaari)
=================================================
We have created a stocks streamlit page
    - Uses the Finnhub API
    - Stock Day Data Button: displays the stock quote table, graph, and stock returns data
    - Company News Button: displays the top 3 latest news stories with images and links
    - Expert Recommendations Button: displays the most recommended action on the stock by experts with a pie chart showing all recommendations
    - Company Profile Button: displays company logo, industry, market cap, IPO date, and website link
    
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
    Retrives expert recommendations for a given ticker symbol for this month.
    Displays most recommended action and pie chart of all recommendations

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    if not symbol:
        st.subheader("Invalid Stock Ticker")
        return

    if API.get_recommendations(symbol) == []:
        st.subheader("Invalid Stock Ticker")
        return

    # Get and process recommendation data
    current_recommendations = API.get_recommendations(symbol)[0]
    timestamp = current_recommendations["period"]
    recommendation_categories = ["strongBuy", "buy", "hold", "sell", "strongSell"]
    recommendation_counts_dict = {k: current_recommendations[k] for k in recommendation_categories}
    total_recommendations = sum(recommendation_counts_dict.values())

    # Display most recommended action
    st.subheader(f"Expert recommendations for {symbol} on {timestamp}")
    most_recommended_action, most_recommended_action_count = max(recommendation_counts_dict.items(), key=lambda item: item[1])
    st.write(f"Most experts ({most_recommended_action_count}/{total_recommendations}) recommend this stock as a {most_recommended_action}.")

    # Pie chart for recommendation distributions
    non_zero_recommendation_counts_dict = {k: v for k, v in recommendation_counts_dict.items() if v != 0} # remove options with 0 recommendations to clean up chart
    fig, ax = plt.subplots()
    ax.pie(
        non_zero_recommendation_counts_dict.values(),
        labels=non_zero_recommendation_counts_dict.keys(),
        autopct=lambda pct: f'{int(pct * total_recommendations / 100)} ({pct:.1f}%)' # show percentage and number of recommendations
    )
    ax.set_title(f"Expert Recommendations for {symbol} on {timestamp}")
    st.pyplot(fig)

    # Display non recommended actions
    non_selected_options = []
    for category in recommendation_categories:
        if category not in non_zero_recommendation_counts_dict.keys():
            non_selected_options.append(category)
    if non_selected_options:
        st.write(f"0 experts recommended {symbol} as {', '.join(non_selected_options)}")

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

def display_company_profile(symbol):
    """
    Displays company profile information for a given ticker symbol.

    Parameters:
        symbol (str): Stock ticker symbol.
    """
    data = API.get_company_profile(symbol)

    if not data:
        st.warning(f"No company profile found for '{symbol}'. Check the ticker symbol.")
        return

    col1, col2 = st.columns([1, 3])

    with col1:
        if data.get("logo"):
            st.image(data["logo"], width=100)

    with col2:
        st.subheader(data.get("name", symbol))
        st.write(f"**Industry:** {data.get('finnhubIndustry', 'N/A')}")
        st.write(f"**Exchange:** {data.get('exchange', 'N/A')}")
        st.write(f"**Country:** {data.get('country', 'N/A')}")

    market_cap = data.get("marketCapitalization", 0)
    if market_cap >= 1_000_000:
        cap_display = f"${market_cap / 1_000_000:.2f} Trillion"
    elif market_cap >= 1_000:
        cap_display = f"${market_cap / 1_000:.2f} Billion"
    else:
        cap_display = f"${market_cap:.2f} Million"

    st.write(f"**Market Cap:** {cap_display}")
    st.write(f"**IPO Date:** {data.get('ipo', 'N/A')}")

    if data.get("weburl"):
        st.link_button("Company Website", data["weburl"])

def main():
    st.title("Welcome to the Stock Market App")
    st.subheader("Track stock prices, view company info, and stay on top of the market, all in one place:")
    ticker = st.text_input("Which stock ticker would you like to see?")
    st.info("Note: This app is intended to work only for company stocks, mutual fund tickers will not work")
    ticker = ticker.upper()
    if st.button("Stock Day Data"):
        display_stock_day_data(ticker)
        
    if st.button("Company News"):
        display_company_news(ticker)

    if st.button("Expert Recommendations"):
        display_expert_recommendations(ticker)
    
    if st.button("Company Profile"):
        display_company_profile(ticker)



if __name__ == "__main__":
    main()
