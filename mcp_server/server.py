from mcp_server.tools import get_market_data, analyze_risk
from mcp_server.schemas import MarketDataRequest, RiskAnalysisRequest

class MCPServer:
    def __init__(self):
        self.tools = {
            "get_market_data": get_market_data,
            "analyze_risk": analyze_risk
        }

    def call_tool(self, agent_name: str, tool_name: str, payload: dict):
        if tool_name not in self.tools:
            raise ValueError("Tool not allowed")

        tool = self.tools[tool_name]

        if tool_name == "get_market_data":
            request = MarketDataRequest(**payload)
            return tool(agent_name, request)

        if tool_name == "analyze_risk":
            request = RiskAnalysisRequest(**payload)
            return tool(agent_name, request)
