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
        """
        Extracts company/entity name from query.
        """
        query = query.lower()
        if "tesla" in query:
            return "Tesla"
        if "apple" in query:
            return "Apple"
        return "Unknown Entity"

    def run(self, query: str) -> dict:
        """
        Main execution method.
        """
        entity = self.extract_entity(query)

        if entity == "Unknown Entity":
            return {
                "status": "skipped",
                "reason": "No identifiable entity for compliance analysis"
            }

        # In real systems this would read PDFs via MCP
        # Example: 10-K, 10-Q, internal compliance docs
        compliance_flags = self.check_compliance_rules(entity)

        return {
            "entity": entity,
            "compliance_status": compliance_flags["status"],
            "flags": compliance_flags["flags"],
            "summary": compliance_flags["summary"]
        }

    def check_compliance_rules(self, entity: str) -> dict:
        """
        Mock compliance logic.
        Replace with MCP PDF reader or RAG pipeline later.
        """

        # Example simulated findings
        if entity == "Tesla":
            return {
                "status": "Attention Required",
                "flags": [
                    "Regulatory disclosures under review",
                    "Market volatility disclosures detected"
                ],
                "summary": "Potential regulatory scrutiny due to recent filings"
            }

        return {
            "status": "Clear",
            "flags": [],
            "summary": "No immediate compliance concerns detected"
        }
