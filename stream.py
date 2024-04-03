from stream_node import StreamNode

class Stream:
    def __init__(self):
        self.first_song = StreamNode()
        self.last_song = self.first_song
        self.curr_song = self.first_song

    def get_first_song(self):
        return self.first_song

    def get_last_song(self):
        return self.last_song

    def get_curr_song(self):
        return self.curr_song

    def set_first_song(self, song_id):
        pass

    def set_last_song(self, song_node):
        pass

    def set_curr_song(self, song_node):
        return self.curr_song

    def add_song(self, song_id):
        pass

    def remove_songs(self, positions):
        pass

    def get_next_song(self):
        pass

