 # Design Considerations
 
## Selection of Data Structure for Song Queue

### Array
Pros:
- Constant time O(1) for adding new songs to end of array
- Builtin data structure
- Pointer can be used to keep track of the current position in the queue

Cons:
- Removing a song from queue is more complex
   - Options include using a sentinel value to replace songs which are removed. 
      If the program encounters a sentinel value, that position will be skipped. 
     - The removal of many songs could mean slowing down playback while the next song is found. 
   - Another option is shifting every song after the removed song to the left
- 

### Deque
Python implements the deque as a doubly linked list

Pros:
- Deque offers easy constant time O(1) additions or removals from the left and right

Cons:
- Removing multiple elements by position at the same time is not inherently supported
   - A single element can be removed at linear time O(n). 
   - Once an element is removed, the positions of elements after the element have changed

### Doubly Linked List and hashmap with reference to the streams and song nodes

Pros:
- Constant time get song, add song, and delete song implementation
- Deleting a song from the middle of the list in constant time is possible by storing the references to the song nodes
which then disconnect themselves from thew stream.

Cons:
- Additional boilerplate and testing required due to not using a builtin data structure. 
- Additional space used compared to deque/array implementations
