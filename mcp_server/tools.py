
from mcp_server.schemas import (
    MarketDataRequest, MarketDataResponse,
    RiskAnalysisRequest, RiskAnalysisResponse
)
from mcp_server.audit import log_action
import random


def get_market_data(agent_name: str, request: MarketDataRequest):
    log_action(agent_name, "get_market_data", request.dict())

    # Mock response (replace with real API later)
    return MarketDataResponse(
        symbol=request.symbol,
        price=round(random.uniform(100, 500), 2),
        trend="Bullish"
    )


def analyze_risk(agent_name: str, request: RiskAnalysisRequest):
    log_action(agent_name, "analyze_risk", request.dict())

    return RiskAnalysisResponse(
        symbol=request.symbol,
        risk_score=round(random.uniform(0, 1), 2),
        volatility="Medium"
    )
