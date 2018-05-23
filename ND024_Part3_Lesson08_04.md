# Lesson 8.4 Quiz: More IDB

#### Quiz:
Creating an index in IndexedDB

#### Initial Setup:
- `git reset --hard`
- `git checkout task-idb-people`
- file `public/js/idbtest/index.js`

#### Objective:
- Create an index where they're ordered by age.
- Create index in upgrade function.
- Then log out all the people in that order.
- Use test ID: `idb-age`

#### Solution:
```
import idb from 'idb';

var dbPromise = idb.open('test-db', 4, function(upgradeDb) {
  switch(upgradeDb.oldVersion) {
    case 0:
      var keyValStore = upgradeDb.createObjectStore('keyval');
      keyValStore.put("world", "hello");
    case 1:
      upgradeDb.createObjectStore('people', { keyPath: 'name' });
    case 2:
      var peopleStore = upgradeDb.transaction.objectStore('people');
      peopleStore.createIndex('animal', 'favoriteAnimal');
    case 3:
      var peopleStore = upgradeDb.transaction.objectStore('people');
      peopleStore.createIndex('age', 'age');
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
dbPromise.then(function(db) {
  var tx = db.transaction('people');
  var peopleStore = tx.objectStore('people');
  var ageIndex = peopleStore.index('age');

  return ageIndex.getAll();
}).then(function(people) {
  console.log('People from young to old:', people);
});
```

#### Notes:
Further lesson.
- `git reset --hard`
- `git checkout idb-cursoring`
- We can use cursors to iterate through the index.
- `.openCursor()` returns a promise for a cursor object representing the first item in the index or undefined if there isn't one.
- `.advance()` we enter the number we want to jump ahead in the index.
- `cursor.value` is the entry we want to access.
- `cursor.update(newValue)` can change the value.
- `cursor.delete()` will delete the entry.
- `cursor.continue()` to go on to the next cursor.

```
// Using cursors
dbPromise.then(function(db) {
  var tx = db.transaction('people');
  var peopleStore = tx.objectStore('people');
  var ageIndex = peopleStore.index('age'); //GC Comment: Same thing we need to open a transaction and get access to the index we want.

  return ageIndex.openCursor(); //GC Comment: This is how we open the cursor on the index. This returns a promise for a cursor object representing the first item in the index or undefined if there isn't one.
}).then(function(cursor) {
  if (!cursor) return; //GC Comment: If cursor is undefined, we'll return.
  return cursor.advance(2); //GC Comment: .advance() is optional. We can use this to jump ahead in the index.
}).then(function logPerson(cursor) { //GC Comment: We'll name the function so we can call it again.
  if (!cursor) return; //GC Comment: We're always checking if cursor is still define.
  console.log("Cursored at:", cursor.value.name); //GC Comment: cursor.value will give us the person. cursor.value.name is the name of that person.
  // I could also do things like:
  // cursor.update(newValue) to change the value, or
  // cursor.delete() to delete this entry
  return cursor.continue().then(logPerson); //GC Comment: We're going to call this same function again. It'll return when cursor is no longer defined.
}).then(function() {
  console.log('Done cursoring');
});
```

- - -
Next up: [Using the IDB Cache and Display Entries](ND024_Part3_Lesson08_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
