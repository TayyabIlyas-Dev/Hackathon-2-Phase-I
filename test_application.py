#!/usr/bin/env python3
"""
Test script to verify the Todo CLI application components work correctly.
"""

import sys
import os


# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services import TaskService

def test_application():
    """Test all the functionality of the Todo application."""
    print("Testing Todo CLI Application...")

    # Initialize the service
    task_service = TaskService()

    # Test 1: Add a task
    print("\n1. Testing add task functionality...")
    task1 = task_service.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task: ID={task1.id}, Title='{task1.title}', Description='{task1.description}', Completed={task1.completed}")

    # Test 2: Add another task
    task2 = task_service.add_task("Walk the dog")
    print(f"   Added task: ID={task2.id}, Title='{task2.title}', Description='{task2.description}', Completed={task2.completed}")

    # Test 3: Get all tasks
    print("\n2. Testing view all tasks...")
    all_tasks = task_service.get_all_tasks()
    for task in all_tasks:
        status = "Complete" if task.completed else "Incomplete"
        print(f"   Task {task.id}: {task.title} [{status}]")
        if task.description:
            print(f"      Description: {task.description}")

    # Test 4: Update a task
    print("\n3. Testing update task functionality...")
    success = task_service.update_task(task1.id, "Buy weekly groceries", "Milk, bread, eggs, fruits, vegetables")
    if success:
        updated_task = task_service.get_task_by_id(task1.id)
        print(f"   Updated task: ID={updated_task.id}, Title='{updated_task.title}', Description='{updated_task.description}'")
    else:
        print("   Failed to update task")

    # Test 5: Mark task as complete
    print("\n4. Testing mark task complete...")
    success = task_service.mark_task_complete(task1.id)
    if success:
        completed_task = task_service.get_task_by_id(task1.id)
        print(f"   Marked task {completed_task.id} as {'Complete' if completed_task.completed else 'Incomplete'}")
    else:
        print("   Failed to mark task as complete")

    # Test 6: Mark task as incomplete
    print("\n5. Testing mark task incomplete...")
    success = task_service.mark_task_incomplete(task2.id)
    if success:
        incomplete_task = task_service.get_task_by_id(task2.id)
        print(f"   Marked task {incomplete_task.id} as {'Complete' if incomplete_task.completed else 'Incomplete'}")
    else:
        print("   Failed to mark task as incomplete")

    # Test 7: View all tasks again to see changes
    print("\n6. Testing final view of all tasks...")
    all_tasks = task_service.get_all_tasks()
    for task in all_tasks:
        status = "Complete" if task.completed else "Incomplete"
        print(f"   Task {task.id}: {task.title} [{status}]")

    # Test 8: Delete a task
    print("\n7. Testing delete task functionality...")
    success = task_service.delete_task(task2.id)
    if success:
        print(f"   Deleted task with ID {task2.id}")
    else:
        print("   Failed to delete task")

    # Test 9: View tasks after deletion
    print("\n8. Testing view after deletion...")
    all_tasks = task_service.get_all_tasks()
    if all_tasks:
        for task in all_tasks:
            status = "Complete" if task.completed else "Incomplete"
            print(f"   Task {task.id}: {task.title} [{status}]")
    else:
        print("   No tasks remaining")

    print("\nAll tests completed successfully! ✓")

if __name__ == "__main__":
    test_application()