# Lesson 1.2 Client Server Demonstration

- Client (browser like Chrome or Firefox)
- Internet (middle man)
- Server (provides content).

Client sends a get request to server.
Server sends back what is requested. Call Response.
Client uses the response.
Client performs many requests according to the website.
When browser makes a request synchronously, without AJAX, it has to wait for responses before proceeding with the load.
AJAX is special because it allows these types of requests asynchronously, which means they can happen in the background without blocking the rest of the page load.
With AJAX, a request is sent to serer, the client holds on to a set of instructions of what to do when the response comes back, and then proceed to do other tasks. The instructions is called Callback.

GET Request: An internet request for data. Sent from a client to a server.
Response: A server's response to a request. Sent from a server to a client. A response to a GET request will usually include data that the client needs to load the page's content.

- - -
Next up: [Ajax Definition & Examples](ND024_Part3_Lesson01_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
