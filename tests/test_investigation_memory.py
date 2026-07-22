# test_investigation_memory.py

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory


def test_memory_stores_evidence() -> None:
    memory = InvestigationMemory()

    location_result = {
        "risk": "red",
        "score": 80,
        "reason": "High-risk location",
    }

    memory.add_evidence("location", location_result)

    assert memory.has_evidence("location")
    assert memory.get_evidence("location") == location_result


def test_memory_marks_goal_completed_once() -> None:
    memory = InvestigationMemory()

    memory.mark_goal_completed("analyze_location")
    memory.mark_goal_completed("analyze_location")

    assert memory.get("completed_goals") == ["analyze_location"]