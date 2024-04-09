import pytest
from stream_models.stream import Stream
from stream_models.stream_store import StreamStore
from stream_models.stream_node import StreamNode
from uuid import uuid4

SONG_URI = 'spotify:track:6MA8bZDOKnJ0s6niH7INtO'
STREAM = Stream(SONG_URI)
STREAM_ID = STREAM.get_stream_id()
STREAM_SONG_ID = STREAM.get_first_song().get_stream_song_id()


class TestStreamStore:

    def test_store_stream__success(self):
        store = StreamStore()
        store.store_stream(STREAM)
        assert STREAM_ID in store.store

    def test_store_stream_song__success(self):
        store = StreamStore()
        new_song = StreamNode(STREAM_ID, SONG_URI)
        store.store_stream(STREAM)
        store.store_stream_song(new_song)
        assert store.get_stream_song(new_song.get_stream_song_id()) == new_song

    def test_get_stream_song__failure(self):
        store = StreamStore()
        with pytest.raises(Exception):
            store.get_stream_song(STREAM_SONG_ID)


