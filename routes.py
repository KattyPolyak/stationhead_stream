from flask import Flask

app = Flask(__name__)

VERSION = "v1"
BASE_ROUTE = f"/api/{VERSION}"


@app.route(f"{BASE_ROUTE}/health")
def health():
    return "healthy"

@app.post(f"{BASE_ROUTE}/stream")
def add_to_playlist(message):
    return

@app.delete(f"{BASE_ROUTE}/stream")
def delete_from_playlist(message):
    return

@app.get(f"{BASE_ROUTE}/stream")
def get_stream_queue():
    return

@app.get(f"{BASE_ROUTE}/stream/next")
def get_next_song():
    return