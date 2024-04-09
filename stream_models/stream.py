from .stream_node import StreamNode
from . import stream_utils
from uuid import uuid4


class Stream:
    def __init__(self, first_song_uri: str):
        self.stream_id = str(uuid4())
        self.first_song = StreamNode(self.stream_id, first_song_uri)
        self.last_song = self.first_song
        self.curr_song = self.first_song

    def __str__(self):
        output = ""
        curr_node = self.first_song
        while curr_node:
            output = output + str(curr_node)
            curr_node = curr_node.get_next_song()
        return output

    """
    Compare the stream objects for StreamNode song_id in correct order
     if not the same Stream object. 
    """
    def get_stream_id(self) -> str:
        return self.stream_id

    def get_first_song(self) -> StreamNode:
        return self.first_song

    def get_last_song(self) -> StreamNode:
        return self.last_song

    """
    returns the next song that would be played but does not change the stream state
    """
    def get_curr_song(self) -> StreamNode:
        return self.curr_song

    def set_first_song(self, song_node: StreamNode) -> None:
        self.first_song = song_node

    def set_last_song(self, song_node: StreamNode) -> None:
        self.last_song = song_node

    def set_curr_song(self, song_node: StreamNode) -> None:
        self.curr_song = song_node

    """
    returns the current song. makes the current song the next song 
    """
    def get_next_song(self) -> StreamNode:
        if self.curr_song is None:
            raise Exception("No songs remaining")

        if not self.is_last_song():
            self.curr_song = self.curr_song.next_song
            return self.curr_song.get_previous_song()
        else:
            self.curr_song = None
            return self.last_song

    def is_last_song(self) -> bool:
        return self.curr_song is not None and self.curr_song == self.last_song

    def add_song(self, song_uri) -> StreamNode:
        new_song = StreamNode(self.stream_id, song_uri)
        new_song.set_previous_song(self.last_song)
        self.last_song.set_next_song(new_song)
        self.last_song = new_song
        return new_song
