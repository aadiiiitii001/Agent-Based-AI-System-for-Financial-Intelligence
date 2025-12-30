from agents.orchestrator import OrchestratorAgent

def test_orchestrator_execution():
    orchestrator = OrchestratorAgent()
    result = orchestrator.execute("Analyze Tesla stock risk")

    assert "details" in result
    assert "risk" in result["details"]
