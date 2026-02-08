# Todo CLI Application

A simple command-line Todo application that allows users to manage daily tasks with add, view, update, delete, and mark complete/incomplete functionality.

## Features

- Add new tasks with title and optional description
- View all tasks with their ID, title, and completion status
- Update existing task title and/or description
- Delete tasks by ID
- Mark tasks as complete or incomplete

## Requirements

- Python 3.13 or higher

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Run the application using Python:

```bash
python src/main.py
```

## Usage

The application provides a menu-driven interface:

1. Add task - Add a new task with title and optional description
2. View tasks - Display all tasks with their ID, title, and completion status
3. Update task - Modify an existing task's title and/or description
4. Delete task - Remove a task by ID
5. Mark task complete/incomplete - Toggle task completion status
6. Exit - Close the application

## Architecture

The application follows a modular architecture with clear separation of concerns:

- `models.py`: Task data model
- `services.py`: Business logic for task operations
- `cli.py`: User interface and input handling
- `main.py`: Application entry point
- `utils.py`: Utility functions# Hackathon-2-Phase-1
