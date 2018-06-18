# Lesson 7.7 A server for POST

### A server for POST
One approach that I like to use when designing a new piece of code is to imagine that it already exists, and think through the ways that a user would use it. Coming up with these narratives is a useful tool to plan out what the code will need to do.

In the next few exercises, you'll be building a messageboard server. When a user goes to the main page in their browser, it'll display a form for writing messages, as well as a list of the previously written messages. Submitting the form will send a request to the server, which stores the submitted message and then re-displays the main page.

In order to test your messageboard server, you'll need to install the requests module, which is a Python module for making HTTP requests. We'll see much more about this module later in this lesson. For now, just run pip3 install requests in your terminal to install it.

Yes! We'll be using a GET request to display the messageboard's existing contents, and POST to update the contents by creating new messages. Creating new messages is not idempotent — we don't want duplicates.

Why don't we want to use GET for submitting the form? Imagine if a user did this. They write a message and press the submit button … and the message text shows up in their URL bar. If they press reload, it sends the message again. If they bookmark that URL and go back to it, it sends the message again. This doesn't seem like such a great experience. So we'll use POST for message submission, and GET to display the main page.

### POST handlers read the request body
Previously you've written handler classes that have just a single method, do_GET. But a handler class can have do_POST as well, to support GET and POST requests. This is exactly how the messageboard server will work. When a GET request comes in, the server will send the HTML form and current messages. When a POST request comes in with a new message, the server will store the message in a list, and then return all the messages it's seen so far.

The code for a do_POST method will need to do some pretty different things from a do_GET method. When we're handling a GET request, all the user data in the request is in the URI path. But in a POST request, it's in the request body. Inside do_POST, our code can read the request body by calling the self.rfile.read method. self.rfile is a file object, like the self.wfile we saw earlier — but rfile is for reading the request, rather than writing the response.

However, self.rfile.read needs to be told how many bytes to read … in other words, how long the request body is.

Exactly. If there's a request body at all, the browser will send the length of the request body in the Content-Length header.

### Headers are strings (or missing)
The handler class gives us access to the HTTP headers as the instance variable self.headers, which is an object that acts a lot like a Python dictionary. The keys of this dictionary are the header names, but they're case-insensitive: it doesn't matter if you look up 'content-length' or 'Content-Length'. The values in this dictionary are strings: if the request body is 140 bytes long, the value of the Content-length entry will be the string "140". We need to call self.rfile.read(140) to read 140 bytes; so once we read the header, we'll need to convert it to an integer.

But in an HTTP request, it's also possible that the body will be empty, in which case the browser might not send a Content-length header at all. This means we have to be a little careful when accessing the headers from the self.headers object. If we do self.headers['content-length'] and there's no such header, our code will crash with a KeyError. Instead we'll use the .get dictionary method to get the header value safely.

So here's a little bit of code that can go in the do_POST handler to find the length of the request body and read it:
```
length = int(self.headers.get('Content-length', 0))
data = self.rfile.read(length).decode()
```
Once you read the message body, you can use urllib.parse.parse_qs to extract the POST parameters from it.

With that, you can now build a do_POST method!

### Exercise: Messageboard, part one
The first step to building the messageboard server is to build a server that accepts a POST request and just echoes it back to the browser. The starter code for this exercise is in Lesson-2/3_MessageboardPartOne.

There are several steps involved in doing this, so here's a checklist —

### Solution, Part One
You can see my version of the solution to the Messageboard Part One exercise in the 3_MessageboardPartOne/solution subdirectory. As before, there are lots of variations on how you can do this exercise; if the tests in test.py pass, then you've got a good server!

MessageboardPartOne.py:
```
#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.
#
# Instructions:
#
# This server should accept a POST request and return the value of the
# "message" field in that request.
#
# You'll need to add three things to the do_POST method to make it work:
#
# 1. Find the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.
#
# When you're done, run this server and test it from your browser using the
# Messageboard.html form.  Then run the test.py script to check it.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-Length', 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # 3. Extract the "message" field from the request data.
        message = ''.join(parse_qs(data)["message"])
        print(data)
        print(message)

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

```

### Exercise: Messageboard, Part Two
So far, this server only handles POST requests. To submit the form to it, you have to load up the form in your browser as a separate HTML file. It would be much more useful if the server could serve the form itself.

This is pretty straightforward to do. You can add the form in a variable as a Python string (in triple quotes), and then write a do_GET method that sends the form.

You can choose to start from where you left off in the previous exercise; or if you like, you can start from the code in the 4_MessageboardPartTwo directory.

When you're done, you should have a server that you can access in your browser at http://localhost:8000/. Going there should display the form. Submitting the form should get the message echoed back. That's most of the way to a messageboard server ... let's keep going!

### Solution, Part Two
You can see my version of the solution to the Messageboard Part Two exercise in the 4_MessageboardPartTwo/solution subdirectory.

MessageboardPartTwo.py:
```
#!/usr/bin/env python3
#
# Step two in building the messageboard server:
# A server that handles both GET and POST requests.
#
# Instructions:
#
# 1. Add a string variable that contains the form from Messageboard.html.
# 2. Add a do_GET method that returns the form.
#
# You don't need to change the do_POST method in this exercise!
#
# To test your code, run this server and access it at http://localhost:8000/
# in your browser.  You should see the form.  Then put a message into the
# form and submit it.  You should then see the message echoed back to you.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
messageBoardHTML = '''
<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
'''

class MessageHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write(messageBoardHTML.encode())

    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # Extract the "message" field from the request data.
        message = parse_qs(data)["message"][0]

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

```

On the next page, you'll get into part three. But first, once you have your server up and running, try testing it out with some silly queries in this quiz:

This particular server doesn't look at the URI path at all. Any GET request will get the form. Any POST request will save a message.

- - -
Next up: [Post-Redirect-Get](ND024_Part4_Lesson07_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
