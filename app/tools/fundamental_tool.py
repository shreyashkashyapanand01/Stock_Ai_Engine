import yfinance as yf


def fetch_fundamental_data(symbol: str):

    if not symbol.endswith(".NS"):
        symbol = symbol + ".NS"

    ticker = yf.Ticker(symbol)

    info = ticker.info

    fundamentals = {
        "pe_ratio": info.get("trailingPE"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_margin": info.get("profitMargins"),
        "debt_to_equity": info.get("debtToEquity")
    }

    return fundamentals