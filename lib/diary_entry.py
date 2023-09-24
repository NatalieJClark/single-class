import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0

    def format(self):
        return f"{self._title}: {self._contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        contents_word_count = len(self._contents_words())
        return math.ceil(contents_word_count / wpm)
        

    def reading_chunk(self, wpm, minutes):
        num_words_user_can_read = wpm * minutes
        words_list = self._contents_words()
        if self._read_so_far >= len(words_list):
            self._read_so_far = 0

        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + num_words_user_can_read
        chunk_words = words_list[chunk_start : chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)
    
    def _contents_words(self):
        return self._contents.split()