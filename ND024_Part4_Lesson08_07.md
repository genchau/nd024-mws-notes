# Lesson 8.7 New developments in HTTP

### HTTP/2
The new version of HTTP is called HTTP/2. It's based on earlier protocol work done at Google, under the name SPDY (pronounced "speedy").

Unfortunately, we can't show you very much about HTTP/2 in Python, because the libraries for it are not very mature yet (as of early 2017). We'll still take a look at the motivations for the changes that HTTP/2 brings, though.

Some other languages are a little bit more up to the minute; one of the best demonstrations of HTTP/2's advantages is in [the Gophertiles demo](https://http2.golang.org/gophertiles) from the makers of the Go programming language. In order to see the effects, you'll need to be using a browser that supports HTTP/2. Check CanIUse.com to check that your browser does!

This demo lets you load the same web page over HTTP/1.1 and HTTP/2. It also lets you add extra latency (delay) to each request, simulating what happens when you access a server that's far away or when you're on a slow network. The latency options are zero (no extra latency), 30 milliseconds, 200 milliseconds, and one second. Try it out!

<img src="![screen-shot-2017-01-10-at-11.31.59.png](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/587560c5_screen-shot-2017-01-10-at-11.31.59/screen-shot-2017-01-10-at-11.31.59.png)">

A partly-loaded Gophertiles demo, using HTTP/1 with server latency of 1 second.

#### QUIZ QUESTION
In the Gophertiles demo, try the HTTP/2 and HTTP/1 links with 1 second of latency. What do you notice about the time it takes to load all the images?

HTTP/2 should load much faster than HTTP/1, if your browser is using it!

### Other HTTP/2 demos
You don't have to take the Go folks' word for it, either; there's http://www.http2demo.io/ too, and also https://http2.akamai.com/demo. Each of these demos works similarly to the Gophertiles demo, and will show you much the same effects. The HTTP/2 one is (on average) a whole lot faster, especially with high latency.

But why is it faster? To answer that, we first need to look at some browser behavior in HTTP/1.1.

### Exercise: Multiple connections
Since the early days of HTTP, browsers have kept open multiple connections to a server. This lets the browser fetch several resources (such as images, scripts, etc.) in parallel, with less waiting. However, the browser only opens up a small number of connections to each server. And in HTTP/1.1, each connection can only request a single resource at a time.

As an exercise, take a look at the server in Lesson-3/3_Parallelometer. Try running this server on your computer and accessing it at http://localhost:8000 to see parallel requests happening. The code here is based on the threading server that you've seen earlier in this lesson.

Depending on your browser, you may see different numbers, but most likely the biggest one you'll see is 6. Common browsers such as Chrome, Firefox, and Safari open up as many as six connections to the same server. And under HTTP/1.1, only one request can effectively be in flight per connection, which means that they can only have up to six requests in flight with that server at a time.

### Multiplexing
But if you're requesting hundreds of different tiny files from the server — as in this demo or the Gophertiles demo — it's kind of limiting to only be able to fetch six at a time. This is particularly true when the latency (delay) between the server and browser gets high. The browser can't start fetching the seventh image until it's fully loaded the first six. The greater the latency, the worse this affects the user experience.

HTTP/2 changes this around by multiplexing requests and responses over a single connection. The browser can send several requests all at once, and the server can send responses as quickly as it can get to them. There's no limit on how many can be in flight at once.

And that's why the Gophertiles demo loads much more quickly over HTTP/2 than over HTTP/1.

### Server push
When you load a web page, your browser first fetches the HTML, and then it goes back and fetches other resources such as stylesheets or images. But if the server already knows that you will want these other resources, why should it wait for your browser to ask for them in a separate request? HTTP/2 has a feature called server push which allows the server to say, effectively, "If you're asking for index.html, I know you're going to ask for style.css too, so I'm going to send it along as well."

### Encryption
The HTTP/2 protocol was being designed around the same time that web engineers were getting even more interested in encrypting all traffic on the web for privacy reasons. Early drafts of HTTP/2 proposed that encryption should be required for sites to use the new protocol. This ended up being removed from the official standard … but most of the browsers did it anyway! Chrome, Firefox, and other browsers will only attempt HTTP/2 with a site that is using TLS encryption.

### Many more features
Now you have a sense of where HTTP development has been going in the past few years. You can read much more about HTTP/2 in the [HTTP/2 FAQ](https://http2.github.io/faq/).

- - -
Next up: [Keep learning!](ND024_Part4_Lesson08_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
