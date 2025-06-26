import requests

def analyze_stock_price(ticker: str, price: float):
    prompt = f"Analyze the stock price of {ticker}, currently at ${price}. Provide a buy/sell/hold recommendation with reasoning."

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        )
        result = response.json()
        return result.get("response", "No response from Mistral.")
    except Exception as e:
        return f"Error generating analysis: {str(e)}"
