# test_mission_manager.py

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory
from cybersecurity_agent.planning.mission_manager import MissionManager


def test_default_mission_is_investigate() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()

    mission = mission_manager.get_current_mission(memory)

    assert mission == "INVESTIGATE"


def test_mission_manager_changes_mission() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()

    mission_manager.change_mission(
        memory=memory,
        new_mission="EMERGENCY_RESPONSE",
        reason="Active attack detected",
    )

    assert (
        mission_manager.get_current_mission(memory)
        == "EMERGENCY_RESPONSE"
    )

    assert memory.get("decision_log") == [
        (
            "Mission changed from INVESTIGATE "
            "to EMERGENCY_RESPONSE: Active attack detected"
        )
    ]


def test_same_mission_is_not_logged_twice() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()

    mission_manager.change_mission(
        memory=memory,
        new_mission="INVESTIGATE",
        reason="No change required",
    )

    assert memory.get("decision_log") == []