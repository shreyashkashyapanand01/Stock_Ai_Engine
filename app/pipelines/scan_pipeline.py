from concurrent.futures import ThreadPoolExecutor

from app.data.universe_provider import load_universe
from app.pipelines.stock_pipeline import run_stock_pipeline
from app.scoring.opportunity_scorer import score_opportunity


def process_stock(symbol):

    result = run_stock_pipeline(symbol)

    if "error" in result:
        return None

    score = score_opportunity(result)

    return {
        "symbol": symbol,
        "score": score,
        "summary": result["summary"]
    }


def run_market_scan():

    symbols = load_universe()

    opportunities = []

    with ThreadPoolExecutor(max_workers=5) as executor:

        results = executor.map(process_stock, symbols)

    for r in results:
        if r:
            opportunities.append(r)

    opportunities.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return opportunities[:5]