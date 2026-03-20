from app.tools.market_data_tool import get_stock_name
import yfinance as yf


def get_sector(symbol: str):
    try:
        ticker_symbol = get_stock_name(symbol)

        if not ticker_symbol.endswith(".NS"):
            ticker_symbol += ".NS"
            
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        return info.get("sector", "Others")

    except Exception:
        return "Others"