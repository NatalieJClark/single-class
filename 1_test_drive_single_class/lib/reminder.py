class Reminder():
    def __init__(self, name):
        self._name = name

    def remind_me_to(self, task):
        self._task = task

    def remind(self):
        return f"{self._name}, {self._task}!"
    

reminder = Reminder("Natalie")
reminder.remind_me_to("walk the dog")
print(reminder.remind())


