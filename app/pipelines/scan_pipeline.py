from app.data.universe_providers.gainer_provider import fetch_top_sector_performers 
from app.config import top_limit,per_sector_limit

def run_market_scan(limit_per_sector=per_sector_limit, total_limit=top_limit):

    top_movers = fetch_top_sector_performers(
        limit_per_sector=limit_per_sector, 
        total_top_limit=total_limit
    )

    if not top_movers:
        print("Market Scan: No data retrieved from NSE.")
        return []

    opportunities = []
    for stock in top_movers:
        opportunities.append({
            "symbol": stock["symbol"],
            "sector": stock["sector"],
            "score": round(stock["perChange"], 2),  # Using % Change as the primary score
            "last_price": stock["ltp"],
            "status": "High Momentum"
        })

    return opportunities
