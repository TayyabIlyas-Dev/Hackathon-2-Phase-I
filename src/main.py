"""
Main entry point for the Todo CLI application.

This module initializes the application components and starts the CLI loop.
"""

from services import TaskService
from cli import TodoCLI


def main():
    """
    Main function that initializes the application and starts the CLI.
    """
    # Initialize the task service
    task_service = TaskService()

    # Initialize the CLI with the task service
    cli = TodoCLI(task_service)

    # Start the CLI loop
    print("Welcome to the Todo CLI Application!")
    cli.run()


if __name__ == "__main__":
    main()