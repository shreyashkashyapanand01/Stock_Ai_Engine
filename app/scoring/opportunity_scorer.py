def score_opportunity(stock_result):

    technical = stock_result["technical"]
    fundamental = stock_result["fundamental"]

    score = 0

    if technical["trend"] == "bullish":
        score += 2

    if technical["momentum"] == "strong":
        score += 2

    if technical["rsi"] == "oversold":
        score += 2

    if fundamental["valuation"] == "undervalued":
        score += 2

    if fundamental["growth"] == "strong growth":
        score += 2

    return score