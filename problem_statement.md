Problem Statement:
For our live station feature, we need to support the ability for a user to curate and manage a list
of songs to play in a particular order. We want to allow a user to enqueue a list of songs that
play in the correct order for their listeners, and also give that user the ability to add or remove
songs at any time. The songs can be removed from any position within the list, and adding to
the list will append to the end of the list. One-or-many songs can be added/removed at a time.
Also, the user can add the same song as many times as they would like.
Desired Solution:
Build a REST API which maintains the state of the queue for a single user described above
in-memory. The API should implement sufficient endpoints to enable all of the described
functionalities.
General Requirements:
1. Should be able to add 1+ songs to the queue
2. Should be able to remove 1+ songs from the queue
3. Should be able to add the same song multiple times
a. When removing songs from the queue, removing the same song should not
remove all entries of that song
4. The state must be maintained in memory
Notes:
● The solution can be provided in any of the following languages: C#, PHP, Java / Kotlin,
Python, JavaScript / TypeScript, Go
● When in doubt about any requirement, assume the simplest possible solution is desired
● Be prepared to review the code and discuss it in depth with the team