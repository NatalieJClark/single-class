from lib.gratitudes import Gratitudes
"""
Given multiple gratitudes
We can see a nice list of them
"""
def test_given_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    gratitudes.add("my family")
    gratitudes.add("my friends")
    result = gratitudes.format()
    assert result == "I am grateful for: my health, my family, and my friends."
