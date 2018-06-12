# Lesson 4.3 HTTP/1 Problem: Uncompressed Headers

To reduce the time it takes to send data, a lot of websites compress their assets with Gzip or other compression algorithms that work on the web. The H.T. modified boilerplate project uses the Gzip compression. Check below for more information about this. Compression of the data is great, but the request and response headers are still being sent uncompressed. When we think about it, that doesn't make a lot of sense. They are plain text which makes them highly compressible. Also they repeat a lot across requests. The host header's always the same, the cookies are the same, and so are some other headers. In a Google's research paper, they state that on average, headers take up about 800 bytes. Let's look at the potential savings we could have. If a site made 100 requests, roughly 80 kilobytes of data would be taken up by the headers and most of that would be redundant. We'd save a lot of space if we could compress the headers. Unfortunately, we can't do that with HTTP/1. But with HTTP/2, we can!

- [html5-boilerplate/.htaccess at master · h5bp/html5-boilerplate · GitHub](https://github.com/h5bp/html5-boilerplate/blob/master/dist/.htaccess#L709-L795)
- [SPDY: An experimental protocol for a faster web - The Chromium Projects](http://dev.chromium.org/spdy/spdy-whitepaper)

- - -
Next up: [HTTP/1 Problem: Security](ND024_Part4_Lesson04_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
