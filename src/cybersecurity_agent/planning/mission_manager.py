# mission_manager.py
# 

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory


class MissionManager:
    def get_current_mission(
        self,
        memory: InvestigationMemory,
    ) -> str:
        return memory.get("current_mission", "INVESTIGATE")

    def change_mission(
        self,
        memory: InvestigationMemory,
        new_mission: str,
        reason: str,
    ) -> None:
        current_mission = self.get_current_mission(memory)

        if current_mission == new_mission:
            return

        memory.set("current_mission", new_mission)
        memory.add_decision_log(
            f"Mission changed from {current_mission} "
            f"to {new_mission}: {reason}"
        )