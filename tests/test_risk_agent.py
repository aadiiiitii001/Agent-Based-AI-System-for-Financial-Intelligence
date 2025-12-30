from agents.risk_agent import RiskAgent

def test_risk_agent():
    agent = RiskAgent()
    response = agent.run("Analyze TSLA risk")

    assert "risk_score" in response
    assert "assessment" in response
