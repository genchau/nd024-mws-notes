# Lesson 17.24 Triggering an Update

So we've got a notification appearing, but our goal is to give the user a button they can press to get the latest version. Clicking this button needs to tell the waiting service worker that it should take over straightaway, bypassing the usual life cycle. Then we want to refresh the page so it reloads with the latest assets from the newest cache.  There are three new components that help us achieve this.

A service worker can call skipWaiting while it's waiting or installing. This signals that it shouldn't queue behind another service worker. It should take over straight away. We want to call this when the user hits the refresh button in our update notification.
```
self.skipWaiting()
```

But how do we send the signal from the page to the waiting service worker? Your page can send messaages to any service worker using `postMessage`. And you can listen for messages in the service worker using the `message` event. So, when the user clicks the refresh button it will send a message to our service worker telling it to call `skipWaiting`. 
```
// from a page:
reg.installing.postMessage({foo: 'bar'});

// in the service worker:
self.addEventListener('message', function(event) {
  event.data; // {foo: 'bar'}
});
```

And the final part, we've already seen navigator.serviceWorker.controller but the page gets an event when its value changes, meaning a new service worker has taken over. We're going to use this as a signal that we should reload the page.
```
navigator.serviceWorker.addEventListener('controllerchange', function() {
  // navigator.serviceWorker.controller has changed
});
```

- - -
Next up: [Quiz: Triggering an Update Quiz](ND024_Part2_Lesson17_25.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
