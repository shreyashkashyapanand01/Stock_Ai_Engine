import random

RISK_FREE_RATE = 0.06


def calculate_portfolio_metrics(holdings, market_data_tool):
    total_investment = 0
    total_value = 0

    returns = []

    for h in holdings:
        data = market_data_tool(h.symbol)
        current_price = data.get("price", h.buy_price)
        
        if current_price==0:
            current_price=h.buy_pice

        invested = h.buy_price * h.quantity
        current_val = current_price * h.quantity

        total_investment += invested
        total_value += current_val

        returns.append((current_price - h.buy_price) / h.buy_price)

    total_return = ((total_value - total_investment) / total_investment) * 100

    avg_return = sum(returns) / len(returns) if returns else 0

    volatility = (sum([(r - avg_return) ** 2 for r in returns]) / len(returns)) ** 0.5 if returns else 0

    sharpe = (avg_return - RISK_FREE_RATE) / volatility if volatility != 0 else 0

    beta = round(0.8 + random.random() * 1.2, 2)  # mock realistic beta

    return {
        "totalInvestment": round(total_investment, 2),
        "totalValue": round(total_value, 2),
        "totalReturn": round(total_return, 2),
        "beta": beta,
        "sharpeRatio": round(sharpe, 2),
        "volatility": round(volatility, 2)
    }