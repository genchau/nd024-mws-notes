# Lesson 8.2 Getting Started with IDB

Remember: If any part of a transaction fails, the transaction will never complete, and it'll be like nothing happened.

```
import idb from 'idb';

var dbPromise = idb.open('test-db', 1, function(upgradeDb) {
  var keyValStore = upgradeDb.createObjectStore('keyval');
  keyValStore.put("world", "hello");
});

// read "hello" in "keyval"
dbPromise.then(function(db) {
  var tx = db.transaction('keyval');
  var keyValStore = tx.objectStore('keyval');
  return keyValStore.get('hello');
}).then(function(val) {
  console.log('The value of "hello" is:', val);
});

// set "foo" to be "bar" in "keyval"
dbPromise.then(function(db) {
  var tx = db.transaction('keyval', 'readwrite');
  var keyValStore = tx.objectStore('keyval');
  keyValStore.put('bar', 'foo');
  return tx.complete;
}).then(function() {
  console.log('Added foo:bar to keyval');
});

dbPromise.then(function(db) {
  // TODO: in the keyval store, set
  // "favoriteAnimal" to your favourite animal
  // eg "cat" or "dog"
});
```

With my annotations:
```
import idb from 'idb'; //GC comment: We are importing idb library.

var dbPromise = idb.open('test-db', 1, function(upgradeDb) { 
//GC comment: var dbPromise to store the database object.  
//GC comment: .open() returns a promise that resolves with a database object.
//GC comment: idb.open, creates the database. idb.open(database name, version, callback function). If version is greater, browser will run this code.
//GC comment: This is the only place to create/remove objects store and indexes.
  var keyValStore = upgradeDb.createObjectStore('keyval'); 
//GC comment: We'll store the object store in keyValStore.  
//GC comment: Then we createObjectStore with the store name.
  keyValStore.put("world", "hello");
//GC comment: Then we add content with .put(). It takes the value first, then the key. value-key than key-value pair.
});

// read "hello" in "keyval"
//GC comment: We need to create a transaction to do anything with the database.
dbPromise.then(function(db) { //GC comment: We are tacking a .then to the object store. 
  var tx = db.transaction('keyval'); //GC comment: var tx will be our transaction. We create a transaction to the keyval store.
  var keyValStore = tx.objectStore('keyval'); //GC comment: On the transaction we tack on the object store keyval. Yes it's a bit repetitive.
  return keyValStore.get('hello'); //GC comment: We use .get() to retrieve our value. .get() takes the key as the parameter. This returns a promise, which resolves to the value.
}).then(function(val) { //GC comment: We take the value and do something with it.
  console.log('The value of "hello" is:', val);
});

// set "foo" to be "bar" in "keyval"
 //GC comment: We'll open another transaction to add another value to the object store.
dbPromise.then(function(db) { //GC comment: Same thing we tack a .then function to the object store.
  var tx = db.transaction('keyval', 'readwrite'); //GC comment: We start the transaction by giving it the object store, and opening it up for readwrite.
  var keyValStore = tx.objectStore('keyval'); //GC comment: We specify the .objectStore.
  keyValStore.put('bar', 'foo'); //GC comment: We are using .put() to add in content. The parameters are (value, key), a bit opposite from intuition of key then value.
  return tx.complete; //GC comment: We complete the transaction. .complete() is a promise that fulfills if and when the transaction completes, and it rejects if it fails.
}).then(function() { //GC comment: Once it completes we'll do something about it.
  console.log('Added foo:bar to keyval');
});

dbPromise.then(function(db) {
  // TODO: in the keyval store, set
  // "favoriteAnimal" to your favourite animal
  // eg "cat" or "dog"
});
```
- - -
Next up: [Quiz: Getting Started with IDB](ND024_Part3_Lesson08_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
