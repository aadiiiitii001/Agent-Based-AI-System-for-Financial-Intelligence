# agents/orchestrator.py

from agents.market_agent import MarketAgent
from agents.risk_agent import RiskAgent
from agents.compliance_agent import ComplianceAgent

class OrchestratorAgent:
    def __init__(self):
        self.market_agent = MarketAgent()
        self.risk_agent = RiskAgent()
        self.compliance_agent = ComplianceAgent()

    def plan_tasks(self, user_query: str):
        """
        Decompose the user query into tasks.
        """
        tasks = []

        query = user_query.lower()

        if "stock" in query or "market" in query or "price" in query:
            tasks.append("market_analysis")

        if "risk" in query or "volatility" in query:
            tasks.append("risk_analysis")

        if "compliance" in query or "regulatory" in query:
            tasks.append("compliance_check")

        return tasks

    def execute(self, user_query: str):
        """
        Execute planned tasks and aggregate results.
        """
        plan = self.plan_tasks(user_query)
        results = {}

        for task in plan:
            if task == "market_analysis":
                results["market"] = self.market_agent.run(user_query)

            elif task == "risk_analysis":
                results["risk"] = self.risk_agent.run(user_query)

            elif task == "compliance_check":
                results["compliance"] = self.compliance_agent.run(user_query)

        return self.aggregate_results(results)

    def aggregate_results(self, results: dict):
        """
        Combine all agent outputs into a structured response.
        """
        final_report = {
            "summary": "Automated financial intelligence report",
            "details": results
        }
        return final_report
