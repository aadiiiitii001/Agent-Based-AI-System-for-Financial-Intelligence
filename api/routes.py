from fastapi import APIRouter, Depends
from api.deps import get_current_user
from api.models import QueryRequest
from agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()

@router.post("/analyze")
def analyze_financial_query(
    request: QueryRequest,
    user=Depends(get_current_user)
):
    """
    Secure endpoint for financial analysis
    """
    result = orchestrator.execute(request.query)

    return {
        "user": user["sub"],
        "result": result
    }
