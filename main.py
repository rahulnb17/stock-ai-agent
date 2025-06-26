from fastapi import FastAPI
from pydantic import BaseModel
from stock_price_fetcher import get_stock_price_yahoo, get_stock_price_ddg
from ai_analyzer import analyze_stock_price
from prometheus_fastapi_instrumentator import Instrumentator  # ✅ ADD THIS

app = FastAPI()

# ✅ Expose /metrics for Prometheus
Instrumentator().instrument(app).expose(app)

class StockRequest(BaseModel):
    ticker: str

@app.get("/")
def home():
    return {"message": "Stock Market AI with Mistral is Running!"}

@app.post("/fetch_stock_price/")
def fetch_stock_price(stock: StockRequest):
    yahoo_data = get_stock_price_yahoo(stock.ticker)
    if "error" in yahoo_data:
        yahoo_data = get_stock_price_ddg(stock.ticker)
    return yahoo_data

@app.post("/analyze_stock/")
def analyze_stock(stock: StockRequest):
    price_data = get_stock_price_yahoo(stock.ticker)
    if "error" in price_data:
        return {"error": "Stock price not available."}
    
    analysis = analyze_stock_price(stock.ticker, price_data["price"])
    return {
        "ticker": stock.ticker,
        "price": price_data["price"],
        "analysis": analysis
    }
