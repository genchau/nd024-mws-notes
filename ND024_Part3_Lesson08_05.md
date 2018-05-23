# Lesson 8.5 Using the IDB Cache and Display Entries

The plan here is to create a database for Wittr that stores these posts.

When Wittr loads via a service worker, it does so without going to the network. 
- Fetches page skeleton from the cache.
- Then go to network for posts.
We're going to change this.

Instead:
- We'll get posts from the database
- Display them. (We're displaying post content offline first.)
- Then connect the web socket.
- New posts are displayed
- Then added to the database.

First thing we're going to do is populate the database. Then display the contents later.

IndexController.js:
- method for opening the web socket.
- in this method, there's an event listener.
- then it goes off to onSocketMessage.
- onSocketMessage parses the data with JSON.
- Then passes it to addPosts.
- var messages is what we need, it has all the posts.
- We'll store the messages into IndexedDB.
- id is the primary key.
- We want it sorted by date order.

- - -
Next up: [Quiz: Using IDB Cache](ND024_Part3_Lesson08_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
