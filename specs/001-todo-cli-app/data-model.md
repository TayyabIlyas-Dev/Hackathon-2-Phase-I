# Data Model: Todo CLI Application

**Date**: 2025-12-31
**Feature**: Phase I – In-Memory Todo Python Console Application
**Branch**: 001-todo-cli-app

## Task Entity

### Attributes
- **id**: integer (auto-incremented, unique)
  - Purpose: Unique identifier for each task
  - Type: int
  - Constraints: Positive integer, unique within the application session

- **title**: string (required)
  - Purpose: The main description of the task
  - Type: str
  - Constraints: Non-empty string

- **description**: string (optional)
  - Purpose: Additional details about the task
  - Type: str or None
  - Constraints: Can be empty or None

- **completed**: boolean (default: False)
  - Purpose: Track completion status of the task
  - Type: bool
  - Default: False

### Example Instance
```python
task = {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs, and fruits",
    "completed": False
}
```

## Task List Structure

### In-Memory Storage
- **Type**: List of Task objects
- **Purpose**: Store all tasks during the application session
- **Access Pattern**: Iteration for searching and filtering
- **Lifespan**: Until application terminates

### Operations
- **Add**: Append new task to the list
- **Find**: Iterate through list to find task by ID
- **Update**: Modify attributes of existing task
- **Delete**: Remove task from the list
- **List All**: Return all tasks in the list

## Data Flow

### Creation
1. User provides title and optional description
2. System assigns next available ID
3. System sets completion status to False
4. Task is added to the task list

### Retrieval
1. For viewing all tasks: return entire list
2. For specific task: iterate through list to find matching ID

### Modification
1. Find task by ID in the list
2. Update specified attributes
3. Maintain other attributes unchanged

### Deletion
1. Find task by ID in the list
2. Remove task from the list
3. Remaining tasks retain their IDs