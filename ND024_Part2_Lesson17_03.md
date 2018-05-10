# Lesson 17.3 Adding a Service Worker To the Project

The service worker will intercept all network requests:
- HTML
- CSS
- JavaScript
- images

This is our service worker javascript file:
`wittr/public/js/sw/index.js`

We can browse to `localhost:8888/sw.js` to see the changes.

Example code of intercepting a fetch request with the service worker:
```
self.addEventListener('fetch', function(event) {
  console.log(event.request);
});
```

- - -
Next up: [Quiz: Registering a Service Worker](ND024_Part2_Lesson17_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
