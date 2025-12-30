# agents/risk_agent.py
import os
from mcp_server.server import MCPServer


class RiskAgent:
    """
    RiskAgent is responsible for evaluating financial risk
    such as volatility, anomaly likelihood, or exposure score.
    """

    def __init__(self):
        self.api_key = os.getenv("3XKO7J60NL23QRW7")
        self.base_url = "https://www.alphavantage.co/query"
        self.name = "RiskAgent"
        self.mcp = MCPServer()

    def extract_symbol(self, query: str) -> str:
        """
        Very simple symbol extraction logic.
        Can be replaced with NLP / NER later.
        """
        query = query.upper()
        if "TESLA" in query or "TSLA" in query:
            return "TSLA"
        if "APPLE" in query or "AAPL" in query:
            return "AAPL"
        return "UNKNOWN"

    def run(self, query: str) -> dict:
        """
        Main execution method called by Orchestrator.
        """
        symbol = self.extract_symbol(query)

        if symbol == "UNKNOWN":
            return {
                "status": "skipped",
                "reason": "Unable to identify financial instrument"
            }

        # Call MCP tool instead of direct logic
        response = self.mcp.call_tool(
            agent_name=self.name,
            tool_name="analyze_risk",
            payload={"symbol": symbol}
        )

        return {
            "instrument": symbol,
            "risk_score": response.risk_score,
            "volatility": response.volatility,
            "assessment": self.interpret_risk(response.risk_score)
        }

    def interpret_risk(self, risk_score: float) -> str:
        """
        Converts numeric risk into human-readable explanation.
        """
        if risk_score < 0.3:
            return "Low risk – stable behavior observed"
        elif risk_score < 0.7:
            return "Moderate risk – monitor for fluctuations"
        else:
            return "High risk – significant volatility detected"
