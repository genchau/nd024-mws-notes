# Lesson 8.4 Cookies

### Cookies
Cookies are a way that a server can ask a browser to retain a piece of information, and send it back to the server when the browser makes subsequent requests. Every cookie has a name and a value, much like a variable in your code; it also has rules that specify when the cookie should be sent back.

What are cookies for? A few different things. If the server sends each client a unique cookie value, it can use these to tell clients apart. This can be used to implement higher-level concepts on top of HTTP requests and responses — things like sessions and login. Cookies are used by analytics and advertising systems to track user activity from site to site. Cookies are also sometimes used to store user preferences for a site.

### How cookies happen
The first time the client makes a request to the server, the server sends back the response with a Set-Cookie header. This header contains three things: a cookie name, a value, and some attributes. Every subsequent time the browser makes a request to the server, it will send that cookie back to the server. The server can update cookies, or ask the browser to expire them.

### Seeing cookies in your browser
Browsers don't make it easy to find cookies that have been set, because removing or altering cookies can affect the expected behavior of web services you use. However, it is possible to inspect cookies from sites you use in every major browser. Do some research on your own to find out how to view the cookies that your browser is storing.

Here's a cookie that I found in my Chrome browser, from a web site I visited:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58507324_unnamed-1/unnamed-1.png">

A cookie displayed in my Chrome browser.

What are all these pieces of data in my cookie? There are eight different fields there!

By the way, if you try to research "cookie fields" with a web search, you may get a lot of results from the Mrs. Fields cookie company. Try "HTTP cookie fields" for more relevant results.

The first two, the cookie's name and content, are also called its key and value. They're analogous to a dictionary key and value in Python — or a variable's name and value for that matter. They will both be sent back to the server. There are some syntactic rules for which characters are allowed in a cookie name; for instance, they can't have spaces in them. The value of the cookie is where the "real data" of the cookie goes — for instance, a unique token representing a logged-in user's session.

The next two fields, Domain and Path, describe the scope of the cookie — that is to say, which queries will include it. By default, the domain of a cookie is the hostname from the URI of the response that set the cookie. But a server can also set a cookie on a broader domain, within limits. For instance, a response from www.udacity.com can set a cookie for udacity.com, but not for com.

The fields that Chrome describes as "Send for" and "Accessible to script" are internally called Secure and HttpOnly, and they are boolean flags (true or false values). The internal names are a little bit misleading. If the Secure flag is set, then the cookie will only be sent over HTTPS (encrypted) connections, not plain HTTP. If the HttpOnly flag is set, then the cookie will not be accessible to JavaScript code running on the page.

Finally, the last two fields deal with the lifetime of the cookie — how long it should last. The creation time is just the time of the response that set the cookie. The expiration time is when the server wants the browser to stop saving the cookie. There are two different ways a server can set this: it can set an Expires field with a specific date and time, or a Max-Age field with a number of seconds. If no expiration field is set, then a cookie is expired when the browser closes.

### Using cookies in Python
To set a cookie from a Python HTTP server, all you need to do is set the Set-Cookie header on an HTTP response. Similarly, to read a cookie in an incoming request, you read the Cookie header. However, the format of these headers is a little bit tricky; I don't recommend formatting them by hand. Python's http.cookies module provides handy utilities for doing so.

To create a cookie on a Python server, use the SimpleCookie class. This class is based on a dictionary, but has some special behavior once you create a key within it:
```
from http.cookies import SimpleCookie, CookieError

out_cookie = SimpleCookie()
out_cookie["bearname"] = "Smokey Bear"
out_cookie["bearname"]["max-age"] = 600
out_cookie["bearname"]["httponly"] = True
```

Then you can send the cookie as a header from your request handler:
```
self.send_header("Set-Cookie", out_cookie["bearname"].OutputString())
```
To read incoming cookies, create a SimpleCookie from the Cookie header:
```
in_cookie = SimpleCookie(self.headers["Cookie"])
in_data = in_cookie["bearname"].value
```
Be aware that a request might not have a cookie on it, in which case accessing the Cookie header will raise a KeyError exception; or the cookie might not be valid, in which case the SimpleCookie constructor will raise http.cookies.CookieError.

Important safety tip: Even though browsers make it difficult for users to modify cookies, it's possible for a user to modify a cookie value. Higher-level web toolkits, such as Flask (in Python) or Rails (in Ruby) will cryptographically sign your cookies so that they won't be accepted if they are modified. Quite often, high-security web applications use a cookie just to store a session ID, which is a key to a server-side database containing user information.

