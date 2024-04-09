from uuid import uuid4
from . import stream_utils


class StreamNode:
    def __init__(self, stream_id: str, song_uri: str):
        self.song_id = str(uuid4())
        self.stream_song_id = stream_id + "_" + self.song_id
        self.song_uri = song_uri
        self.previous_song = None
        self.next_song = None

    def __str__(self):
        return self.song_id + ":" + self.song_uri

    def get_stream_id(self) -> str:
        stream_id, _ = stream_utils.parse_stream_song_id(self.get_stream_song_id())
        return stream_id

    def get_song_id(self) -> str:
        return self.song_id

    def get_stream_song_id(self) -> str:
        return self.stream_song_id

    def get_song_uri(self) -> str:
        return self.song_uri

    def get_previous_song(self):
        return self.previous_song

    def get_next_song(self):
        return self.next_song

    def set_previous_song(self, song_node) -> None:
        self.previous_song = song_node

    def set_next_song(self, song_node) -> None:
        self.next_song = song_node

    def disconnect_self(self):
        previous_song = self.get_previous_song()
        next_song = self.get_next_song()
        previous_song.next_song = next_song
