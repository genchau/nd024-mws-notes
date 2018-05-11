# Lesson 17.10 Hijacking Requests

So far we've setup our own service worker, learned its life cycle, and explored the dev tools, but we haven't really used our service worker to do anything yet. Currently, the server's having all the fun when it comes to sending content back to the browser. Well, now it's our turn to have fun. So far we've seen requests go from the page, through the service worker fetch event, then onto the network as usual, through the HTTP cache. But now we're going to catch the request as it hits the service worker, and respond ourselves, so nothing goes to the network. Obviously, this is an important step in going offline first, so let's make it happen. 

Over in the service worker script, we can call event.respondWith. This tells the browser that we're going to handle this request ourselves. event.respondWith takes a response object or a promise that resolves with a response. One way to create a response is well, new response. The first parameter is the body of the response, which can be a block, a buffer, some other things, but at its simplest it can take a string. So here I'm going to respond with Hello world.

file: `public/js/sw/index.js`

```
self.addEventListener('fetch', function(event) {
  event.respondWith(
    new Response('Hello <b>world</b>', {
      headers: {'foo': 'bar'}
    })
  );
});
```

We can set headers as part of the response with `headers: {'foo': 'bar'}`.

- - -
Next up: [Quiz: Hijacking Requests 1 Quiz](ND024_Part2_Lesson17_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
