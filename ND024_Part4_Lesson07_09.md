# Lesson 7.9 Making requests

### Making requests
Now let's turn from writing web servers to writing web clients. The requests library is a Python library for sending requests to web servers and interpreting the responses. It's not included in the Python standard library, though; you'll need to install it. In your terminal, run pip3 install requests to fetch and install the requests library.

Then take a look at the [quickstart documentation for requests](http://docs.python-requests.org/en/master/user/quickstart/) and try it out.

The requests function for performing GET requests is requests.get, and it takes the URI as an argument.

### Response objects
When you send a request, you get back a Response object. Try it in your Python interpreter:
```
>>> import requests
>>> a = requests.get('http://www.udacity.com')
>>> a
<Response [200]>
>>> type(a)
<class 'requests.models.Response'>
```

Both, but they're different. r.content is a bytes object representing the literal binary data that the server sent. r.text is the same data but interpreted as a str object, a Unicode string.

### Handling errors
Try fetching some different URIs with the requests module in your Python interpreter. More specifically, try some that don't work. Try some sites that don't exist, like http://bad.example.com/, but also try some pages that don't exist on sites that do, like http://google.com/ThisDoesNotExist.

What do you notice about the responses that you get back?
```
uri = "http://bad.example.com/"
r = requests.get(uri)
```

The first and last answers are correct, according to the way that HTTP is designed to work.

If the requests.get call can reach an HTTP server at all, it will give you a Response object. If the request failed, the Response object has a status_code data member — either 200, or 404, or some other code.

But if it wasn't able to get to an HTTP server, for instance because the site doesn't exist, then requests.get will raise an exception.

However: Some Internet service providers will try to redirect browsers to an advertising site if you try to access a site that doesn't exist. This is called DNS hijacking, and it's nonstandard behavior, but some do it anyway. If your ISP hijacks DNS, you won't get exceptions when you try to access nonexistent sites. Standards-compliant DNS services such as Google Public DNS don't hijack.

- - -
Next up: [Using a JSON API](ND024_Part4_Lesson07_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
