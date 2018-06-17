# Lesson 6.2 Your first web server

An HTTP transaction always involves a client and a server. You're using an HTTP client right now, your web browser. Your browser sends HTTP requests to web servers, and servers send responses back to your browser. Like when you went to this page, your browser sent a request to Udacity's web server, which sent a response back. Loading a page may take many requests, sometimes to different servers. Like this video is hosted on YouTube servers. The code in this website tells your browser to request this video from Youtube. And just up ahead, you're going to run a web server of your own on your own computer. But first, let's  do a quiz about what kinds of things a web server might be involved in.

### Your first web server
An HTTP transaction always involves a client and a server. You're using an HTTP client right now — your web browser. Your browser sends HTTP requests to web servers, and servers send responses back to your browser. Displaying a simple web page can involve dozens of requests — for the HTML page itself, for images or other media, and for additional data that the page needs.

HTTP was originally created to serve hypertext documents, but today is used for much more. As a user of the web, you're using HTTP all the time.

Did the pizza one surprise you? A lot of smartphone apps use HTTP under the hood to send requests and receive data. Web browsers are just the most common — and complicated — user interface for web technology. But browsers are not the only web client around. HTTP is powerful and widely supported in software, so it's a common choice for programs that need to talk to each other across the network, even if they don't look anything like a web browser.

### Exercise: Running your first web server
So what about the other end, the web server? Well, it turns out that a web server can actually be a lot simpler than a browser. Browsers have all this user interface and animation and graphics stuff going on. A server just needs to do one thing: handle incoming requests.

The Python http.server module can run a built-in web server on your computer. It's not a web app you'd publish to the world; it's a demonstration of Python's HTTP abilities. We'll be referring to this as the demo server in this lesson.

So, let's get started with the demo web server.

Open up a terminal; cd to a directory that has some files in it — maybe a directory containing some text files, HTML files, or images — then run python3 -m http.server 8000 in your terminal.

Here, I've run it in a directory containing some silly comics I drew:
<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fbf613_image-2/image-2.png">

Starting the demo server in the terminal. I've changed directories to my Documents directory, then run python3 -m http.server 8000. The server tells me that it's serving HTTP on port 8000.

When you start up the demo server, it will print a message telling you that it's serving HTTP. Leave it running, and leave the terminal open. Now try accessing http://localhost:8000/ from your browser. You should see something like this, although the file names you see will be different from mine:
<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/57fbf67e_image-3/image-3.png">

Accessing http://localhost:8000/ in my web browser, I see the demo server showing the same files that are in my Documents directory.

And that's the Python demo web server, running on your own computer. It serves up files on your local disk so you can look at them in your browser.

This may not seem like much of a big deal — after all, if you just wanted to access files on your local computer in your browser, you could use file:// URIs. But the demo server is actually a web server. If you have another computer on the same local network, you could use it to access files served up by this server.

When you put localhost:8000 in your browser, your browser sends an HTTP request to the Python program you're running. That program responds with a piece of data, which your browser presents to you. In this case, it's showing you a directory listing as a piece of HTML. Use your browser's developer tools to look at the HTML that it sends.

Note: If you have a file called index.html in that directory, you'll see the contents of that file in your browser instead of the directory listing. Move that file somewhere else and reload the page, and you will see the directory listing like the one above.

404 is the HTTP status code for "Not Found". On Highway 101, not far from the Udacity office in Mountain View, there's a sign that tells the distance to Los Angeles. As it happens, it's 404 miles from Mountain View to Los Angeles, so the sign says Los Angeles 404. And so, every web programmer in Silicon Valley has probably heard the "Los Angeles Not Found" joke at least once.

### What's a server anyway?
A server is just a program that accepts connections from other programs on the network.

When you start a server program, it waits for clients to connect to it — like the demo server waiting for your web browser to ask it for a page. Then when a connection comes in, the server runs a piece of code — like calling a function — to handle each incoming connection. A connection in this sense is like a phone call: it's a channel through which the client and server can talk to each other. Web clients send requests over these connections, and servers send responses back.

Take a look in the terminal where you ran the demo server. You'll see a server log with an entry for each request your browser sent:
```
Serving HTTP on 0.0.0.0 port 8000 ...
127.0.0.1 - - [03/Oct/2016 13:47:35] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:47:36] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:48:06] "GET /falafelosofhy.png HTTP/1.1" 200 -
127.0.0.1 - - [03/Oct/2016 13:49:23] code 404, message File not found
127.0.0.1 - - [03/Oct/2016 13:49:23] "GET /NotExistyFile HTTP/1.1" 404 -
```
Hey wow, what is all this stuff? There are some dates and times in there, but what's GET / HTTP/1.1, or for that matter 127.0.0.1? And what's that 200 doing over there?

How do these things relate to the web address you put into your browser? Let's take a look at that next.

- - -
Next up: [Parts of a URI](ND024_Part4_Lesson06_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
