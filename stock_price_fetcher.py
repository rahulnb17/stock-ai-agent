import yfinance as yf
from duckduckgo_search import DDGS

def get_stock_price_yahoo(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")["Close"].iloc[-1]
        return {"ticker": ticker, "price": round(current_price, 2)}
    except Exception as e:
        return {"error": f"Failed to fetch from Yahoo Finance: {str(e)}"}

def get_stock_price_ddg(ticker: str):
    try:
        query = f"{ticker} stock price"
        results = DDGS(query, max_results=1)
        return {"ticker": ticker, "source": "DuckDuckGo", "price_info": results[0]} if results else {"error": "No data found"}
    except Exception as e:
        return {"error": f"Failed to fetch from DuckDuckGo: {str(e)}"}
