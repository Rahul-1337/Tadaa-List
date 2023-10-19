import pytest
from project import add_task, remove_task_by_number, view_tasks

def test_add_task():
    add_task("Task 1")
    assert view_tasks() == ["Task 1"]

def test_remove_task_by_number():
    add_task("Task 1")
    remove_task_by_number(0)
    assert view_tasks() == ["Task 1"]

def test_view_tasks():
    add_task("Task 1")
    add_task("Task 2")
    assert view_tasks() == ["Task 1", "Task 1", "Task 2"]
