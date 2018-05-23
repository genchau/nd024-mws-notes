# Lesson 8.9 Cache Photos

We want to cache the photos. We can use IDB to store the photos but that requires being able to read the pixel data and converting it. The cache, will stream the data instead of returning a lump. Streaming is more efficient and leads to faster renders. The cache API is a better fit for the photos.

The images being served are responsive, the browser load different size photos depending on viewport. So we'll wait until the browser makes the request, we'll hear it in service worker. We'll fetch from network, and store in cache also sending it to the page. We'll create a separate cache. We'll reset the content of our static cache whenever we update our JavaScript or CSS, but we want the photos to live between versions of our app. Next time we get a request for an image that we already have cached, we simply return it. The trick is, we'll return whatever size image we have on the cache, even if the browser requests something different.

We can only use the body of a response once:
- response.json()
- response.blob()
- event.respondWith(response);
The original data will be gone after running any one of those. So we need to use `response.clone()` as the parameter if we plan on returning the response.

example:
```
cache.put(request, response.clone());
return response;
```

- - -
Next up: [Quiz: Cache Photos Quiz](ND024_Part3_Lesson08_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
