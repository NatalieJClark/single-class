# Music Tracker Class Design Recipe

## 1. Descibe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

```python
class MusicTracker():
    def __init__(self):
        # parameters:
        #   track_list: empty list

    def add(self, track):
        # parameters:
        #   track: string, representing a track
        # side effect:
        #   track is added to the track_list

    def list_listened(self):
        # returns:
        #   track_list: list representing all the tracks listened to

```

## 3. Create Example as Tests

```python
import pytest

""" 
Initially there are no tracks in the track list
"""
music_tracker = MusicTracker()
music_tracker.list_listened() => []

"""
When one track is added
The track is reflected in the list_listened
"""
music_tracker = MusicTracker()
music_tracker.add("Track 1")
music_tracker.list_listened() => ["Track 1"]

"""
When multiple tracks are added
All the added tracks are reflected in the list_listened
"""
music_tracker = MusicTracker()
music_tracker.add("Track 1")
music_tracker.add("Track 2")
music_tracker.add("Track 3")
music_tracker.list_listened() => ["Track 1", "Track 2", "Track 3"]

"""
When an empty track name is added
This raises an error
And the list_listened remains unchanged
"""
music_tracker = MusicTracker()
with pytest.raises(Exception) as e:
    music_tracker.add("")
assert str(e.value) == "Cannot add an empty track name"

```

## 4. Implement the Behaviour