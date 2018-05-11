# Lesson 17.16 Caching and Serving Assets

So far, we've seen how to hijack requests and respond to them differently. We've even created responses ourselves, meaning we can respond without using the network at all. However, if we want to be able to load Wittr without using the network, we need somewhere to store the HTML, the CSS, the JavaScript, the images, the web font. Thankfully, there is such a place, the cache API. 

The cache API gives us this caches object on the global. If I want to create or open a cache, I call `caches.open` with the name of cache. That returns a promise for a cache of that name. If I haven't opened a cache of that name before, it creates one and returns it. A cache box contains request and response pairs from any secure origin. We can use it to store fonts, scripts, images, and anything really, from both our own origin as well as elsewhere on the web. 

We can add cache itm using `cache.put` and pass in a request or a URL and a response. Or I can use `cache.addAll`. This takes an array of requests or URLs, fetches them, and puts the **request-response pairs** into the cache. This operation's atomic. If any of these fail to cache, none of them are added. addAll uses fetch under the hood, so bear in mind that requests will go via the browser cache. Later, when we want to get something out of the cache, we can call `cache.match`, passing in a request or a URL. This will return a promise for a matching response if one is found, or null otherwise. `caches.match` does the same, but it tries to find a match in any cache, starting with the oldest. So we have somewhere to store our stuff, but when should we store it? Thankfully, there's another service worker event that helps here. 

When a broswer runs a service worker for the first time, an event is fired within it, the install event. The browser won't let this new service worker take control of pages until its install phase is completed, and we're in control of what that involves. We use it as an opportunity to get everything we need from the network and create a cache for them. So let's do that for Wittr.

Over in the service worker file, I'm going to add a listener for the install event. `event.waitUntil` lets us signal the progress of the install. We pass it a promise. If and when the promise resolves, the browser knows the install is complete. If the promise rejects, it knows the install failed, and this service worker should be discarded.


```
caches.open('my-stuff').then(function(cache) {
  //...
});

cache.put(request, response);
cache.addAll([
  '/foo',
  '/bar'
]);
cache.match(request);
caches.match(request);
```

```
self.addEventListener('install', function(event) {
  event.waitUntil(
  
  );
});
```


- - -
Next up: [Quiz: Install and Cache Quiz](ND024_Part2_Lesson17_17.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
