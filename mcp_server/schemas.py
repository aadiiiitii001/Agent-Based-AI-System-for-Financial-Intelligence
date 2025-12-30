from pydantic import BaseModel

class MarketDataRequest(BaseModel):
    symbol: str

class MarketDataResponse(BaseModel):
    symbol: str
    price: float
    trend: str


class RiskAnalysisRequest(BaseModel):
    symbol: str

class RiskAnalysisResponse(BaseModel):
    symbol: str
    risk_score: float
    volatility: str
