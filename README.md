# Stationhead Stream

## Design
- Streams exist as instances of the Stream class (Doubly Linked List). Each Stream has references to its current song,
first song, and last song. 
- Songs exist as instances of StreamNodes. When a song is removed from a stream, the StreamNode disconnects itself from
its previous song and next song by linking its next song to its previous song. 
- The state is maintained by the StreamStore (singleton) and maintains each stream's references separately.

## Manual testing

1. Should be able to add 1+ songs to the queue
    a. Create the initial stream and get back the stream_id of the newly created stream
    ```
    POST http://localhost:5000/api/v1/stream
    message body: {"song_uri": "spotify:track:6MA8bZDOKnJ0s6niH7INtO"}
    ex response: {"stream_id": "05872b72-ee38-4c00-956c-e3731b52831e"}
    ```
    b. Add additional songs to the queue and get back the song_stream_id for this instance of song_uri
    ```
    POST http://localhost:5000/api/v1/stream/05872b72-ee38-4c00-956c-e3731b52831e
    message body: {"song_uri": "spotify:track:6MA8bZDOKnJ0s6niH7INtO"}
    ex response: 
    {
        "stream_song_id": "05872b72-ee38-4c00-956c-e3731b52831e_6a4e7dc4-1687-4c73-9910-f3382106b012"
    }
    ```
   c. the same song_uri can be added multiple times as each instance has its own unique song_stream_id
2. Should be able to remove 1+ songs from the queue
   a. Delete songs from a given stream_id by their song_stream_id
   b. When removing songs from the queue, removing the same song will not remove all entries of that song_uri
       ```
       DELETE http://localhost:5000/api/v1/stream
       message body:
        {
           "stream_id": "05872b72-ee38-4c00-956c-e3731b52831e",
           "song_id_list": ["05872b72-ee38-4c00-956c-e3731b52831e_a3f0e858-d0a7-4bc7-ae91-a0c278b146a8", "05872b72-ee38-4c00-956c-e3731b52831e_cfc002d2-562d-4d42-bd2c-018d2cca46da"]
       }
       ```

## Possible Extensions
Since the stream is implemented as a doubly linked list, a get previous song endpoint could be added. When a stream 
ends, the stream store could traverse a stream and save the exact order of songs which were played to a permanent data
store for VOD creation.
In addition, new streams could be created with the same song uris as another stream instance but in a random order 
by using the song stream map in the stream store.

## Notes 
To productionize this implementation, some missing error handling would need to be added. The stream store could be 
converted to an in memory database like Redis. Interesting metrics to add might be the amount of times a song has been
played or how many listeners a stream has. 

Observability, security and authentication would also need to be added.

