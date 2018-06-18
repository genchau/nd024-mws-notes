# Lesson 7.11 The bookmark server

<img src="images/ND024_Part4_Lesson07_11_Bookmark_Server.JPG">

### Exercise: The bookmark server
You're almost to the end of this lesson! One more server to write …

You've probably seen URL-shortening services such as TinyURL or Google's goo.gl. They let you create short URI paths like http://goo.gl/xLcHvY that redirect to a longer URI on another site. It's easier to put a short URI into an email, text message, or tweet. In this exercise, you'll be writing a service similar to this.

Like the messageboard server, this bookmark server will keep all of its data in memory. This means that it'll be reset if you restart it.

Your server needs to do three things, depending on what kind of request it receives:

- On a GET request to the / path, it displays an HTML form with two fields. One field is where you put the long URI you want to shorten. The other is where you put the short name you want to use for it. Submitting this form sends a POST to the server.
- On a POST request, the server looks for the two form fields in the request body. If it has those, it first checks the URI with requests.get to make sure that it actually exists (returns a 200).
    - If the URI exists, the server stores a dictionary entry mapping the short name to the long URI, and returns an HTML page with a link to the short version.
    - If the URI doesn't actually exist, the server returns a 404 error page saying so.
    - If either of the two form fields is missing, the server returns a 400 error page saying so.
- On a GET request to an existing short URI, it looks up the corresponding long URI and serves a redirect to it.

The starter code for this exercise is in the 7_BookmarkServer directory. I've given you a skeleton of the server; your job is to fill out the details!

BookmarkServer.py:
```
#!/usr/bin/env python3
#
# A *bookmark server* or URI shortener that maintains a mapping (dictionary)
# between short names and long URIs, checking that each new URI added to the
# mapping actually works (i.e. returns a 200 OK).
#
# This server is intended to serve three kinds of requests:
#
#   * A GET request to the / (root) path.  The server returns a form allowing
#     the user to submit a new name/URI pairing.  The form also includes a
#     listing of all the known pairings.
#   * A POST request containing "longuri" and "shortname" fields.  The server
#     checks that the URI is valid (by requesting it), and if so, stores the
#     mapping from shortname to longuri in its dictionary.  The server then
#     redirects back to the root path.
#   * A GET request whose path contains a short name.  The server looks up
#     that short name in its dictionary and redirects to the corresponding
#     long URI.
#
# Your job in this exercise is to finish the server code.
#
# Here are the steps you need to complete:
#
# 1. Write the CheckURI function, which takes a URI and returns True if a
#    request to that URI returns a 200 OK, and False otherwise.
#
# 2. Write the code inside do_GET that sends a 303 redirect to a known name.
#
# 3. Write the code inside do_POST that sends a 400 error if the form fields
#    are missing.
#
# 4. Write the code inside do_POST that sends a 303 redirect to the form
#    after saving a newly submitted URI.
#
# 5. Write the code inside do_POST that sends a 404 error if a URI is not
#    successfully checked (i.e. if CheckURI returns false).
#
# In each step, you'll need to delete a line of code that raises the
# NotImplementedError exception.  These are there as placeholders in the
# starter code.
#
# After writing each step, restart the server and run test.py to test it.

import http.server
import requests
from urllib.parse import unquote, parse_qs

memory = {}

form = '''<!DOCTYPE html>
<title>Bookmark Server</title>
<form method="POST">
    <label>Long URI:
        <input name="longuri">
    </label>
    <br>
    <label>Short name:
        <input name="shortname">
    </label>
    <br>
    <button type="submit">Save it!</button>
</form>
<p>URIs I know about:
<pre>
{}
</pre>
'''


def CheckURI(uri, timeout=5):
    '''Check whether this URI is reachable, i.e. does it return a 200 OK?

    This function returns True if a GET request to uri returns a 200 OK, and
    False if that GET request returns any other response, or doesn't return
    (i.e. times out).
    '''
    # 1. Write this function.  Delete the following line.
    try:
        r = requests.get(uri)
    except:
        # print("exception")
        return False
    else:
        if r.status_code == 200:
            return True
        else:
            # print("DNS intercepting")
            return False


class Shortener(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # A GET request will either be for / (the root path) or for /some-name.
        # Strip off the / and we have either empty string or a name.
        name = unquote(self.path[1:])

        if name:
            if name in memory:
                # 2. Send a 303 redirect to the long URI in memory[name].
                #    Delete the following line.
                self.send_response(303)
                self.send_header('Location', memory[name])
                self.end_headers()
            else:
                # We don't know that name! Send a 404 error.
                self.send_response(404)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write("I don't know '{}'.".format(name).encode())
        else:
            # Root path. Send the form.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # List the known associations in the form.
            known = "\n".join("{} : {}".format(key, memory[key])
                              for key in sorted(memory.keys()))
            self.wfile.write(form.format(known).encode())

    def do_POST(self):
        # Decode the form data.
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)

        # Check that the user submitted the form fields.
        if "longuri" not in params or "shortname" not in params:
            # 3. Serve a 400 error with a useful message.
            #    Delete the following line.
            self.send_response(400)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Please fill out both Long URI and Short Name fields".encode())

        longuri = params["longuri"][0]
        shortname = params["shortname"][0]
        print(longuri)
        print(shortname)

        if CheckURI(longuri):
            # This URI is good!  Remember it under the specified name.
            print("CheckURI passed")
            memory[shortname] = longuri

            # 4. Serve a redirect to the root page (the form).
            #    Delete the following line.
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # Didn't successfully fetch the long URI.
            print("CheckURI failed")
            # 5. Send a 404 error with a useful message.
            #    Delete the following line.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Page not found".encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, Shortener)
    httpd.serve_forever()

```

- - -
Next up: [You did it!](ND024_Part4_Lesson07_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
