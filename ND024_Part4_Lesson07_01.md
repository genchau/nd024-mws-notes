# Lesson 7.1 Python's `http.server`

In the last lesson, you used the built in demo web server from Python's HTTP. server module. But the demo server is just that, a demo. Just surfing static files out of a directory is hardly the only thing you could do with HTTP. In this lesson, you'll build a few different web services using HTTP. server, and you'll learn more about HTTP as you're doing it. Later on in the lesson, you'll also use another module, requests, to write code that acts as an HTTP client fetching data off the web. The code you write in this lesson will run on your own computer so get out your favorite text editor, and maybe start up a new directory or a project for that code. And let's get into it.

### Python's http.server
In the last lesson, you used the built-in demo web server from the Python http.server module. But the demo server is just that — a demonstration of the module's abilities. Just serving static files out of a directory is hardly the only thing you can do with HTTP. In this lesson, you'll build a few different web services using http.server, and learn more about HTTP at the same time. You'll also use another module, requests, to write code that acts as an HTTP client.

These modules are written in object-oriented Python. You should already be familiar with creating class instances, defining subclasses, and defining methods on classes. If you need a refresher on the Python syntax for these object-oriented actions, you might want to browse the [Python tutorial on classes](https://docs.python.org/3/tutorial/classes.html) or take another look at the [sections on classes in our Programming Foundations with Python course](https://classroom.udacity.com/courses/ud036).

In the exercises in this lesson, you'll be writing code that runs on your own computer. You'll need the [starter code](https://github.com/udacity/course-ud303) that you downloaded at the end of the last lesson, which should be in a directory called course-ud303. And you'll need your favorite text editor to work on these exercises.

### Servers and handlers
Web servers using http.server are made of two parts: the HTTPServer class, and a request handler class. The first part, the HTTPServer class, is built in to the module and is the same for every web service. It knows how to listen on a port and accept HTTP requests from clients. Whenever it receives a request, it hands that request off to the second part — a request handler — which is different for every web service.

Here's what your Python code will need to do in order to run a web service:

- Import http.server, or at least the pieces of it that you need.
- Create a subclass of http.server.BaseHTTPRequestHandler. This is your handler class.
- Define a method on the handler class for each HTTP verb you want to handle. (The only HTTP verb you've seen yet in this course is GET, but that will be changing soon.)
    - The method for GET requests has to be called do_GET.
    - Inside the method, call built-in methods of the handler class to read the HTTP request and write the response.
- Create an instance of http.server.HTTPServer, giving it your handler class and server information — particularly, the port number.
- Call the HTTPServer instance's run_forever method.

Once you call the HTTPServer instance's run_forever method, the server does that — it runs forever, until stopped. Just as in the last lesson, if you have a Python server running and you want to stop it, type Ctrl-C into the terminal where it's running. (You may need to type it two or three times.)

### Exercise: The hello server
Let's take a quick tour of an example! In your terminal, go to the course-ud303 directory you downloaded earlier. Under the Lesson-2 subdirectory, you'll find a subdirectory called 0_HelloServer. Inside, there's a Python program called HelloServer.py. Open it up in your text editor and take a look around. Then run it in your terminal with python3 HelloServer.py. It won't print anything in the terminal … until you access it at http://localhost:8000/ in your browser.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/58866b65_screen-shot-2017-01-23-at-12.44.35/screen-shot-2017-01-23-at-12.44.35.png">

Accessing the hello server in Chrome.

### A tour of the hello server
Open up HelloServer.py in your text editor. Let's take a look at each part of this code, line by line.
```
from http.server import HTTPServer, BaseHTTPRequestHandler
```
The http.server module has a lot of parts in it. For now, this program only needs these two. I'm using the from syntax of import so that I don't have to type http.server over and over in my code.
```
class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
```
This is the handler class. It inherits from the BaseHTTPRequestHandler parent class, which is defined in http.server. I've defined one method, do_GET, which handles HTTP GET requests. When the web server receives a GET request, it will call this method to respond to it.

As you saw in the previous lesson, there are three things the server needs to send in an HTTP response: a status code, some headers, and the response body. The handler parent class has methods for doing each of these things. Inside do_GET, I just call them in order.
```
        # First, send a 200 OK response.
        self.send_response(200)
```
The first thing the server needs to do is send a 200 OK status code; and the send_response method does this. I don't have to tell it that 200 means OK; the parent class already knows that.
```
        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
```
The next thing the server needs to do is send HTTP headers. The parent class supplies the send_header and end_headers methods for doing this. For now, I'm just having the server send a single header line — the Content-type header telling the client that the response body will be in UTF-8 plain text.
```
        # Now, write the response body.
        self.wfile.write("Hello, HTTP!\n".encode())
```
The last part of the do_GET method writes the response body.

The parent class gives us a variable called self.wfile, which is used to send the response. The name wfile stands for writeable file. Python, like many other programming languages, makes an analogy between network connections and open files: they're things you can read and write data to. Some file objects are read-only; some are write-only; and some are read/write.

self.wfile represents the connection from the server to the client; and it is write-only; hence the name. Any binary data written to it with its write method gets sent to the client as part of the response. Here, I'm writing a friendly hello message.

What's going on with .encode() though? We'll get to that in a moment. Let's look at the rest of the code first.
```
if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
```
This code will run when we run this module as a Python program, rather than importing it. The HTTPServer constructor needs to know what address and port to listen on; it takes these as a tuple that I'm calling server_address. I also give it the HelloHandler class, which it will use to handle each incoming client request.

At the very end of the file, I call serve_forever on the HTTPServer, telling it to start handling HTTP requests. And that starts the web server running.

### End of the tour
That's all that's involved in writing a basic HTTP server in Python. But the hello server isn't very interesting. It doesn't even do as much as the demo server. No matter what query you send it, all it has to say is hello. (Try it: http://localhost:8000/goodbye)

In the rest of this lesson, we'll build servers that do much more than say hello.

- - -
Next up: [What about `.encode()`?](ND024_Part4_Lesson07_02.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
