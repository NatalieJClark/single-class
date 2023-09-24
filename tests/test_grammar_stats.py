import pytest
from lib.grammar_stats import GrammarStats

"""
Given a string with a starting capital and an ending full stop
#check returns True
"""
def test_starting_capital_and_ending_full_stop_returns_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, I'm Natalie.")
    assert result == True

"""
Given a string with a starting capital and an ending question mark
#check returns True
"""
def test_starting_capital_and_ending_question_mark_returns_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello, what's your name?")
    assert result == True

"""
Given a string with a starting capital and an ending exclamation mark
#check returns True
"""
def test_starting_capital_and_ending_exclamation_mark_returns_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("What a fine day!")
    assert result == True

"""
Given a string with a starting capital, but an ending comma
#check returns False
"""
def test_starting_capital_and_ending_comma_returns_false():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("What a fine day,")
    assert result == False

"""
Given a string with a starting lowercase, and an ending full stop
#check returns False
"""
def test_starting_lowercase_and_ending_full_stop_returns_false():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello world.")
    assert result == False

"""
Given an empty text
#check raises an error
"""
def test_given_empty_text_raises_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    assert str(e.value) == "Cannot check an empty text"

"""
Given one valid text
#percentage_good returns 100 after #check called on text
"""
def test_percentage_100_after_one_valid_text_checked():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello, I'm Natalie.")
    result = grammar_stats.percentage_good()
    assert result == 100

"""
Given one invalid text
#percentage_good returns 0 after #check called on text
"""
def test_percentage_0_after_one_invalid_text_checked():
    grammar_stats = GrammarStats()
    grammar_stats.check("hello, I'm Natalie")
    result = grammar_stats.percentage_good()
    assert result == 0

"""
Given one valid and then one invalid text
#percentage_good is 100 after #check
#percentage_good is 50 after second #check
"""
def test_percentage_updates_after_second_check():
    grammar_stats = GrammarStats()
    grammar_stats.check("What a fine day!")
    assert grammar_stats.percentage_good() == 100
    grammar_stats.check("hello world.")
    assert grammar_stats.percentage_good() == 50





