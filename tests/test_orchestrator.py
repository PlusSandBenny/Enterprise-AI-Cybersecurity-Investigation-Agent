# test_orchestrator.py

from cybersecurity_agent.core.orchestrator import Orchestrator
from cybersecurity_agent.memory.investigation_memory import (
    InvestigationMemory,
)
from cybersecurity_agent.planning.mission_manager import (
    MissionManager,
)
from cybersecurity_agent.planning.planner import Planner


def test_orchestrator_returns_planner_decision() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()
    planner = Planner()

    orchestrator = Orchestrator(
        planner=planner,
        mission_manager=mission_manager,
        memory=memory,
    )

    decision = orchestrator.run(
        goal="Determine account compromise",
        available_tools=[
            "analyze_device_reputation",
            "analyze_login_history",
            "analyze_location",
        ],
    )

    assert decision.action == "analyze_location"
    assert decision.mission == "INVESTIGATE"


def test_orchestrator_uses_current_mission() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()
    planner = Planner()

    mission_manager.change_mission(
        memory=memory,
        new_mission="EMERGENCY_RESPONSE",
        reason="Active attack detected",
    )

    orchestrator = Orchestrator(
        planner=planner,
        mission_manager=mission_manager,
        memory=memory,
    )

    decision = orchestrator.run(
        goal="Contain active attack",
        available_tools=[
            "analyze_login_history",
            "analyze_location",
        ],
    )

    assert decision.mission == "EMERGENCY_RESPONSE"


def test_orchestrator_records_planning_decision() -> None:
    memory = InvestigationMemory()
    mission_manager = MissionManager()
    planner = Planner()

    orchestrator = Orchestrator(
        planner=planner,
        mission_manager=mission_manager,
        memory=memory,
    )

    decision = orchestrator.run(
        goal="Determine account compromise",
        available_tools=[
            "analyze_login_history",
            "analyze_location",
        ],
    )

    decision_log = memory.get("decision_log")

    assert len(decision_log) == 1
    assert decision.action in decision_log[0]
    assert "INVESTIGATE" in decision_log[0]