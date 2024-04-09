import json

from .stream_node import StreamNode
from .stream import Stream
from . import stream_utils

class StreamStore:
    def __init__(self):
        self.store = {}

    def __str__(self):
        return str(self.store)

    def store_stream(self, stream: Stream):
        stream_id = stream.get_stream_id()
        self.store[stream_id] = {"stream_obj": stream, "stream_song_map": {}}

    def get_stream(self, stream_id) -> Stream:
        stream = self.store.get(stream_id,{}).get("stream_obj")
        if not stream:
            raise KeyError(f"Could not get stream {stream_id}.")
        return stream

    """
    stores a reference to a song node in the stream store with key = 'stream_id'
    """
    def store_stream_song(self, stream_node: StreamNode) -> None:
        stream_id = stream_node.get_stream_id()
        stream_song_id = stream_node.get_stream_song_id()
        self.store[stream_id]["stream_song_map"][stream_song_id] = stream_node

    def get_stream_song(self, stream_song_id: str) -> StreamNode:
        stream_id, song_id = stream_utils.parse_stream_song_id(stream_song_id)
        stream_song = self.store.get(stream_id, {}).get("stream_song_map", {}).get(stream_song_id)
        if not stream_song:
            raise KeyError(f"Could not get stream_song_id {stream_song_id}.")
        return stream_song

    def delete_stream_song(self, stream_song_id) -> None:
        stream_id, song_id = stream_utils.parse_stream_song_id(stream_song_id)
        node_to_delete = self.get_stream_song(stream_song_id)
        if not node_to_delete:
            raise KeyError(f"Could not delete stream_song_id {stream_song_id}.")
        node_to_delete.disconnect_self()

        del self.store[stream_id]["stream_song_map"][stream_song_id]
