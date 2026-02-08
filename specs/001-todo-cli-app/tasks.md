---
description: "Task list for Todo CLI Application implementation"
---

# Tasks: Phase I – In-Memory Todo Python Console Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No automated tests required per specification (manual CLI testing only for Phase I)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 Initialize Python 3.13 project with basic configuration
- [x] T003 [P] Create README.md with setup and run instructions
- [x] T004 [P] Create pyproject.toml with project metadata

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Task model in src/models.py with id, title, description, completed attributes
- [x] T006 Create in-memory task storage in src/services.py with list initialization
- [x] T007 [P] Create utils.py for input validation helpers
- [x] T008 Create basic CLI menu structure in src/cli.py
- [x] T009 Create main.py entry point that initializes the application

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with required title and optional description

**Independent Test**: User can run the application and add a new task, which appears in the task list with a unique ID and is displayed as incomplete

### Implementation for User Story 1

- [x] T010 [P] [US1] Add add_task method to TaskService in src/services.py
- [x] T011 [P] [US1] Create add_task_input function in src/cli.py for user input
- [x] T012 [US1] Create add_task_display function in src/cli.py for confirmation messages
- [x] T013 [US1] Integrate add task functionality in main.py menu option 1
- [x] T014 [US1] Add title validation to ensure it's not empty
- [x] T015 [US1] Add auto-incrementing ID assignment to new tasks

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with their ID, title, and completion status

**Independent Test**: User can add tasks and then view them, seeing all tasks with their unique ID, title, and completion status

### Implementation for User Story 2

- [x] T016 [P] [US2] Add get_all_tasks method to TaskService in src/services.py
- [x] T017 [P] [US2] Create view_tasks_display function in src/cli.py for formatting task list
- [x] T018 [US2] Integrate view tasks functionality in main.py menu option 2
- [x] T019 [US2] Add empty task list handling with appropriate message
- [x] T020 [US2] Format task display with ID, title, and completion status

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Enable users to mark tasks as complete or incomplete by ID

**Independent Test**: User can mark a task as complete or incomplete, and the status changes appropriately

### Implementation for User Story 3

- [x] T021 [P] [US3] Add mark_task_complete method to TaskService in src/services.py
- [x] T022 [P] [US3] Add mark_task_incomplete method to TaskService in src/services.py
- [x] T023 [US3] Create mark_task_input function in src/cli.py for selecting task and status
- [x] T024 [US3] Integrate mark task functionality in main.py menu option 5
- [x] T025 [US3] Add validation to ensure task ID exists before marking

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Existing Task (Priority: P2)

**Goal**: Enable users to update an existing task's title and/or description by ID

**Independent Test**: User can update a task's title or description, and the changes reflect immediately

### Implementation for User Story 4

- [x] T026 [P] [US4] Add update_task method to TaskService in src/services.py
- [x] T027 [P] [US4] Create update_task_input function in src/cli.py for collecting new values
- [x] T028 [US4] Integrate update task functionality in main.py menu option 3
- [x] T029 [US4] Add validation to ensure task ID exists before updating
- [x] T030 [US4] Preserve unchanged attributes when updating

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task by ID (Priority: P2)

**Goal**: Enable users to delete tasks by their ID

**Independent Test**: User can delete a task, and it is removed from the list

### Implementation for User Story 5

- [x] T031 [P] [US5] Add delete_task method to TaskService in src/services.py
- [x] T032 [P] [US5] Create delete_task_input function in src/cli.py for task selection
- [x] T033 [US5] Integrate delete task functionality in main.py menu option 4
- [x] T034 [US5] Add validation to ensure task ID exists before deletion
- [x] T035 [US5] Add confirmation prompt for delete operation

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 [P] Add comprehensive error handling for invalid task IDs across all operations
- [x] T037 [P] Improve CLI output formatting for better readability
- [x] T038 Add proper exit functionality in main.py menu option 6
- [x] T039 [P] Add input validation helpers in src/utils.py for task IDs
- [x] T040 Add consistent error messages for edge cases
- [x] T041 [P] Add docstrings to all public functions
- [x] T042 Run manual testing validation using quickstart.md scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Add add_task method to TaskService in src/services.py"
Task: "Create add_task_input function in src/cli.py for user input"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence