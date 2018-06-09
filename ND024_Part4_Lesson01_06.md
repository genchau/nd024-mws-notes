# Lesson 1.6 Getting Multiple Requests

We just saw how to fetch a single document using an HTTP request. These documents can be any kind of data really but on the web, everything usually starts with an index document. The index document is what the server will send back to you if no explicit file is defined in the request. By typing a URL in the address bar of the browser, the user is instructing the browser to oepn a new connection to the server identified by the host name in the URL, and getting the document specified in the path of the URL. In this case, the server will respond with the index.html and the browser can start parsing it. This is a really interesting step and the browser does a number of things to handle and receive data. Check out the link in the instructor notes for an explanation on how this works. After the browser has parsed the response, things start to get a little wild. As the browser is reading the index.html, it will probably find references to other documents needed to properly display the website. These can be images, stylesheets, JavaScript files, videos, you name it. For each of these resources, another request is sent and once the response is received by the browser, this entire process of parsing and potentially sending new requests is repeated. That also means that each of these resources can in turn pull in additional resources. Each landing page will have its own set of dependencies like images, CSS, and JavaScript files. That means that visiting a single URL can send off many more requests than we might be aware of.

1. Starts with index.html.
2. Browser starts parsing the information.
3. Browser sends off multiple more requests depending what the webpage needs.
4. It can be CSS
5. It can be JavaScript
6. It can be images
7. It can be videos

[Converting HTML to the DOM](https://classroom.udacity.com/courses/ud884/lessons/1464158642/concepts/15290985490923)

- - -
Next up: [Exercise Setup](ND024_Part4_Lesson01_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