Another important safety tip: If you're displaying the cookie data as HTML, you need to be careful to escape any HTML special characters that might be in it. An easy way to do this in Python is to use the html.escape function, from the built-in html module!

For a lot more information on cookie handling in Python, see the [documentation for the http.cookies module](https://docs.python.org/3/library/http.cookies.html).

### Exercise: A server that remembers you
In this exercise, you'll build a server that asks for your name, and then stores your name in a cookie on your browser. You'll be able to see that cookie in your browser's cookie data. Then when you visit the server again, it'll already know your name.

The starter code for this exercise is in Lesson-3/2_CookieServer.

```
#!/usr/bin/env python3
#
# An HTTP server that remembers your name (in a cookie)
#
# In this exercise, you'll create and read a cookie to remember the name
# that the user submits in a form.  There are two things for you to do here:
#
# 1. Set the relevant fields of the cookie:  its value, domain, and max-age.
#
# 2. Read the cookie value into a variable.

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
from urllib.parse import parse_qs
from html import escape as html_escape
from http.cookies import SimpleCookie, CookieError

form = '''<!DOCTYPE html>
<title>I Remember You</title>
<p>
{}
<p>
<form method="POST">
<label>What's your name again?
<input type="text" name="yourname">
</label>
<br>
<button type="submit">Tell me!</button>
</form>
'''


class NameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the post data?
        length = int(self.headers.get('Content-length', 0))

        # Read and parse the post data
        data = self.rfile.read(length).decode()
        yourname = parse_qs(data)["yourname"][0]

        # Create cookie.
        c = cookies.SimpleCookie()

        # 1. Set the fields of the cookie.
        #    Give the cookie a value from the 'yourname' variable,
        #    a domain (localhost), and a max-age.
        c["yourname"] = yourname
        c["yourname"]["max-age"] = 600
        c["yourname"]["domain"] = 'localhost'


        # Send a 303 back to the root page, with a cookie!
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.send_header('Set-Cookie', c['yourname'].OutputString())
        self.end_headers()

    def do_GET(self):
        # Default message if we don't know a name.
        message = "I don't know you yet!"

        # Look for a cookie in the request.
        if 'cookie' in self.headers:
            try:
                # 2. Extract and decode the cookie.
                #    Get the cookie from the headers and extract its value
                #    into a variable called 'name'.
                in_cookie = SimpleCookie(self.headers["Cookie"])
                name = in_cookie['yourname'].value

                # Craft a message, escaping any HTML special chars in name.
                message = "Hey there, " + html_escape(name)
            except (KeyError, cookies.CookieError) as e:
                message = "I'm not sure who you are!"
                print(e)

        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the message in it.
        mesg = form.format(message)
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NameHandler)
    httpd.serve_forever()
```

### How it looks on my browser

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588d3120_screen-shot-2017-01-28-at-16.01.55/screen-shot-2017-01-28-at-16.01.55.png">

A cookie from localhost ...

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588d317d_screen-shot-2017-01-28-at-16.03.33/screen-shot-2017-01-28-at-16.03.33.png">

... and a server that recognizes it.

### DNS domains and cookie security
Back in Lesson 1, you used the host or nslookup command to look up the IP addresses of a few different web services, such as Wikipedia and your own localhost. But domain names play a few other roles in HTTP besides just being easier to remember than IP addresses. A DNS domain links a particular hostname to a computer's IP address. But it also indicates that the owner of that domain intends for that computer to be treated as part of that domain.

Imagine what a bad guy could do if they could convince your browser that their server evilbox was part of (say) Facebook, and get you to request a Facebook URL from evilbox instead of from Facebook's real servers. Your browser would send your facebook.com cookies to evilbox along with that request. But these cookies are what prove your identity to Facebook … so then the bad guy could use those cookies to access your Facebook account and send spam messages to all your friends.

In the immortal words of Dr. Egon Spengler: It would be bad.

This is just one reason that DNS is essential to web security. If a bad guy can take control of your site's DNS domain, they can send all your web traffic to their evil server … and if the bad guy can fool users' browsers into sending that traffic their way, they can steal the users' cookies and reuse them to break into those users' accounts on your site.

- - -
Next up: [HTTPS for security](ND024_Part4_Lesson08_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
