from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze-stock")
def analyze_stock(data: dict):

    symbol = data.get("symbol")

    return {
        "symbol": symbol,
        "summary": "Dummy analysis working",
        "risk_level": "low",
        "confidence": 0.5
    }