import pytest
from stream_models.stream import Stream
from stream_models.stream_node import StreamNode
from uuid import uuid4

STREAM_ID = str(uuid4())
OTHER_STREAM_ID = str(uuid4())

SONG_ID = str(uuid4())
STREAM_SONG_ID = f"{STREAM_ID}_{SONG_ID}"
SONG_URI = "spotify:track:6MA8bZDOKnJ0s6niH7INtO"
OTHER_SONG_URI = "spotify:track:0X4YYZtZcvqNqYIpMd93IT"


class TestStreamNode:

    def test_disconnect_self(self):
        stream = Stream(SONG_URI)
        middle_song = stream.add_song(OTHER_SONG_URI)
        last_song = stream.add_song(SONG_URI)
        middle_song.disconnect_self()

        assert stream.get_first_song().get_next_song() == last_song
