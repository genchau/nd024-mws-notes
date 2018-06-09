# Lesson 2.2 The Netcat Command

### Netcat
Throughout this lesson we'll be using the Netcat command. Netcat is a utility that's used for sending and receiving messages over a network connection. Netcat is known as the Swiss Army knife of networking tools, and we'll be using it to communicate directly with a server.

### Netcat command
There are many variations of Netcat, and the one I'll be using is accessed with the nc command. Here I'm using Netcat to connect to Google on port 80 (the default port for HTTP connections).

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/June/57509a9e_netcat-example/netcat-example.png">
Netcat example

The prompt waits for us to enter the details of the HTTP request. To send a GET request, enter:

    GET / HTTP/1.1

...then make sure you press the enter button twice (once to get to a new line, and one more to indicate that you're finished entering the request's headers). And you'll get something similar to:

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/June/57509af5_header-get/header-get.png">
netcat GET example

### Further Research
- https://en.wikipedia.org/wiki/Netcat
- http://nc110.sourceforge.net/

- - -
Next up: [HTTP Verbs](ND024_Part4_Lesson02_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
