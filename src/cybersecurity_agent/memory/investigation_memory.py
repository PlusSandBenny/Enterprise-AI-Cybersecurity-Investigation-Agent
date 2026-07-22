# investigation_memory.py
from typing import Any


class InvestigationMemory:
    def __init__(self) -> None:
        self._data: dict[str, Any] = {
            "current_mission": "INVESTIGATE",
            "incident_mode": "NORMAL",
            "evidence": {},
            "completed_goals": [],
            "decision_log": [],
        }

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def add_evidence(self, evidence_name: str, result: dict[str, Any]) -> None:
        self._data["evidence"][evidence_name] = result

    def get_evidence(self, evidence_name: str) -> dict[str, Any] | None:
        return self._data["evidence"].get(evidence_name)

    def has_evidence(self, evidence_name: str) -> bool:
        return evidence_name in self._data["evidence"]

    def mark_goal_completed(self, goal_name: str) -> None:
        if goal_name not in self._data["completed_goals"]:
            self._data["completed_goals"].append(goal_name)

    def add_decision_log(self, message: str) -> None:
        self._data["decision_log"].append(message)

    def to_dict(self) -> dict[str, Any]:
        return self._data.copy()