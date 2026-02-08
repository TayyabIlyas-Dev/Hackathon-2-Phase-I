"""
CLI interface for the Todo CLI application.

This module handles user input, menu display, and output formatting.
"""

from typing import Optional
from models import Task
from services import TaskService
from utils import validate_task_id


class TodoCLI:
    """
    Command-line interface for the Todo application.
    Handles user interactions and displays information.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI with a task service.

        Args:
            task_service: The service to handle task operations
        """
        self.task_service = task_service

    def display_menu(self):
        """Display the main menu options to the user."""
        print("\nTodo CLI Application")
        print("====================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task complete/incomplete")
        print("6. Exit")
        print()

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            The user's choice as a string
        """
        return input("Enter your choice (1-6): ").strip()

    def add_task_input(self) -> tuple[str, Optional[str]]:
        """
        Get task details from user input.

        Returns:
            A tuple containing the title and optional description
        """
        title = input("Enter task title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty")

        description_input = input("Enter task description (optional, press Enter to skip): ").strip()
        description = description_input if description_input else None

        return title, description

    def add_task_display(self, task: Task):
        """
        Display confirmation of task addition.

        Args:
            task: The task that was added
        """
        print(f"Task added successfully!")
        print(f"ID: {task.id}, Title: {task.title}")
        if task.description:
            print(f"Description: {task.description}")
        print(f"Status: {'Complete' if task.completed else 'Incomplete'}")

    def view_tasks_display(self):
        """Display all tasks in a formatted list."""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("\nTask List:")
        print("-" * 60)
        for task in tasks:
            status = "Complete" if task.completed else "Incomplete"
            print(f"ID: {task.id} | {status} | {task.title}")
            if task.description:
                print(f"       Description: {task.description}")
        print("-" * 60)

    def get_task_id_input(self, action: str) -> int:
        """
        Get a task ID from user input.

        Args:
            action: The action being performed (for error messages)

        Returns:
            The task ID entered by the user
        """
        while True:
            task_id_input = input(f"Enter task ID to {action}: ").strip()
            if validate_task_id(task_id_input):
                return int(task_id_input)
            else:
                print("Please enter a valid positive task ID.")

    def update_task_input(self) -> tuple[Optional[str], Optional[str]]:
        """
        Get updated task details from user input.

        Returns:
            A tuple containing the new title (or None) and new description (or None)
        """
        title_input = input("Enter new title (leave blank to keep current): ").strip()
        title = title_input if title_input else None

        description_input = input("Enter new description (leave blank to keep current): ").strip()
        description = description_input if description_input else None

        return title, description

    def mark_task_input(self) -> bool:
        """
        Get completion status from user input.

        Returns:
            True for complete, False for incomplete
        """
        while True:
            status_input = input("Mark as complete (c) or incomplete (i)? ").strip().lower()
            if status_input in ['c', 'complete']:
                return True
            elif status_input in ['i', 'incomplete']:
                return False
            else:
                print("Please enter 'c' for complete or 'i' for incomplete.")

    def display_error(self, message: str):
        """
        Display an error message to the user.

        Args:
            message: The error message to display
        """
        print(f"Error: {message}")

    def display_success(self, message: str):
        """
        Display a success message to the user.

        Args:
            message: The success message to display
        """
        print(f"Success: {message}")

    def run(self):
        """Run the main CLI loop."""
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.handle_add_task()
            elif choice == '2':
                self.handle_view_tasks()
            elif choice == '3':
                self.handle_update_task()
            elif choice == '4':
                self.handle_delete_task()
            elif choice == '5':
                self.handle_mark_task()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def handle_add_task(self):
        """Handle the add task operation."""
        try:
            title, description = self.add_task_input()
            task = self.task_service.add_task(title, description)
            self.add_task_display(task)
        except ValueError as e:
            self.display_error(str(e))
        except Exception as e:
            self.display_error(f"Failed to add task: {str(e)}")

    def handle_view_tasks(self):
        """Handle the view tasks operation."""
        try:
            self.view_tasks_display()
        except Exception as e:
            self.display_error(f"Failed to view tasks: {str(e)}")

    def handle_update_task(self):
        """Handle the update task operation."""
        try:
            task_id = self.get_task_id_input("update")
            if not self.task_service.get_task_by_id(task_id):
                self.display_error(f"Task with ID {task_id} not found.")
                return

            title, description = self.update_task_input()
            if title is None and description is None:
                print("No changes provided.")
                return

            success = self.task_service.update_task(task_id, title, description)
            if success:
                self.display_success(f"Task {task_id} updated successfully.")
            else:
                self.display_error(f"Failed to update task {task_id}.")
        except Exception as e:
            self.display_error(f"Failed to update task: {str(e)}")

    def handle_delete_task(self):
        """Handle the delete task operation."""
        try:
            task_id = self.get_task_id_input("delete")
            task = self.task_service.get_task_by_id(task_id)
            if not task:
                self.display_error(f"Task with ID {task_id} not found.")
                return

            # Confirmation prompt for delete operation
            print(f"Task to delete: {task.title}")
            if not self.confirm_delete():
                print("Delete operation cancelled.")
                return

            success = self.task_service.delete_task(task_id)
            if success:
                self.display_success(f"Task {task_id} deleted successfully.")
            else:
                self.display_error(f"Failed to delete task {task_id}.")
        except Exception as e:
            self.display_error(f"Failed to delete task: {str(e)}")

    def confirm_delete(self) -> bool:
        """
        Ask the user to confirm the delete operation.

        Returns:
            True if user confirms deletion, False otherwise
        """
        return input("Are you sure you want to delete this task? (y/N): ").strip().lower() in ['y', 'yes']

    def handle_mark_task(self):
        """Handle the mark task operation."""
        try:
            task_id = self.get_task_id_input("mark")
            if not self.task_service.get_task_by_id(task_id):
                self.display_error(f"Task with ID {task_id} not found.")
                return

            is_complete = self.mark_task_input()
            if is_complete:
                success = self.task_service.mark_task_complete(task_id)
                status = "complete"
            else:
                success = self.task_service.mark_task_incomplete(task_id)
                status = "incomplete"

            if success:
                self.display_success(f"Task {task_id} marked as {status}.")
            else:
                self.display_error(f"Failed to update task {task_id} status.")
        except Exception as e:
            self.display_error(f"Failed to mark task: {str(e)}")