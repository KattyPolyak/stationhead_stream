class StreamNode:
    def __init__(self):
        self.song_id = None
        self.prev = None
        self.next = None

    def get_song_id(self):
        return self.song_id

    def get_previous_song(self):
        return self.prev

    def get_next_song(self):
        return self.next

    def set_song_id(self, song_id):
        self.song_id = song_id

    def set_previous_song(self, song_node):
        self.prev = song_node

    def set_next_song(self, song_node):
        self.next = song_node
