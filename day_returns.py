def calculate_returns(previous_close, current_price):
    """
    Calculates the total and percentage return from the
    previous closing price to the current stock price.
    """

    if previous_close <= 0: #Ensure correct data
        raise ValueError("Close must be greater than zero")

    total_return = current_price - previous_close

    percent_return = ((total_return / previous_close) * 100)

    return total_return, percent_return