import pytest
from lib.task_tracker import TaskTracker

"""
Initially there are no tasks
"""
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

"""
When we add a task
It is reflected in the list of tasks
"""
def test_add_task_reflected_in_list_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
When we add multiple tasks
They are all reflected in the list of tasks
"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Buy milk")
    tracker.add("Pay bill")
    assert tracker.list_incomplete() == ["Walk the dog", "Buy milk", "Pay bill"]

"""
When we add multiple tasks
Add mark one as complete
Only the incomplete tasks are reflected in the list of tasks
"""
def test_add_multiple_tasks_mark_one_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Buy milk")
    tracker.add("Pay bill")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Pay bill"]

"""
If we try to mark complete a task that doesn't exist (index too low)
It raises an error
"""
def test_mark_index_too_low_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(-1)
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]

"""
If we try to mark complete a task that doesn't exist (index too high)
It raises an error
"""
def test_mark_index_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(1)
    assert str(e.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]


