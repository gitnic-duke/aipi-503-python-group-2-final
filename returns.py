import pandas as pd

def calculate_returns(df: DataFrame):
    """Calculates the the total and percentage return for a stock over a period

    Requirements for Hasan:
    1) Be a pandas df
    2) Contain a row of stock price data
    3) Contain a column names "Close"
    4) Be order chronologically from oldest to most recent date
    ex)
    Date         Close
    2026-01-01    100.00
    2026-01-02    105.00
    2026-01-03    110.00
    """

    if df.empty:
        raise ValueError("DataFrame is empty")

    if "Close" not in df.columns:
        raise ValueError("Missing 'Close' column")

    start_price = df["Close"].iloc[0] 
    end_price = df["Close"].iloc[-1]

    total_return = end_price - start_price

    percent_return = (
        ((total_return) / (start_price)) * 100
    )

    return total_return, percent_return