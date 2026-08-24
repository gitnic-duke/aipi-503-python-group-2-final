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
2. Create a .streamlit/secrets.toml file with the content STOCK_API_KEY="{your_API_key}"
3. Save the file
```bash
### Usage
streamlit run streamlit_app.py