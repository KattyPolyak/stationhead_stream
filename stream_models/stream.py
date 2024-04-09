from stream_node import StreamNode
from utils import stream_utils
from uuid import uuid4
from stream_store import StreamStore

class Stream:
    def __init__(self, first_song_uri):
        self.stream_id = str(uuid4())
        self.first_song = StreamNode(self.stream_id, first_song_uri) # TODO: where do we get first song_uri?
        self.last_song = self.first_song
        self.curr_song = self.first_song

    """
    Compare the stream objects for StreamNode song_id in correct order
     if not the same Stream object. 
    """
    def get_stream_id(self):
        return self.stream_id

    def get_first_song(self):
        return self.first_song

    def get_last_song(self):
        return self.last_song

    def get_curr_song(self):
        return self.curr_song

    def set_first_song(self, song_node):
        self.first_song = song_node

    def set_last_song(self, song_node):
        self.last_song = song_node

    def set_curr_song(self, song_node):
        self.curr_song = song_node

    def get_next_song(self) -> StreamNode:
        if not self.is_last_song():
            self.curr_song = self.curr_song.next_song
            return self.curr_song
        else:
            raise Exception("No songs remaining")

    def is_last_song(self):
        return self.curr_song == self.last_song

    def add_song(self, song_uri):
        new_song = StreamNode(self.stream_id, song_uri)
        self.last_song.set_next_song(new_song)
        self.last_song = new_song

    def remove_songs(self, song_id_list):
        for stream_song_id in song_id_list:
            stream_id, _ = stream_utils.parse_stream_song_id(stream_song_id)
            if stream_id != self.stream_id:
                raise Exception("Removal of songs from this stream is not permitted")
            # get the reference of the node from the db
            StreamStore.get_stream_song(stream_song_id) # TODO: where does this get instantiated?
            # unlink the node
            # remove the node reference from the stream store