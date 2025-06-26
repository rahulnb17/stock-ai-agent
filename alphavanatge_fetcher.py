import requests

API_KEY = "0O9ZKES1C05UAT5I"  # Replace with your API key
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Global Quote" in data:
        price = data["Global Quote"]["05. price"]
        return {"ticker": symbol, "price": float(price)}
    else:
        return {"error": "Failed to fetch stock data."}

# Example Usage
if __name__ == "__main__":
    stock = "AAPL"  # Change this to any stock ticker
    print(get_stock_price(stock))
