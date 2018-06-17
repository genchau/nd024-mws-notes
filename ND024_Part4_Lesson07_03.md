# Lesson 7.3 The echo server

The hello server doesn't do very much. But it does do all the basics of being an HTTP server. That's actually a pretty big deal. Deal. Let's take it a little step further though. In this exercise, you'll modify that server into one that makes use of the requests that it gets.

### The echo server
The hello server doesn't do anything with the query you send it. It just always sends back the same piece of text. Let's modify it into a server that sends back whatever request path you send it, like an echo. For instance, if you access the page http://localhost:8000/bears, you will see "bears" in your browser. We'll call this the echo server.

In order to echo back the request, the server needs to be able to look at the request information. That's something that http.server lets your code do. But to find out how, let's take a look in the documentation.

path is the right answer. Which means that in do_GET, you'll need to access `self.path` to get the request path.

### Exercise: Turn HelloHandler into EchoHandler
Change directory to course-ud303/Lesson-2/1_EchoServer. Here, you'll find a file called EchoServer.py. However, the code in that file is just a copy of the hello server code! For this exercise, modify this code so that it echoes back the request path that it receives. For instance, if you access http://localhost:8000/puppies, you should see the word "puppies" in your browser.

While you're at it, rename it from HelloHandler to EchoHandler, to better describe what we'll have it do now. When you're done, run EchoServer.py and test it out with some different request paths.

What didn't get echoed?
Once you have EchoServer.py running on your machine, try these three test URIs:

- http://localhost:8000/bears
- http://localhost:8000/spiders_from_mars#stardust
- http://localhost:8000/giant-squid?color=green

The word stardust only shows up in a URI fragment above — it appears after the # sign in the second URI. Fragments aren't sent to the server as part of an HTTP GET request; they only affect the browser. So this is the correct answer.

### How did you build the echo server?
The only difference in the code between EchoHandler and HelloHandler is what they write in the response body. The hello server always writes the same message, while the echo server takes its message from the request path. Here's how I did it — a one-line change at the end of do_GET:
```
self.wfile.write(self.path[1:].encode())
```
What I'm doing here is taking the path (for instance "/bears"), using a string slice to remove the first character (which is always a slash), and then encoding the resulting string into bytes, then writing that to the HTTP response body.

You could also do it in several lines of code:
```
message = self.path[1:]  # Extract 'bears' from '/bears', for instance
message_bytes = message.encode()  # Make bytes from the string
self.wfile.write(message_bytes)  # Send it over the network
```
Make sure to keep EchoServer.py around! We'll use it later in the course to look at queries.

The new server exits. Under normal conditions, only one program on your computer can listen on a particular port at the same time. If you want to have both servers running, you have to change the port number from 8000 to something else.

### Errata (Windows 10):
This is an erratum to the quiz above. Windows 10 has a different behavior from all other operating systems (including earlier Windows versions) when two processes try to listen on the same port. Instead of exiting with an error, the new server will stop and wait for the old server to exit. If you are using Windows 10, be on the lookout for this behavior in your network servers!

- - -
Next up: [Queries and quoting](ND024_Part4_Lesson07_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
