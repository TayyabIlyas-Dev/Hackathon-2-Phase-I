"""
Utility functions for the Todo CLI application.

This module contains helper functions for input validation and formatting.
"""


def validate_task_id(task_id_str: str) -> bool:
    """
    Validate if a string represents a valid task ID (positive integer).

    Args:
        task_id_str: String to validate as a task ID

    Returns:
        True if the string represents a valid positive integer, False otherwise
    """
    try:
        task_id = int(task_id_str)
        return task_id > 0
    except ValueError:
        return False


def get_positive_int_input(prompt: str) -> int:
    """
    Get a positive integer input from the user.

    Args:
        prompt: The prompt to display to the user

    Returns:
        A positive integer entered by the user
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def confirm_action(prompt: str) -> bool:
    """
    Ask the user to confirm an action.

    Args:
        prompt: The confirmation prompt to display

    Returns:
        True if user confirms, False otherwise
    """
    response = input(f"{prompt} (y/N): ").strip().lower()
    return response in ['y', 'yes']