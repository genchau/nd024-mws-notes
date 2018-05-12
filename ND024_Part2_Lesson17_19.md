# Lesson 17.19 Updating the Static Cache

Force update reloads the service worker on every refresh and causes it to install.

Here's how we work with the service worker lifecycle. To get the CSS to update, we need to make a change to the service worker. The browser will then treat this updated worker as a new version. Because it's new, it'll get its own install event where it'll fetch the JavaScript, HTML, and our updated CSS and put them in a new cache. It won't put them in a different cache automatically. We need to change the name of our cache to make this happen. We create a new cache because we don't want to disrupt the cache that's already there being used by the old service worker and the pages it controls. Then, once the old service worker is released and we're ready to take over, we delete the old cache so the next page load gets resources from the new cache, meaning it gets the latest CSS. 

Use this code to run something, once the new service worker is activated:
```
self.addEventListener('activate', function(event) {
  // ...
});
```
`caches.delete(cacheName);` Used to delete a cache. Returns a promise.
`caches.keys();` Used to get  the names of all the caches. Returns a promise.
- - -
Next up: [Quiz: Update Your CSS Quiz](ND024_Part2_Lesson17_20.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
