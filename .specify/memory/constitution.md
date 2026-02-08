<!-- SYNC IMPACT REPORT:
Version change: N/A → 1.0.0
List of modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ updated
- README.md ⚠ pending
Follow-up TODOs: None
-->

# Todo Console Application Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All code must be generated through the SpecKit workflow: Specify → Plan → Tasks → Implement. No manual coding is permitted under any condition. Every line of code must map to an approved Task ID derived from a spec. This ensures deterministic and traceable development where specs are the single source of truth.

### II. Architect-First Approach
The engineer acts as system architect, not a syntax writer. Intent, architecture, and constraints must be clearly defined in specs before implementation. Claude Code performs all implementation work based on these architectural specifications.

### III. Phase I Scope Adherence
Development is strictly limited to the five core features: Add Task, View Task List, Update Task, Delete Task, and Mark Task as Complete/Incomplete. No additional features beyond Phase I scope are permitted. No external databases, file persistence, web frameworks, or async functionality allowed.

### IV. Simplicity and Clarity
Code must prioritize simplicity and clarity over over-engineering. Clean code and readable structure suitable for beginners and reviewers is required. Use small, focused functions with predictable CLI behavior and consistent formatting.

### V. Deterministic Implementation
All features must be implemented through the SpecKit workflow with Claude Code as the only implementation tool. Each feature must be independently spec'd and traceable back to specific tasks. No dead code or unused functions permitted.

### VI. Python-First Architecture
Application must be built as a Python console (CLI) application using Python 3.13+ with UV for package management. In-memory data storage only using Python data structures (lists, dicts, classes). Single-user application with modular structure and separation of concerns.

## Technology Constraints

- Python version: 3.13+
- Package management: UV
- Tooling: Claude Code + Spec-Kit Plus only
- Data storage: In-memory only (no database, no files, no persistence)
- Application type: Console (CLI) application only
- No web frameworks, no async/concurrency, no external dependencies beyond core Python

## Development Standards

- No code may be written without an approved Task ID
- All features must be implemented through the SpecKit workflow: Specify → Plan → Tasks → Implement
- Claude Code must be used for all code generation
- Specs are the single source of truth; code must never override specs
- Each feature must be independently spec'd and traceable
- Explicit error handling and validation required
- Clear and meaningful naming conventions
- Modular structure with separation of concerns (models, logic, CLI)

## Quality Assurance

- All five basic features must work correctly via CLI
- Tasks must have unique IDs
- Task completion status must be clearly visible
- All code must be traceable back to specs and tasks
- No manual code edits permitted
- Claude prompts and iterations must demonstrate spec refinement
- Code must pass validation against architectural constraints

## Governance

This constitution supersedes all other development practices. All amendments must be documented with clear approval process and migration plan if applicable. All pull requests and code reviews must verify compliance with these principles. All development must reference this constitution as the governing document. Complexity must be justified against simplicity principles. Use this document for runtime development guidance and decision-making.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31