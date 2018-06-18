# Lesson 7.8 Post-Redirect-Get

### Post-Redirect-Get
There's a very common design pattern for interactive HTTP applications and APIs, called the PRG or Post-Redirect-Get pattern. A client POSTs to a server to create or update a resource; on success, the server replies not with a 200 OK but with a 303 redirect. The redirect causes the client to GET the created or updated resource.

This is just one of many, many ways to architect a web application, but it's one that makes good use of HTTP methods to accomplish specific goals. For instance, wiki sites such as Wikipedia often use Post-Redirect-Get when you edit a page.

For the messageboard server, Post-Redirect-Get means:

1. You go to http://localhost:8000/ in your browser. Your browser sends a GET request to the server, which replies with a 200 OK and a piece of HTML. You see a form for posting comments, and a list of the existing comments. (But at the beginning, there are no comments posted yet.)
2. You write a comment in the form and submit it. Your browser sends it via POST to the server.
3. The server updates the list of comments, adding your comment to the list. Then it replies with a 303 redirect, setting the Location: / header to tell the browser to request the main page via GET.
4. The redirect response causes your browser to go back to the same page you started with, sending a GET request, which replies with a 200 OK and a piece of HTML …

One big advantage of Post-Redirect-Get is that as a user, every page you actually see is the result of a GET request, which means you can bookmark it, reload it, and so forth — without ever accidentally resubmitting a form.

### Exercise: Messageboard, Part Three
Update the messageboard server to a full Post-Redirect-Get pattern, as described above. You'll need both do_GET and do_POST handlers; the do_POST handler should reply with a 303 redirect with no response body.

The starter code for this exercise is in the 5_MessageboardPartThree directory. I've added the logic that actually stores the messages into a list; all you need to do is implement the HTTP steps described above.

When you're done, test it in your browser and with the test.py script, as before.

### Solution, part three
You can see my version of the solution to the Messageboard Part Three exercise in the 5_MessageboardPartThree/solution subdirectory. Your code might not look the same as mine; stylistic variations are normal! But if the tests in test.py pass, you've got a good server.

- - -
Next up: [Making requests](ND024_Part4_Lesson07_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
