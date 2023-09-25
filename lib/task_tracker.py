class TaskTracker():
    def __init__(self):
        self._task_list = []

    def add(self, task):
        # parameters:
        #   task: a string, representing a task
        self._task_list.append(task)
    
    def list_incomplete(self):
        # returns:
        #   list_incomplete: a list of all task to be completed
        return self._task_list

    def mark_complete(self, index):
        # parameters:
        #   index: an integer represented the list index of the completed task
        # side-effect:
        #   removes the task, at the given index, from the list of tasks
        if index < 0 or index >= len(self._task_list) :
            raise Exception("No such task to mark complete")
        self._task_list.pop(index)
    