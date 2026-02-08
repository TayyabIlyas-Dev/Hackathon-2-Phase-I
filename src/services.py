"""
Task management services for the Todo CLI application.

This module contains business logic for all task operations (CRUD operations).
"""

from typing import List, Optional
from models import Task


class TaskService:
    """
    Service class that handles all task operations including:
    - Adding new tasks
    - Retrieving tasks
    - Updating tasks
    - Deleting tasks
    - Marking tasks as complete/incomplete
    """

    def __init__(self):
        """Initialize the service with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with the given title and optional description.

        Args:
            title: The required title of the task
            description: Optional description of the task

        Returns:
            The newly created Task object
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None,
                   description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided)
            description: New description (if provided)

        Returns:
            True if task was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if task was marked complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = True
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = False
        return True