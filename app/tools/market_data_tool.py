import yfinance as yf


import yfinance as yf


def fetch_price_history(symbol: str):

    if not symbol.endswith(".NS"):
        symbol = symbol + ".NS"

    ticker = yf.Ticker(symbol)

    df = ticker.history(period="6mo")

    return df

def fetch_latest_price(symbol: str):

    ticker = yf.Ticker(symbol)

    price = ticker.history(period="1d")["Close"].iloc[-1]

    return float(price)