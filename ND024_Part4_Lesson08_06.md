# Lesson 8.6 Beyond GET and POST

### All of the other methods
The different HTTP methods each stand for different actions that a client might need to perform upon a server-hosted resource. Unlike GET and POST, their usage isn't built into the normal operation of web browsers; following a link is always going to be a GET request, and the default action for submitting an HTML form will always be a GET or POST request.

However, other methods are available for web APIs to use, for instance from client code in JavaScript. If you want to use other methods in your own full-stack applications, you'll have to write both server-side code to accept them, and client-side JavaScript code to make use of them.

### PUT for creating resources
The HTTP PUT method can be used for creating a new resources. The client sends the URI path that it wants to create, and a piece of data in the request body. A server could implement PUT in a number of different ways — such as storing a file on disk, or adding records to a database. A server should respond to a PUT request with a 201 Created status code, if the PUT action completed successfully. After a successful PUT, a GET request to the same URI should return the newly created resource.

#### QUESTION 1 OF 3
PUT can be used for actions such as uploading a file to a web site. However, it's not the most common way to do file uploads. PUT has to be done in application code (e.g. JavaScript), whereas with another method it's possible to do uploads with just HTML on the client side. What method do you think this describes?

Most file uploads are done via POST requests. For examples, see [this article at MDN](https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications).

### DELETE for, well, deleting things
The destructive counterpart to PUT is DELETE, for removing a resource from the server. After a DELETE has happened successfully, further GET requests for that resource will yield 404 Not Found ... unless, of course, a new resource is later created with the same name!

#### QUESTION 2 OF 3
What's something that we would almost always want the client to do before allowing it to delete resources in your application?

Most applications that involve creating and deleting resources on the server are going to require authentication, to make sure that the client is actually someone we want to trust with that power.

### PATCH for making changes
The PATCH method is a relatively new addition to HTTP. It expresses the idea of patching a resource, or changing it in some well-defined way. (If you've used Git, you can think of patching as what applying a Git commit does to the files in a repository.)

However, just as HTTP doesn't specify what format a resource has to be in, it also doesn't specify in what format a patch can be in: how it should represent the changes that are intended to be applied. That's up to the application to decide. An application could send diffs over HTTP PATCH requests, for instance. One standardized format for PATCH requests is the JSON Patch format, which expresses changes to a piece of JSON data. A different one is JSON Merge Patch.

### HEAD, OPTIONS, TRACE for debugging
There are a number of additional methods that HTTP supports for various sorts of debugging and examining servers.

- HEAD works just like GET, except the server doesn't return any content — just headers.
- OPTIONS can be used to find out what features the server supports.
- TRACE echoes back what the server received from the client — but is often disabled for security reasons.

#### QUESTION 3 OF 3
If HTTP methods are the "verbs" in the protocol, what are the "objects" (in the grammatical sense)?

An HTTP method asks the server to do something to a resource, which is named by a URI.

### Great responsibility
HTTP can't prevent a service from using methods to mean something different from what they're intended to mean, but this can have some surprising effects. For instance, you could create a service that used a GET request to delete content. However, web clients don't expect GET requests to have side-effects like that. In one famous case from 2006, an organization put up a web site where "edit" and "delete" actions happened through GET requests, and the result was that [the next search-engine web crawler to come along deleted the whole site](http://thedailywtf.com/articles/The_Spider_of_Doom).

### The standard tells all
For much more about HTTP methods, consult the [HTTP standards documents](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html).

- - -
Next up: [New developments in HTTP](ND024_Part4_Lesson08_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
