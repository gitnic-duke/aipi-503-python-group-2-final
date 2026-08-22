# aipi-503-python-group-2-final
AIPI 503 final project for group 2 (Hasan Al-Quaid, Raul Cepin, Mihir Kosuri, Caleb McNeill, Nicholas Wang, Daniel Yaari)

### Prerequisites
- Python 3.9+

### Installation
```bash
GitHub repo: "aipi-503-python-group-2-final"
git clone https://github.com/gitnic-duke/aipi-503-python-group-2-final.git
cd aipi-503-python-group-2-final
python -m venv .venv
.venv/Scripts/activate.ps1 # Windows or
source .venv/bin/activate # Mac
pip install -r requirements.txt

### Usage
```
### API Key set up
1. Copy your API key from Finnhub.
If you don't have one, create one on https://finnhub.io/
2. Create a .streamlit/secrets.toml file with the content OPENWEATHER_API_KEY="{your_API_key}"
3. Save the file
```bash
streamlit run streamlit_app.py

### Documentation
.env #Stock API
.gitignore # .env (Secure keys)