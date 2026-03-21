import logging
from fastapi import APIRouter
from app.schemas.portfolio_schema import PortfolioAnalysisRequest
from app.pipelines.portfolio_pipeline import run_portfolio_pipeline

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/portfolio-analyze")
def analyze_portfolio(request: PortfolioAnalysisRequest):
    logger.info("portfolio_api: Received portfolio analysis request")

    try:
        result = run_portfolio_pipeline(request.holdings)
        return result

    except Exception as e:
        logger.error(f"portfolio_api: Error - {str(e)}")
        return {"error": "Portfolio analysis failed"}