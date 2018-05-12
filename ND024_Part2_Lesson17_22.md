# Lesson 17.22 Adding UX to the Update Process

So now we have a safe way to update our static asseets. But as we saw in the previous chapter, the changes would be in the waiting worker. Ideally we want users to be on the latest version as soon as possible. We want them to get the latest features, the latest design, and of course bug fixes. We want to be able to tell the user an update is available, and give them the option to refresh the page to get the new version.

We need an update notification.

The API give us insight into the service worker lifecycle. When we register a service worker it returns a promise. That promise fulfills with a service worker registration object. This object has properties and methods relating to the service worker registration. We get methods to do things like unregister, or trigger an update. We get free properties installing, waiting, and active. The registration object will emit an event when a new update is found, called update found.

```
navigator.serviceWorker.register('/sw.js').then(function(reg) {
  reg.unregister();
  reg.update();
  reg.installing; // may fail and gets thrown away.
  reg.waiting; // we know there's an updated service worker.
  reg.active;
  reg.addEventListener('updatefound', function() {
    // reg.installing has changed
  });
});
```

On the service worker object we can look at their state.
```
var sw = reg.installing;
console.log(sw.state); // ...logs "installing"
// state can also be:
// "installed"
// "activating"
// "activated" // ready for fetch events
// "redundant" // thrown away
sw.addEventListener('statechange', function() {
  // sw.state has changed
});
```

`navigator.serviceWorker.controller` refers to the service worker that is currently controlling the page. We want to tell the user when there's an update ready. But because the service worker update happens in the background, the update could be ready and waiting, it could be in progress, or it might not have started yet. This means we need to look at the state of things when the page loads. But we may also need to listen for future changes. For instance, if there's no controller, that means this page didn't load using a serviceWorker. So they loaded the content from the network. 
```
if (!navigator.serviceWorker.controller) {
  // page didn't load using a service worker
}
```

Otherwise we need to look at the registration. If there's a waiting worker there's an update ready and waiting. We tell the user about it. Otherwise if there isn't installing worker there's an update in progress. Of course the update may fail. So, we listen to the state changes to track it and if it reaches the installed state. We tell the user. 
```
if (reg.waiting) {
  // there's an update ready!
}
if (reg.installing) {
  // there's an update in progress
  reg.installing.addEventListener('statechange', function() {
    if (this.state == 'installed') {
      // there's an update ready!
    }
  });
}
```

Otherwise, we listen for the update found event. When that fires we track the state of the installing worker and if it reaches the installed state we tell the user. That's how we can tell user about updates, whether they're already there, in progress, or start some time later.
```
reg.addEventListener('updatefound', function() {
  reg.installing.addEventListener('statechange', function() {
    if (this.state == 'installed') {
      // there's an update ready!
    }
  });
});
```

- - -
Next up: [Quiz: Adding UX Quiz](ND024_Part2_Lesson17_23.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
