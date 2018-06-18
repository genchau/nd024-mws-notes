# Lesson 8.2 Handling more requests

### Handling more requests
Try creating a link in it where the target URI is the bookmark server's own URI. What happens when you try to do that?

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588d2a54_screen-shot-2017-01-28-at-15.33.04/screen-shot-2017-01-28-at-15.33.04.png">

Looking at the bookmark server I've deployed on Heroku.
I'm about to submit the bookmark server's own URI in the form.

When I do this, the app gives me an error, saying it can't fetch that web page. That's weird! The server is right there; it should be able to reach itself! What do you think is going on here?

That's right! The basic, built-in http.server.HTTPServer class can only handle a single request at once. The bookmark server tries to fetch every URI that we give it, while it's in the middle of handling the form submission.

It's like an old-school telephone that can only have one call at once. Because it can only handle one request at a time, it can't "pick up" the second request until it's done with the first … but in order to answer the first request, it needs the response from the second.

### Concurrency
Being able to handle two ongoing tasks at the same time is called concurrency, and the basic http.server.HTTPServer doesn't have it. It's pretty straightforward to plug concurrency support into an HTTPServer, though. The Python standard library supports doing this by adding a mixin to the HTTPServer class. A mixin is a sort of helper class, one that adds extra behavior the original class did not have. To do this, you'll need to add this code to your bookmark server:
```
import threading
from socketserver import ThreadingMixIn

class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."
```

Then look at the bottom of your bookmark server code, where it creates an HTTPServer. Have it create a ThreadHTTPServer instead:
```
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
```

Commit this change to your Git repository, and push it to Heroku. Now when you test it out, you should be able to add an entry that points to the service itself.

```
import http.server
import requests
import os
import threading
from socketserver import ThreadingMixIn
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
        r = requests.get(uri, timeout=timeout)
    except requests.RequestException:
        # print("exception")
        return False
    else:
        if r.status_code == 200:
            return True
        else:
            # print("DNS intercepting")
            return False

class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."


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
            self.wfile.write("Please fill out both Long URI and Short Name form fields".encode())
            return

        longuri = params["longuri"][0]
        shortname = params["shortname"][0]
        # print(longuri)
        # print(shortname)

        if CheckURI(longuri):
            # This URI is good!  Remember it under the specified name.
            # print("CheckURI passed")
            memory[shortname] = longuri

            # 4. Serve a redirect to the root page (the form).
            #    Delete the following line.
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            # Didn't successfully fetch the long URI.
            # print("CheckURI failed")
            # 5. Send a 404 error with a useful message.
            #    Delete the following line.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Couldn't fetch URI '{}'. Sorry!".format(longuri).encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000)) # Use PORT if it's there.
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, Shortener)
    httpd.serve_forever()
```

- - -
Next up: [What's an Apache or Nginx?](ND024_Part4_Lesson08_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
