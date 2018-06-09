# Lesson 2.12 Performance Details 2

Every time the browser connects to a server to make a request, it has to go through the TCP handshake process. This 3-way handshake is very time consuming. To counteract the cost of these handshakes, HTTP/1.1 introduced the concept of **Keep-Alive**. If the client sets the connection Keep-Alive header, the server will not close the connection after successfully delivering the response, but allows the client to reuse the already established connection for additional requests. Keep in mind though, that you still can send requests before the response for the last request has been fully transferred. All in all, this forces web developers to keep the number of additional resources as low as possible, making the best possible use of their six connections. This is why JavaScript and CSS files are commonly concatenated into bundles and why images are put together into sprites. The bundles can be obtained in just one request. 

- - -
Next up: [Outro](ND024_Part4_Lesson02_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
