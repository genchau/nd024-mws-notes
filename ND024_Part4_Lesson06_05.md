# Lesson 6.5 HTTP GET requests

Now there are a lot of different types of HTTP requests. Every request contains an HTTP verb or method which tells the server what the client is asking it to do. The first kind of request we'll be looking at is called a GET request. This is what browsers use whenever they ask a server to send them a copy of a web page or an image or another resource. You've had your browser send GET requests to your demo server. So let's see if we can take a look at one of those requests.

### HTTP GET requests
Take a look back at the server logs on your terminal, where the demo server is running. When you request a page from the demo server, an entry appears in the logs with a message like this:
```
127.0.0.1 - - [03/Oct/2016 15:45:50] "GET /readme.png HTTP/1.1" 200 -
```
Take a look at the part right after the date and time. Here, it says "GET /readme.png HTTP/1.1". This is the text of the request line that the browser sent to the server. This log entry is the server telling you that it received a request that said, literally, GET /readme.png HTTP/1.1.

This request has three parts.

The word GET is the method or HTTP verb being used; this says what kind of request is being made. GET is the verb that clients use when they want a server to send a resource, such as a web page or image. Later, we'll see other verbs that are used when a client wants to do other things, such as submit a form or make changes to a resource.

/readme.png is the path of the resource being requested. Notice that the client does not send the whole URI of the resource here. It doesn't say https://localhost:8000/readme.png. It just sends the path.

Finally, HTTP/1.1 is the protocol of the request. Over the years, there have been several changes to the way HTTP works. Clients have to tell servers which dialect of HTTP they're speaking. HTTP/1.1 is the most common version today.

### Exercise: Send a request by hand
You can use ncat to connect to the demo server and send it an HTTP request by hand. (Make sure the demo server is still running!)

Try it out:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fc0ab7_image-7/image-7.png">

I used the command ncat 127.0.0.1 8000 to connect to port 8000.
Then I typed out an HTTP request on the next two lines.

Use ncat 127.0.0.1 8000 to connect your terminal to the demo server.

Then type these two lines:
```
GET / HTTP/1.1
Host: localhost
```
After the second line, press Enter twice. As soon as you do, the response from the server will be displayed on your terminal. Depending on the size of your terminal, and the number of files the web server sees, you will probably need to scroll up to see the beginning of the response!

So here I am with a couple of terminals again. On this side, I'll run the demo server, python3 -m http.server, and the port number, 8000. And it tells me that it's serving HTTP on 0.0.0.0 port 8000, which is to say, on all IPv4 addresses port 8000. And over here, I'll run ncat 127.0.0.1, which is localhost, to port 8000 to connect to the server. Now I'll send an HTTP request over to the server-- GET / HTTP/1.1, Host: localhost. Then I'll press Enter twice. And whoa, that's a lot of stuff the server sent back. What is all this? Ok, I'm going to scroll up in my terminal window and take a look. So here's where I sent the HTTP request, and so everything after that is the response. On this line, it says, HTTP/1.0 200 OK. And then here are the HTTP headers, including the date. And down here, we can see the beginnings of a piece of HTML, which is the body of the server's response.

On the next page, we'll look at the parts of the HTTP response in detail.

- - -
Next up: [HTTP responses](ND024_Part4_Lesson06_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
