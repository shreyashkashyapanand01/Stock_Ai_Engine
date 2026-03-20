from app.analysis.sector_mapper import get_sector


def analyze_diversification(holdings):
    sector_allocation = {}

    for h in holdings:
        sector = get_sector(h.symbol)
        sector_allocation[sector] = sector_allocation.get(sector, 0) + h.quantity

    total = sum(sector_allocation.values())

    sector_percent = {
        k: round((v / total) * 100, 2) for k, v in sector_allocation.items()
    }

    max_sector = max(sector_percent, key=sector_percent.get)

    risk = "Well Diversified"
    if sector_percent[max_sector] > 60:
        risk = f"High concentration in {max_sector}"

    return {
        "sectorExposure": sector_percent,
        "risk": risk
    }