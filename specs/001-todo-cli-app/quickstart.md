# Quickstart Guide: Todo CLI Application

**Date**: 2025-12-31
**Feature**: Phase I – In-Memory Todo Python Console Application
**Branch**: 001-todo-cli-app

## Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager (for dependency management)

### Setup
1. Clone or navigate to the project directory
2. Install dependencies: `uv sync` (if pyproject.toml exists)
3. Run the application: `python src/main.py`

### First Run
When you run the application, you'll see a menu with the following options:
```
Todo CLI Application
====================
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task complete/incomplete
6. Exit
```

## Basic Usage

### Adding a Task
1. Select option 1 from the main menu
2. Enter a title for the task (required)
3. Optionally enter a description
4. The task will be added with a unique ID and displayed as incomplete

### Viewing Tasks
1. Select option 2 from the main menu
2. All tasks will be displayed with their ID, title, and completion status
3. If no tasks exist, a message will indicate this

### Updating a Task
1. Select option 3 from the main menu
2. Enter the task ID you want to update
3. Enter the new title and/or description
4. The task will be updated with the new information

### Deleting a Task
1. Select option 4 from the main menu
2. Enter the task ID you want to delete
3. Confirm the deletion if prompted
4. The task will be removed from the list

### Marking Task Complete/Incomplete
1. Select option 5 from the main menu
2. Enter the task ID you want to mark
3. Select whether to mark it complete or incomplete
4. The task status will be updated

## Error Handling
- If you enter an invalid task ID, the application will display an error message
- If you try to update/delete a non-existent task, the application will notify you
- Required fields (like title) will be validated before accepting input

## Session Limitations
- All tasks are stored in memory only
- Tasks will be lost when the application is closed
- This is by design for Phase I of the application