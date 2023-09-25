class MusicTracker():
    def __init__(self):
        # parameters:
        #   track_list: empty list
        self._track_list = []

    def add(self, track):
        # parameters:
        #   track: string, representing a track
        # side effect:
        #   track is added to the track_list
        if track == "":
            raise Exception("Cannot add an empty track name")
        self._track_list.append(track)

    def list_listened(self):
        # returns:
        #   track_list: list representing all the tracks listened to
        return self._track_list
