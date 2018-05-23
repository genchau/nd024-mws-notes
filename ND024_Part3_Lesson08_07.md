# Lesson 8.7 Quiz: Using IDB 2

#### Quiz:


#### Initial Setup:
- `git reset --hard`
- `git checkout task-show-stored`
- file: `public/JS/main/indexController.js.`

#### Objective:
- _showCachedMessages
- get the messages out of the database 
- pass them to the method indexController._postsView.addPost(messages)
- getAll() will get all messages as an array.
- Date is descended order
- Bump the cached version number in service worker.
- 
- Use test ID: `idb-show`

#### Solution:
My implementation.
```
IndexController.prototype._showCachedMessages = function() {
  var indexController = this;
  let messages = [];

  return this._dbPromise.then(function(db) {
    // if we're already showing posts, eg shift-refresh
    // or the very first load, there's no point fetching
    // posts from IDB
    if (!db || indexController._postsView.showingPosts()) return;

    // TODO: get all of the wittr message objects from indexeddb,
    // then pass them to:
    // indexController._postsView.addPosts(messages)
    // in order of date, starting with the latest.
    // Remember to return a promise that does all this,
    // so the websocket isn't opened until you're done!
    const tx = db.transaction('wittrs');
    const wittrsStore = tx.objectStore('wittrs');
    const dateIndex = wittrsStore.index('by-date');

    return dateIndex.openCursor(null,"prev");
  }).then(function addToMessages(cursor) {
    if (!cursor) return;

    messages.push(cursor.value);
    return cursor.continue().then(addToMessages);
  }).then(function() {
    indexController._postsView.addPosts(messages);
  });
};
```
Instructor;s implementation:
```
IndexController.prototype._showCachedMessages = function() {
  var indexController = this;

  return this._dbPromise.then(function(db) {
    // if we're already showing posts, eg shift-refresh
    // or the very first load, there's no point fetching
    // posts from IDB
    if (!db || indexController._postsView.showingPosts()) return;

    // TODO: get all of the wittr message objects from indexeddb,
    // then pass them to:
    // indexController._postsView.addPosts(messages)
    // in order of date, starting with the latest.
    // Remember to return a promise that does all this,
    // so the websocket isn't opened until you're done!
    const index = db.transaction('wittrs')
      .objectStore('wittrs').index('by-date');

    return index.getAll().then(function(messages) {
      indexController._postsView.addPosts(messages.reverse());
    });
  });
};
```

#### Notes:

- - -
Next up: [Quiz: Cleaning IDB](ND024_Part3_Lesson08_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
