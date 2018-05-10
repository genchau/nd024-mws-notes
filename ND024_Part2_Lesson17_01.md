# Lesson 17.1 An Overview of Service Worker

The service worker is a simple JavaScript file that sits between us and network requests. It's a type of web worker. Meaning it runs separately from our page. It isn't visible to the user. It can't access the DOM, but it does control pages and by control, we mean, intercepts requests as the browser makes them. From there, we can do, well, whatever we want really. We can send the request off to the network, as per usual or we can skip the network. Go to some kind of cache or create a custom random response, or any combination of those things.

Register a service worker with the following code. It will return a promise. Re-registering will simply return a promise for the existing registration.
```
navigator.serviceWorker.register('/sw.js').then(function(reg) {     
  console.log('Yay!') ;
} ).catch(function(err) {
  console.log('Boo!');
});
```

We can define a scope so the service worker will only control pages with the defined URL in the scope.
```
navigator.serviceWorker.register('/sw.js', {
  scope: '/my-app/'
});
```

Event listeners:
```
self.addEventListener('install', function(event) {
  // ...
});
self.addEventListener('activate', function(event) {
  // ...
});
self.addEventListener('fetch', function(event) {
  // ...
});
```

For unsupported browsers:
```
if (navigator.serviceWorker) {
  navigator.serviceWorker.register('/sw.js');
}
```

- - -
Next up: [Quiz: Scoping Quiz](ND024_Part2_Lesson17_02.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
