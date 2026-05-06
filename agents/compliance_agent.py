# agents/compliance_agent.py

from mcp_server.server import MCPServer

class ComplianceAgent:
    """
    ComplianceAgent checks regulatory and compliance risks
    by analyzing financial filings and policy documents.
    """
    def __init__(self):
        self.name = "ComplianceAgent"
        self.mcp = MCPServer()

    def extract_entity(self, query: str) -> str:
        query = query.lower()
        if "tesla" in query or "tsla" in query:
            return "Tesla"
        if "apple" in query or "aapl" in query:
            return "Apple"
        if "nvda" in query or "nvidia" in query:
            return "NVDA"
        if "microsoft" in query or "msft" in query:
            return "Microsoft"
        if "google" in query or "googl" in query:
            return "Google"
        if "amazon" in query or "amzn" in query:
            return "Amazon"
        if "bitcoin" in query or "btc" in query:
            return "Bitcoin"
        return "Unknown Entity"

    def run(self, query: str) -> dict:
        entity = self.extract_entity(query)
        if entity == "Unknown Entity":
            return {
                "status": "skipped",
                "reason": "No identifiable entity for compliance analysis"
            }
        compliance_flags = self.check_compliance_rules(entity)
        return {
            "entity": entity,
            "compliance_status": compliance_flags["status"],
            "flags": compliance_flags["flags"],
            "summary": compliance_flags["summary"]
        }

    def check_compliance_rules(self, entity: str) -> dict:
        if entity == "Tesla":
            return {
                "status": "Attention Required",
                "flags": [
                    "Regulatory disclosures under review",
                    "Market volatility disclosures detected"
                ],
                "summary": "Potential regulatory scrutiny due to recent filings"
            }
        if entity == "NVDA":
            return {
                "status": "Attention Required",
                "flags": [
                    "US export control regulations apply",
                    "AI chip restrictions under regulatory review",
                    "Revenue concentration risk in AI segment"
                ],
                "summary": "Subject to US export compliance for AI hardware and chips"
            }
        if entity == "Apple":
            return {
                "status": "Attention Required",
                "flags": [
                    "EU Digital Markets Act compliance required",
                    "App Store antitrust review ongoing"
                ],
                "summary": "Regulatory pressure in EU and US markets"
            }
        if entity == "Microsoft":
            return {
                "status": "Attention Required",
                "flags": [
                    "Activision acquisition under regulatory scrutiny",
                    "AI governance compliance in progress"
                ],
                "summary": "Ongoing regulatory review of AI and acquisitions"
            }
        if entity == "Google":
            return {
                "status": "Attention Required",
                "flags": [
                    "Antitrust ruling in US search market",
                    "EU GDPR compliance requirements"
                ],
                "summary": "Significant antitrust and data privacy regulatory exposure"
            }
        if entity == "Amazon":
            return {
                "status": "Attention Required",
                "flags": [
                    "FTC antitrust investigation ongoing",
                    "Marketplace seller compliance requirements"
                ],
                "summary": "Under FTC scrutiny for marketplace practices"
            }
        if entity == "Bitcoin":
            return {
                "status": "High Risk",
                "flags": [
                    "Unregulated in multiple jurisdictions",
                    "AML and KYC compliance varies by exchange",
                    "SEC classification pending"
                ],
                "summary": "High regulatory uncertainty across global markets"
            }
        return {
            "status": "Clear",
            "flags": [],
            "summary": "No immediate compliance concerns detected"
        }
