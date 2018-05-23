# Lesson 8.1 Introducing the IDB Promised Library

When we receive new Weets, we want to display them and also store them. We also want to remove old posts. A database is the best model for this. 

The web platform has a database called indexDB and it's fair to say it has a bit of a bad reputation. IDB is similar to NoSQL.

With IndexDB, we can have multiple databases with whatever name we give them. But we're only going to be creating one. Generally we'll only have one database per app.

Our database can contain multiple object stores, generally one for each kind of thing we want to store. An object store contains multiple values. These can be JavaScript objects, strings, numbers, dates, or arrays.

Items in the object's store can have a separate primary key or we can assign a property of values to be the key. The key must be unique within an object store. It becomes the way to identify a particular object. Later we can get, set, add, remove, iterate over items in object stores as part of a transaction. 

All read or write operations in IndexDB must be part of a transaction. This means that if we create a transaction for a series of steps and one of the actions fail, none of them are applied. The state of the database would be as if none of the steps happened. 

We can also create indexed within an object store, which provides a different view of the same data ordered by particular properties. The model here is similar to a lot of databases which makes a lot of sense. 

The browser support is good as well with every major browser supporting it. IndexDB has a bad reputation because of the API. It's asynchronous but predates promises, so it invented its own. 

In this course, we'll use IndexDB Promised. A small library that mirrors IndexDB API but uses promises rather than events.

- - -
Next up: [Getting Started with IDB](ND024_Part3_Lesson08_02.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
