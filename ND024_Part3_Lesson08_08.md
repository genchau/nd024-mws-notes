# Lesson 8.8 Quiz: Cleaning IDB

#### Quiz:
We need to clean up the database and delete old posts.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-clean-db`
- file: `public/js/main/IndexController.js`

#### Objective:
- Ensure the database only has 30 weets
- _onSocketMessage.
- No more than 30 items in the store.
- Use test ID: `idb-clean`

#### Solution:
```
// called when the web socket sends message data
IndexController.prototype._onSocketMessage = function(data) {
  var messages = JSON.parse(data);

  this._dbPromise.then(function(db) {
    if (!db) return;

    var tx = db.transaction('wittrs', 'readwrite');
    var store = tx.objectStore('wittrs');
    messages.forEach(function(message) {
      store.put(message);
    });

    // TODO: keep the newest 30 entries in 'wittrs',
    // but delete the rest.
    //
    // Hint: you can use .openCursor(null, 'prev') to
    // open a cursor that goes through an index/store
    // backwards.
    const index = store.index('by-date');
    return index.openCursor(null, 'prev').then(function(cursor) {
      if (!cursor) return;
      return cursor.advance(30);
    }).then(function deleteCursor(cursor) {
      if (!cursor) return;
      cursor.delete();
      return cursor.continue().then(deleteCursor);
    });

  });

  this._postsView.addPosts(messages);
};
```

#### Notes:


#### To-Do List:
- [X] Unobtrusive app updates
- [X] Get the user onto the latest version
- [X] Continually update cache of posts
- [ ] Cache photos
- [ ] Cache avatars


- - -
Next up: [Cache Photos](ND024_Part3_Lesson08_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
