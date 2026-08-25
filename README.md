### aipi-503-python-group-2-final
AIPI 503 final project for Group 2: Hasan Al-Quaid, Raul Cepin, Mihir Kosuri, Caleb McNeill, Nicholas Wang, and Daniel Yaari.

### Project Overview

The app is an interactive stock market dashboard built using Python, Streamlit, and the Finnhub API provided. When activated, users can enter a stock ticker (i.e. AAPL) to view current market data, calculate daily stock returns, read recent company news, and view expert recommendations. This is an all-in-one place for asset analysis!

Some key features in the app include:
- Current stock price data and visualizations
- Daily price change and percentage return
- Stock price movement alerts
- Company news
- Expert buy, hold, and sell recommendations
- Company profile information

The project is deployed on https://aipi-503-python-group-2-final-j7pj4qxqirmlswef5hpwaf.streamlit.app/

![Stonks Image](https://i.ytimg.com/vi/if-2M3K1tqk/maxresdefault.jpg)

### Prerequisites
- Python 3.9+
- Git
- Finnhub API key

### Installation
```bash
GitHub repo: "aipi-503-python-group-2-final"
git clone https://github.com/gitnic-duke/aipi-503-python-group-2-final.git
cd aipi-503-python-group-2-final
python -m venv .venv
#### Windows
.venv/Scripts/activate.ps1
#### Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
```
### API Key set up
1. Copy your API key from Finnhub.
If you don't have one, create one on https://finnhub.io/
2. Create a .env file with the content STOCK_API_KEY="{your_API_key}"
3. Save the file
```bash
### Usage
streamlit run streamlit_app.py
```

### How to run locally
1. From the streamlit_app.py, simply run the following command:
```bash
streamlit run .\streamlit_app.py   
```
2. A page will automatically open in the browser of the streamlit page

### How to run CLI demo
1. From the API.py, simply run the file using the debugger, or you may run it directly from the terminal:
```bash
python API.py
```
2. And the terminal will start the program and prompt the user for an input:
```bash
Welcome to the Stock Market App
Track stock prices, view company info, and stay on top of the market, all in one place:
Which stock ticker would you like to see? 
```
Example of the output(with ```TSLA``` stock):
```bash
Which stock ticker would you like to see? TSLA

    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    4: Get Company Profile
    Exit
    1
{'c': 348.95, 'd': -13.91, 'dp': -3.8334, 'h': 363.24, 'l': 348.26, 'o': 361.41, 'pc': 362.86, 't': 1787601600}

    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    4: Get Company Profile
    Exit
    2
No News Available. Check again tomorrow.
[]

    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    4: Get Company Profile
    Exit
    3
[{'symbol': 'TSLA', 'period': '2026-08-01', 'strongBuy': 10, 'buy': 20, 'hold': 24, 'sell': 6, 'strongSell': 1}, {'symbol': 'TSLA', 'period': '2026-07-01', 'strongBuy': 9, 'buy': 20, 'hold': 24, 'sell': 6, 'strongSell': 1}, {'symbol': 'TSLA', 'period': '2026-06-01', 'strongBuy': 9, 'buy': 20, 'hold': 23, 'sell': 7, 'strongSell': 1}, {'symbol': 'TSLA', 'period': '2026-05-01', 'strongBuy': 9, 'buy': 20, 'hold': 24, 'sell': 7, 'strongSell': 1}]

    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    4: Get Company Profile
    Exit
    4
{'ticker': 'TSLA', 'name': 'Tesla Inc', 'country': 'US', 'currency': 'USD', 'estimateCurrency': 'USD', 'exchange': 'NASDAQ NMS - GLOBAL MARKET', 'ipo': '2010-06-29', 'marketCapitalization': 1378194.5819725988, 'logo': 'https://static2.finnhub.io/file/publicdatany/finnhubimage/stock_logo/TSLA.png', 'shareOutstanding': 3949.55, 'finnhubIndustry': 'Automobiles', 'phone': '15125168177', 'weburl': 'https://www.tesla.com/', 'floatingShare': 3245.62}

    Choose an option below:
    1: Get Stock Quote
    2: Get Company News
    3: Get Recommendations
    4: Get Company Profile
    Exit
    exit
```
