# Lesson 8.3 Quiz: Getting Started with IDB

#### Quiz:
Adding content to the object store in indexedDB.

#### Initial Setup:
- `git reset --hard`
- `git checkout page-skeleton`

#### Objective:
- Add to the keyval object store
- key: favorite animal
- value: my favorite animal
- Use test ID: `idb-animal`

#### Solution:
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
  var tx = db.transaction('keyval','readwrite');
  var keyValStore = tx.objectStore('keyval');
  keyValStore.put('auk','favoriteAnimal');
  return tx.complete;
}).then(function() {
  console.log('Added a flightless bird as my favorite animal to keyval');
});
```

#### Notes:
Further Lesson:
```
import idb from 'idb';

var dbPromise = idb.open('test-db', 3, function(upgradeDb) {
  switch(upgradeDb.oldVersion) {
    case 0:
      var keyValStore = upgradeDb.createObjectStore('keyval');
      keyValStore.put("world", "hello");
    case 1:
      upgradeDb.createObjectStore('people', { keyPath: 'name' });
    case 2:
      var peopleStore = upgradeDb.transaction.objectStore('people');
      peopleStore.createIndex('animal', 'favoriteAnimal');
  }
  // TODO: create an index on 'people' named 'age', ordered by 'age'
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
  var tx = db.transaction('keyval', 'readwrite');
  var keyValStore = tx.objectStore('keyval');
  keyValStore.put('cat', 'favoriteAnimal');
  return tx.complete;
}).then(function() {
  console.log('Added favoriteAnimal:cat to keyval');
});

// add people to "people"
dbPromise.then(function(db) {
  var tx = db.transaction('people', 'readwrite');
  var peopleStore = tx.objectStore('people');

  peopleStore.put({
    name: 'Sam Munoz',
    age: 25,
    favoriteAnimal: 'dog'
  });

  peopleStore.put({
    name: 'Susan Keller',
    age: 34,
    favoriteAnimal: 'cat'
  });

  peopleStore.put({
    name: 'Lillie Wolfe',
    age: 28,
    favoriteAnimal: 'dog'
  });

  peopleStore.put({
    name: 'Marc Stone',
    age: 39,
    favoriteAnimal: 'cat'
  });

  return tx.complete;
}).then(function() {
  console.log('People added');
});

// list all cat people
dbPromise.then(function(db) {
  var tx = db.transaction('people');
  var peopleStore = tx.objectStore('people');
  var animalIndex = peopleStore.index('animal');

  return animalIndex.getAll('cat');
}).then(function(people) {
  console.log('Cat people:', people);
});

// TODO: console.log all people ordered by age
```
With annotations:
```
import idb from 'idb';

var dbPromise = idb.open('test-db', 3, function(upgradeDb) { //GC Comment: upgraded to 3rd version.
  switch(upgradeDb.oldVersion) { //GC Comment: The versions need to be separated, because we can't re-create a store with the same name.
    case 0:
      var keyValStore = upgradeDb.createObjectStore('keyval');
      keyValStore.put("world", "hello");
    case 1:
      upgradeDb.createObjectStore('people', { keyPath: 'name' }); //GC Comment: We are creating a people object store. Specifying a key path of name. We are assuming all names will be unique.
    case 2:
      var peopleStore = upgradeDb.transaction.objectStore('people'); //GC Comment: We need to setup a transaction.
      peopleStore.createIndex('animal', 'favoriteAnimal'); //GC Comment: Then create an index call animal from the favoriteAnimal values.
  }
  // TODO: create an index on 'people' named 'age', ordered by 'age'
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
  var tx = db.transaction('keyval', 'readwrite');
  var keyValStore = tx.objectStore('keyval');
  keyValStore.put('cat', 'favoriteAnimal');
  return tx.complete;
}).then(function() {
  console.log('Added favoriteAnimal:cat to keyval');
});

// add people to "people"
dbPromise.then(function(db) {
  var tx = db.transaction('people', 'readwrite');
  var peopleStore = tx.objectStore('people'); //GC Comment: Starting the transaction.

  peopleStore.put({ //GC Comment: Notice we are not providing a key this time. That's because we specified the name as the key.
    name: 'Sam Munoz',
    age: 25,
    favoriteAnimal: 'dog'
  });

  peopleStore.put({
    name: 'Susan Keller',
    age: 34,
    favoriteAnimal: 'cat'
  });

  peopleStore.put({
    name: 'Lillie Wolfe',
    age: 28,
    favoriteAnimal: 'dog'
  });

  peopleStore.put({
    name: 'Marc Stone',
    age: 39,
    favoriteAnimal: 'cat'
  });

  return tx.complete; //GC Comment: After we're done adding content. We complete the transaction.
}).then(function() {
  console.log('People added');
});

// list all cat people
dbPromise.then(function(db) {
  var tx = db.transaction('people');
  var peopleStore = tx.objectStore('people');
  var animalIndex = peopleStore.index('animal'); //GC Comment: Here we are calling the animal index.

  return animalIndex.getAll('cat'); //GC Comment: We are only returning cat animals using .getAll(). .getAll() with no parameters will return everything.
}).then(function(people) { //GC Comment: getAll resolves with the people's values.
  console.log('Cat people:', people);
});

// TODO: console.log all people ordered by age
```
- - -
Next up: [Quiz: More IDB](ND024_Part3_Lesson08_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
