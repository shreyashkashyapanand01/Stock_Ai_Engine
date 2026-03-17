# from app.data.universe_providers.gainer_provider import fetch_top_sector_performers 
# from app.config import top_limit,per_sector_limit

# def run_market_scan(limit_per_sector=per_sector_limit, total_limit=top_limit):

#     top_movers = fetch_top_sector_performers(
#         limit_per_sector=limit_per_sector, 
#         total_top_limit=total_limit
#     )

#     if not top_movers:
#         print("Market Scan: No data retrieved from NSE.")
#         return []

#     opportunities = []
#     for stock in top_movers:
#         opportunities.append({
#             "symbol": stock["symbol"],
#             "sector": stock["sector"],
#             "score": round(stock["perChange"], 2),  # Using % Change as the primary score
#             "last_price": stock["ltp"],
#             "status": "High Momentum"
#         })

#     return opportunities


from app.data.universe_providers.gainer_provider import fetch_top_sector_performers
from app.pipelines.stock_pipeline import run_stock_pipeline
from app.scoring.opportunity_scorer import score_opportunity


def run_market_scan():

    top_movers = fetch_top_sector_performers()

    opportunities = []

    for stock in top_movers:

        symbol = stock["symbol"]

        try:
            result = run_stock_pipeline(symbol)

            if "error" in result:
                continue

            # AI score
            ai_score = score_opportunity(result)

            # momentum boost
            momentum_score = stock["perChange"]

            final_score = ai_score + (momentum_score / 10)

            opportunities.append({
                "symbol": symbol,
                "sector": stock["sector"],
                "score": round(final_score, 2),
                "momentum": round(momentum_score, 2),
                "summary": result["summary"]
            })

        except Exception:
            continue

    opportunities.sort(key=lambda x: x["score"], reverse=True)

    return opportunities