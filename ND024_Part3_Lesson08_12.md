# Lesson 8.12 Quiz: Cleaning Photo Cache Quiz

#### Quiz:
Implement cleanImageCache, which brings together indexedDB and the cache API.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-clean-photos`
- file: `indexController.js`

#### Objective:
- implement _cleanImageCache.
- Get all the messages from the database,
- Look at what photos they need,
- get rid of photos we don't need in images cache
- Use test ID: `cache-clean`

#### Solution:
My not so elegant solution:
```
IndexController.prototype._cleanImageCache = function() {
  return this._dbPromise.then(function(db) {
    if (!db) return;

    // TODO: open the 'wittr' object store, get all the messages,
    // gather all the photo urls.
    //
    // Open the 'wittr-content-imgs' cache, and delete any entry
    // that you no longer need.
    let listOfWittrPhotosToKeep = [];

    const store = db.transaction('wittrs').objectStore('wittrs');
    store.getAll().then(function(weets) {
      for (const weet of weets) {
        if (weet.photo) {
          listOfWittrPhotosToKeep.push(weet.photo);
        }
      }
     
      caches.open('wittr-content-imgs').then(function(cache) {
        cache.keys().then(function(photosCached) {
          for (const photo of photosCached) {
            if (!listOfWittrPhotosToKeep.includes(photo.url.slice(21))) {
              cache.delete(photo);
            }
          }
        });
      });
    })
  });
};
```

#### Notes:


Here's what Jake did to set us up initially:
```
this._cleanImageCache();
setInterval(function() {
  indexController._cleanImageCache();
}, 1000 * 60 * 5 );
...
IndexController.prototype._cleanImageCache = function() {

};
```

- - -
Next up: [Quiz: Caching Avatars](ND024_Part3_Lesson08_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
