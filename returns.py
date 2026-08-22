import pandas as pd

def calculate_returns(df: pd.DataFrame):
    """Calculates the the total and percentage return for a stock over a period"""

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