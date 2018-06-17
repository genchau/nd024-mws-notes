# Lesson 6.6 HTTP responses

Now that we have a handle on HTTP requests, let's take a closer look at the HTTP response that the server sends back. Now the response to a GET request is going to be whatever it is that the server has to send back to fulfill the client's request. That could be a piece of HTML or an image or some other data. Let's see how that works.

### HTTP responses
Take another look at what you got back from the web server in the previous exercise.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fc0d57_image-8/image-8.png">

I connected to the demo server with ncat 127.0.0.1 8000, then wrote out an HTTP request.
The server sent back an HTTP response.
Everything after the line Host: localhost is part of the server's response.

After you typed Host: localhost and pressed Enter twice, the server sent back a lot of text. This is an HTTP response. One of these exchanges — a request and response — is happening every time your browser asks a server for a page, an image, or anything else.

Here's another one to try. Use ncat to connect to google.com port 80, and send a request for the path / on the host google.com:
```
GET / HTTP/1.1
Host: google.com
```
Make sure to send Host: google.com exactly ... don't slip a www in there. These are actually different hostnames, and we want to take a look at the difference between them. And press Enter twice!

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fc0f25_image-9/image-9.png">

I connected to google.com port 80 and sent an HTTP request.
Google's server sent back an HTTP response.

The HTTP response is made up of three parts: the status line, some headers, and a response body.

The status line is the first line of text that the server sends back. The headers are the other lines up until the first blank line. The response body is the rest — in this case, it's a piece of HTML.

### Status line
In the response you got from your demo server, the status line said HTTP/1.0 200 OK. In the one from Google, it says HTTP/1.1 301 Moved Permanently. The status line tells the client whether the server understood the request, whether the server has the resource the client asked for, and how to proceed next. It also tells the client which dialect of HTTP the server is speaking.

The numbers 200 and 301 here are HTTP status codes. There are dozens of different status codes. The first digit of the status code indicates the general success of the request. As a shorthand, web developers describe all of the codes starting with 2 as "2xx" codes, for instance — the x's mean "any digit".

- 1xx — Informational. The request is in progress or there's another step to take.
- 2xx — Success! The request succeeded. The server is sending the data the client asked for.
- 3xx — Redirection. The server is telling the client a different URI it should redirect to. The headers will usually contain a Location header with the updated URI. Different codes tell the client whether a redirect is permanent or temporary.
- 4xx — Client error. The server didn't understand the client's request, or can't or won't fill it. Different codes tell the client whether it was a bad URI, a permissions problem, or another sort of error.
- 5xx — Server error. Something went wrong on the server side.

You can find out much more about HTTP status codes in this [Wikipedia article](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) or in the [specification for HTTP.](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

The server response here is an example of good user interface on the Web. Google wants browsers to use www.google.com instead of google.com. But instead of showing the user an error message, they send a redirect. Browsers will automatically follow the redirect and end up on the right site.

### Headers
An HTTP response can include many headers. Each header is a line that starts with a keyword, such as Location or Content-type, followed by a colon and a value. Headers are a sort of metadata for the response. They aren't displayed by browsers or other clients; instead, they tell the client various information about the response.

Many, many features of the Web are implemented using headers. For instance, cookies are a Web feature that lets servers store data on the browser, for instance to keep a user logged in. To set a cookie, the server sends the Set-Cookie header. The browser will then send the cookie data back in a Cookie header on subsequent requests. You'll see more about cookies later in this course.

For the next quiz, take a look at the Content-type header sent by the Google server and the demo server. Both servers send the exact same value:
```
Content-type: text/html; charset=utf-8
```
What do you think this means?

A Content-type header indicates the kind of data that the server is sending. It includes a general category of content as well as the specific format. For instance, a PNG image file will come with the Content-type image/png. If the content is text (including HTML), the server will also tell what encoding it's written in. UTF-8 is a very common choice here, and it's the default for Python text anyway.

Very often, the headers will contain more metadata about the response body. For instance, both the demo server and Google also send a Content-Length header, which tells the client how long (in bytes) the response body will be. If the server sends this, then the client can reuse the connection to send another request after it's read the first response. Browsers use this so they can fetch multiple pieces of data (such as images on a web page) without having to reconnect to the server.

### Response body
The headers end with a blank line. Everything after that blank line is part of the response body. If the request was successful (a 200 OK status, for instance), this is a copy of whatever resource the client asked for — such as a web page, image, or other piece of data.

But in the case of an error, the response body is where the error message goes! If you request a page that doesn't exist, and you get a 404 Not Found error, the actual error message shows up in the response body.

### Exercise: Be a web server!
Use ncat -l 9999 to listen on port 9999. Connect to it with your web browser at http://localhost:9999/. What do you see in your terminal?

Keep that terminal open!

Next, send an HTTP response to your browser by typing it into the terminal, right under where you see the headers the browser sent to you:
```
HTTP/1.1 307 Temporary Redirect
Location: https://www.eff.org/
```
At the end, press Enter twice to send a blank line to mark the end of headers.

OK, so here's my terminal and here's my web browser. In the terminal, I'll set an ncat server listening on port 9999. Now in the browser, I'll go to http://localhost:9999 to send a request to the server. And here on the server, we can see the request the browser sent. It starts with get / http/1.1, host: localhost. And then a bunch of other headers. Now, in the terminal, I'll have the server send an HTTP response. HTTP/1.1 307 Temporary Redirect. With a location header pointint to HTTPS://www.eff.org. And when I press Enter twice to send a blank line and signal end of headers, the browser refreshes to the URI that I just gave it, which goes to the Electronic Frontier Foundation's main page.

Do it again! Run ncat -l 9999 to play a server, and get your browser to access it. But this time, instead of sending a 307 redirect, send a 200 OK with a piece of text in it:
```
HTTP/1.1 200 OK
Content-type: text/plain
Content-length: 50

Hello, browser! I am a real HTTP server, honestly!
```
(Remember the blank line between headers and body!)

- - -
Next up: [Congratulations!](ND024_Part4_Lesson06_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
