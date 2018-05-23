# Lesson 8.6 Quiz: Using IDB Cache

#### Quiz:
Setup a database for Wittr, and add posts into it.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-idb-store`
- file `public/js/main/indexcontroler.js`

#### Objective:
- In constructor, openDatabase.
- Method is incomplete, we need to return a promise for a database called 'wittr'
- create object store called 'wittrs'
- uses 'id' as its key
- create an index called 'by-date'
- sorted by the time property.
- add messages to the database.
- _onSocketMessage
- add each of the messages to the Wittr store. (Messages are objects, the first one starts at 0. They have properties, avatar, body, id, name, time)
- If our database gets into a bad state, go into dev tools and run `indexedDB.deleteDatabase('wittr')`
- Use test ID: `idb-store`

#### Solution:
```
function openDatabase() {
  // If the browser doesn't support service worker,
  // we don't care about having a database
  if (!navigator.serviceWorker) {
    return Promise.resolve();
  }

  // TODO: return a promise for a database called 'wittr'
  // that contains one objectStore: 'wittrs'
  // that uses 'id' as its key
  // and has an index called 'by-date', which is sorted
  // by the 'time' property
  var dbPromise = idb.open('wittr', 1, function(upgradeDb) {
    switch(upgradeDb.oldVersion) {
      case 0:
        const wittrsStore = upgradeDb.createObjectStore('wittrs', {
          keyPath: 'id'
        });
        wittrsStore.createIndex('by-date', 'time');
    }
  });
  return dbPromise;
}

// called when the web socket sends message data
IndexController.prototype._onSocketMessage = function(data) {
  var messages = JSON.parse(data);

  this._dbPromise.then(function(db) {
    if (!db) return;

    // TODO: put each message into the 'wittrs'
    // object store.
    const tx = db.transaction('wittrs', 'readwrite');
    const wittrsStore = tx.objectStore('wittrs');

    for (const message of messages) {
      console.log("adding message to wittrs store", message);
      wittrsStore.put(message);
    }
    return tx.complete;
  }).then(function() {
    console.log("Finished added messages to wittrs object store.");
  });

  this._postsView.addPosts(messages);
};
```

#### Notes:


- - -
Next up: [Quiz: Using IDB 2](ND024_Part3_Lesson08_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
