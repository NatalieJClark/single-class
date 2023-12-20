import pytest
from lib.diary_entry import DiaryEntry

"""
Given an empty title
Raises an error
"""
def test_given_empty_title_raise_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "my contents")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title or contents"

"""
Given an empty contents
Raises an error
"""
def test_given_empty_contents_raise_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("My title", "")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title or contents"


"""
Given a title and contents
#format returns a formatted entry like
"My title: These are the contents"
"""
def test_format_given_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

"""
Given a title and a contents
#count_words returns the number of words in the title and contents
"""
def test_counts_words_in_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

"""
Given a wpm of 2
And a contents with 2 words
#reading_time returns 1 minute
"""
def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
And a contents with 3 words
#reading_time returns 2 minutes
"""
def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a wpm of 0
Raises an error
"""
def test_reading_time_with_zero_wpm():
    diary_entry = DiaryEntry("My Title", "Some more contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"

"""
Given a contents of six words
And a wpm of 2
And a minutes of 1
#reading_chunk returns the first two words of contents
"""
def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

"""
Given a contents of six words
And a wpm of 2
And a minutes of 2
#reading_chunk returns the first four words of contents
"""
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

"""
Given a contents of six words
And a wpm of 2 and 1 minute
First time #reading_chunk returns "one two"
Second time #reading_chunk returns "three four"
"""
def test_reading_chunk_with_two_wpm_and_one_minutes_called_twice():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"

"""
Given a contents of six words
And a wpm of 2 and 1 minute
First time #reading_chunk(2, 1) returns "one two"
Second time #reading_chunk(1, 1) returns "three four"
Third time #reading_chunk returns(2, 1) "five six"
"""
def test_reading_chunk_with_two_wpm_and_one_minutes_called_three_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(1, 1) == "three"
    assert diary_entry.reading_chunk(2, 1) == "four five"

"""
Given a contents of six words
If #reading_chunk is called repeatedly
The last chunk isthe last words in the contents, even if shorter than could be read
The next chunk after that is at the start again
"""
def test_reading_chunk_restarts_contents_after_multiple_calls():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"

"""
Given a contents of six words
If #reading_chunk is called repeatedly, with an exact ending
The last chunk is the last words in the contents
The next chunk after that is at the start again
"""
def test_reading_chunk_restarts_contents_after_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
