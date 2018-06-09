# Lesson 1.4 Fetching a single request

The tubes and forms are basically the underlying concept of HTTP, request and responses. Well, we're not really going to be shoving paper through tubes, but rather, data through network cables. 

This is what an actual request looks like. This is the exact text the browser sends to the server to request an image called kitty.jpg. HTTP Request:
```
GET /pictures/kitty.jpg HTTP/1.1
Host: www.google.com
User-Agent: Mozilla/5.0
Connection: keep-alive
Accept: text/html
If-None-Match: b2arb0a1r6a
```

The protocol can get, add, delete and update documents.

To distinguish between these capabilities, the first line starts with an HTTP method or verb. This request uses the GET method, which means we want the server to send data to us. Another example of a method is POST, which instructs the server to save the data we are sending. There are more methods than these, but we'll worry about them later when we talk about REST APIs. Let's get back to the original request. After the method comes the path and name of the document we would like to get. Here, we want the server to send us a file called kitty.jpg located in the pictures directory. The last thing in the first line is the version of the HTTP protocol we are using. As of today, HTTP1.1 is the most common and widely supported version. However, HTTP2 is slowly catching up and taking over as the de facto standard. 

- - -
Next up: [Fetching a single request 2](ND024_Part4_Lesson01_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
