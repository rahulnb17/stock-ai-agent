from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Stock Market AI with Mistral is Running!"}

def test_fetch_stock_price_valid():
    response = client.post("/fetch_stock_price/", json={"ticker": "AAPL"})
    assert response.status_code == 200
    assert "price" in response.json() or "price_info" in response.json()

def test_fetch_stock_price_invalid():
    response = client.post("/fetch_stock_price/", json={"ticker": "INVALID123"})
    data = response.json()
    assert response.status_code == 200
    assert "error" in data or "price_info" in data  # fallback via DDG

def test_analyze_stock_valid():
    response = client.post("/analyze_stock/", json={"ticker": "AAPL"})
    data = response.json()
    assert response.status_code == 200
    assert "analysis" in data

def test_analyze_stock_invalid():
    response = client.post("/analyze_stock/", json={"ticker": "INVALID123"})
    data = response.json()
    assert response.status_code == 200
    assert "error" in data or "analysis" in data
