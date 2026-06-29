import requests

API_KEY = "DYJ6NHFO3EJI81D4"

def get_stock_data(symbol):
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    )
    response = requests.get(url)
    return response.json()

    