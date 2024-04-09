import http
import json

from flask import Flask, request
from .stream_models.stream_store import StreamStore
from .stream_models.stream import Stream
from .stream_models.stream_node import StreamNode
from .stream_models import stream_utils
from markupsafe import escape

app = Flask(__name__)

stream_store = StreamStore()

VERSION = "v1"
BASE_ROUTE = f"/api/{VERSION}"


@app.route(f"{BASE_ROUTE}/health")
def health():
    return "healthy"


@app.post(f"{BASE_ROUTE}/stream")
def create_stream():
    req = request.get_json()
    first_song = req.get("song_uri")
    stream = Stream(first_song)
    stream_store.store_stream(stream)
    stream_store.store_stream_song(stream.get_first_song())
    response = {"stream_id": stream.get_stream_id()}
    return json.dumps(response)


@app.delete(f"{BASE_ROUTE}/stream")
def delete_from_playlist():
    message_dict = request.get_json()
    message_stream_id = message_dict.get("stream_id")
    song_id_list = message_dict.get("song_id_list")
    for stream_song_id in song_id_list:
        stream_id, _ = stream_utils.parse_stream_song_id(stream_song_id)
        if stream_id != message_stream_id:
            raise Exception("Removal of songs from this stream is not permitted")
        song_to_remove = stream_store.get_stream_song(stream_song_id)
        stream = stream_store.get_stream(stream_id)
        if song_to_remove:
            if song_to_remove == stream.get_curr_song():
                stream.set_curr_song(song_to_remove.next_song)
            song_to_remove.disconnect_self()
    return {}


@app.post(f"{BASE_ROUTE}/stream/<stream_id>")
def add_song_to_playlist(stream_id):
    clean_id = escape(stream_id)
    song_uri = request.get_json().get("song_uri")

    stream = stream_store.get_stream(clean_id)
    new_node = stream.add_song(song_uri)
    stream_store.store_stream_song(new_node)

    return {"stream_song_id": new_node.get_stream_song_id()}


@app.get(f"{BASE_ROUTE}/stream/<stream_id>/next")
def get_next_song(stream_id):
    clean_id = escape(stream_id)

    try:
        stream = stream_store.get_stream(clean_id)
        next_song = stream.get_next_song()
        song_uri = next_song.get_song_uri()
    except Exception as e:
        if str(e) == "No songs remaining":
            song_uri = "No songs remaining"
        else:
            return {"error": str(e)}
    response = {"song_uri": song_uri}
    return json.dumps(response)

