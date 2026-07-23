# information_gain.py

from cybersecurity_agent.memory.investigation_memory import InvestigationMemory


TOOL_GAIN = {
    "analyze_failed_logins": 0.40,
    "analyze_location": 0.20,
    "analyze_login_history": 0.30,
    "analyze_device_reputation": 0.50,
}


TOOL_EVIDENCE_MAP = {
    "analyze_failed_logins": "failed_logins",
    "analyze_location": "location",
    "analyze_login_history": "login_history",
    "analyze_device_reputation": "device_reputation",
}


def expected_gain(
    tool: str,
    memory: InvestigationMemory,
) -> float:
    evidence_name = TOOL_EVIDENCE_MAP.get(tool)

    if evidence_name is None:
        raise ValueError(
            f"No evidence mapping exists for tool: {tool}"
        )

    if memory.has_evidence(evidence_name):
        return 0.0

    try:
        return TOOL_GAIN[tool]
    except KeyError as error:
        raise ValueError(
            f"No information-gain value exists for tool: {tool}"
        ) from error