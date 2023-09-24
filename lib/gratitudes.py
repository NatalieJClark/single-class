class Gratitudes():
    def __init__(self):
        self._gratitudes = []

    def add(self, gratitude):
        self._gratitudes.append(gratitude)

    def format(self):
        gratitudes_string = ""
        for gratitude in self._gratitudes[:-1]:
            gratitudes_string += gratitude + ", "
        gratitudes_string += f"and {self._gratitudes[-1]}."
        return f"I am grateful for: {gratitudes_string}"