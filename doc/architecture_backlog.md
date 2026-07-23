# Enterprise AI Cybersecurity Investigation Agent

## Architecture Backlog

This document records architectural improvements that have been intentionally postponed.
These are not bugs.
They are future improvements that will be implemented when they provide sufficient value.

---

## AI-ARCH-001

Status: Planned

Title: Separate Tool Metadata from Business Logic

Current State:
    TOOL_GAIN, TOOL_COST and TOOL_EVIDENCE_MAP are defined inside business logic modules.

Future Design:
    Move them into a dedicated configuration package.

Reason:
    Separate configuration from business logic.

Target Milestone:
    After Tool Registry implementation.

Priority:
    Medium

---

## AI-ARCH-002

Status: Future

Title: Introduce Tool Catalog

Current State:
    Tool metadata is split across multiple configuration files.

Future Design:
    Create a centralized Tool Catalog containing:
        - gain
        - cost
        - evidence mapping
        - permissions
        - estimated runtime
        - business value
        - retry policy

Reason:
    Improve scalability and simplify adding new enterprise tools.

Priority:
    Low