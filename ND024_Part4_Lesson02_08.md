# Lesson 2.8 REST

When writing web apps, we will encounter a lot of API's we'll have to talk to. Some of them might be JavaScript API's that don't involve much more than calling a function in JavaScript, other API's are provided by third parties and require us to make HTTP requests ourselves. A RESTful API is one that follows a design called REST that works especially well with HTTP. 

REST stands for:
- REpresentational
- State
- Transfer

But let's be honest that isn't really a very descriptive name. Not all API's follow the REST pattern but many do. So, let's take a look at the underlying concept. The basic entities are collections and objects inside those collections. The general pattern to retrieve items from collections is using a GET request with both the 'collection name' and the unique 'item name' in that collection. For example, if I wanted to look up Richard, I'd send this request and the server would get the record containing the data about Richard. If I wanted to update the data in that record, I'd use a PUT request and append the updated information to the request. Every subsequent GET request should now yield the updated record. A POST request is used very similarly with PUT, but instead of updating existing records, we use it to create new records. Notice that we do not provide the name under which the new record will be created, but let the server make that choice for us. The response to the POST request is usually a redirect to the newly created record. And lastly DELETE is just what you think it is. It removes items from the collection.

- - -
Next up: [Quiz: REST Quiz](ND024_Part4_Lesson02_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
