import pytest
from stream_models.stream import Stream
from uuid import uuid4

STREAM_ID = str(uuid4())
OTHER_STREAM_ID = str(uuid4())

SONG_ID = str(uuid4())
STREAM_SONG_ID = f"{STREAM_ID}_{SONG_ID}"
SONG_URI = "spotify:track:6MA8bZDOKnJ0s6niH7INtO"
OTHER_SONG_URI = "spotify:track:0X4YYZtZcvqNqYIpMd93IT"


class TestStream:

    def test_get_next_song__success(self):
        actual = Stream(SONG_URI)
        actual.add_song(OTHER_SONG_URI)
        assert actual.get_next_song().get_song_uri() == SONG_URI

    def test_get_next_song__last_song__success(self):
        actual = Stream(SONG_URI)
        actual.add_song(OTHER_SONG_URI)
        actual.get_next_song()
        assert actual.get_next_song().get_song_uri() == OTHER_SONG_URI

    def test_get_next_song__failure(self):
        actual = Stream(SONG_URI)
        actual.get_next_song()
        with pytest.raises(Exception):
            actual.get_next_song()

    def test_add_song__success(self):
        actual = Stream(SONG_URI)
        actual.add_song(OTHER_SONG_URI)
        last_song = actual.add_song(OTHER_SONG_URI)
        assert actual.get_last_song() == last_song

    def test_is_last_song__true(self):
        actual = Stream(SONG_URI)
        assert actual.is_last_song()

    def test_is_last_song_multiple_songs__true(self):
        actual = Stream(SONG_URI)
        actual.add_song(SONG_URI)
        actual.get_next_song()
        assert actual.is_last_song()

    def test_is_last_song__false(self):
        expected = Stream(SONG_URI)
        for i in range(3):
            expected.add_song(SONG_URI)
        assert not expected.is_last_song()



if __name__ == '__main__':
    pass
