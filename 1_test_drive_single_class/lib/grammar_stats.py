class GrammarStats:
    def __init__(self):
        self._total_checks = 0
        self._total_good_checks = 0
  
    def check(self, text):
        if text == "":
            raise Exception("Cannot check an empty text")
        result = text[0].isupper() and text[-1] in ".?!"
        if result == True:
            self._total_good_checks += 1
        self._total_checks += 1
        return result
  
    def percentage_good(self):
        return (self._total_good_checks / self._total_checks) * 100