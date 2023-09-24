# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TaskTracker():
    def __init__(self):
        # parameters:
        #   task_list: empty list

    def add_task(self, task):
        # parameters:
        #   task: a string, representing a task
    
    def list_incomplete(self)
        # returns:
        #   list_incomplete: a list of all task to be completed

    def mark_complete(self, index):
        # parameters:
        #   index: an integer represented the list index of the completed task
        # side-effect:
        #   removes the task, at the given index, from the list of tasks
    
```



## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python

"""
Initially there are no tasks
"""
tracker = TaskTracker()
tracker.list_incomplete #=> []

"""
When we add a task
It is reflected in the list of tasks
"""
tracker = taskTracker()
tracker.add_task("Walk the dog")
tracker.list_incomplete #=> ["Walk the dog"]

"""
When we add multiple tasks
They are all reflected in the list of tasks
"""
tracker = taskTracker()
tracker.add_task("Walk the dog")
tracker.add_task("Buy milk")
tracker.add_task("Pay bill")
tracker.list_incomplete #=> ["Walk the dog", "Buy milk", "Pay bill"]

"""
When we add multiple tasks
Add mark one as complete
Only the incomplete tasks are reflected in the list of tasks
"""
tracker = taskTracker()
tracker.add_task("Walk the dog")
tracker.add_task("Buy milk")
tracker.add_task("Pay bill")
tracker.mark_complete(1)
tracker.list_incomplete #=> ["Walk the dog", "Pay bill"]

"""
If we try to mark complete a task that doesn't exist (index too low)
It raises an error
"""
tracker = taskTracker()
tracker.add_task("Walk the dog")
tracker.mark_complete(-1) #=> Raises error "No such task to mark complete"
tracker.list_incomplete #=> ["Walk the dog"]

"""
If we try to mark complete a task that doesn't exist (index too high)
It raises an error
"""
tracker = taskTracker()
tracker.add_task("Walk the dog")
tracker.mark_complete(2) #=> Raises error "No such task to mark complete"
tracker.list_incomplete #=> ["Walk the dog"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
