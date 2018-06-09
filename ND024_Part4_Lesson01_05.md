# Lesson 1.5 Fetching a single request 2

After the first line of the request. What follows is the header. Headers are additional data about the request itself. A lot of these headers are standardized and contain information like; what type of browser is making the request, what kind of format the browser supports and what version of the document is already available in the browser's local cache. All of these headers are optional except for the host header. The smallest request that can be made would only consist of the first line and the host header. 

HTTP Response:
```
HTTP/1.1 200 OK
Content-Length: 16824
Server: Apache
Content-Type: text/html
Date: Wed, 06 Apr 2016
Etag: fd87e6789

<binary data>
```

At a first glance, a response looks very similar to a request. The biggest difference is probably the first line. Here we can find out the status code of a response that indicates if our request was fulfilled successfully, if the document was not found or if the server wants to redirect us somewhere else. Just like with a request, the next section is the header section. It not only contains data about the document, but also about the server and the connection. Again most of these headers are optional. The only obligatory header is content length to tell the client how many byts of data it should expect. After the headers and an additional empty line, the actual document is sent. This can be a JPEG image, an HTML document or whatever we want to transfer to the user.

- - -
Next up: [Getting Multiple Requests](ND024_Part4_Lesson01_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
