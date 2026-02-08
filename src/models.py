"""
Task model for the Todo CLI application.

This module defines the Task data class with ID, title, description, and completion status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with attributes: ID (unique identifier),
    title (required string), description (optional string), completion status (boolean)
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False