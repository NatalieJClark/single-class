import pytest
from lib.music_tracker import MusicTracker
""" 
Initially there are no tracks in the track list
list_listened returns an empty list
"""
def test_initially_no_tracks_in_list():
    music_tracker = MusicTracker()
    assert music_tracker.list_listened() == []

"""
When one track is added
The track is reflected in the list_listened
"""
def test_add_one_track_reflected_in_list():
    music_tracker = MusicTracker()
    music_tracker.add("Track 1")
    assert music_tracker.list_listened() == ["Track 1"]

"""
When multiple tracks are added
All the added tracks are reflected in the list_listened
"""
def test_add_multiple_tracks_all_reflected_in_list():
    music_tracker = MusicTracker()
    music_tracker.add("Track 1")
    music_tracker.add("Track 2")
    music_tracker.add("Track 3")
    assert music_tracker.list_listened() == ["Track 1", "Track 2", "Track 3"]

"""
When an empty track name is added
This raises an error
And the list_listened remains unchanged
"""
def test_add_empty_track_name_raises_error():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add("")
    assert str(e.value) == "Cannot add an empty track name"
