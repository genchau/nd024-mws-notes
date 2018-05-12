# Lesson 17.25 Quiz: Triggering an Update Quiz

#### Quiz:


#### Initial Setup:
- `git reset --hard`
- `git checkout task-update-reload`
- file: `public/js/main/indexController.js`
- file `public/js/index.js`

#### Objective: 
- Send a message to the new service worker to take over.
- Handle the message in the service worker.
- Complete all todo's.
- Listen for the pages controlling service worker changing and using that as a signal to reload the apge.
- Delete the service worker and refresh.
- Make a change to the service worker, the refresh.
- Press refresh on the notification.
- To use test ID, make a change to the service worker.
- Refresh the page for the update notification. **Do not press refresh**.
- Use test ID: `update-reload`
- Within 8 seconds, press refresh on notification.

#### Solution:
`indexController.js`
```
IndexController.prototype._registerServiceWorker = function() {
  ...

  // TODO: listen for the controlling service worker changing
  // and reload the page
  navigator.serviceWorker.addEventListener('controllerchange', function() {
    window.location.reload();
  });
};

IndexController.prototype._updateReady = function(worker) {
  var toast = this._toastsView.show("New version available", {
    buttons: ['refresh', 'dismiss']
  });

  toast.answer.then(function(answer) {
    if (answer != 'refresh') return;
    // TODO: tell the service worker to skipWaiting
    worker.postMessage({action: 'skipWaiting'});
  });
};
```

`index.js`
```
// TODO: listen for the "message" event, and call
// skipWaiting if you get the appropriate message
self.addEventListener('message', function(event) {
	if (event.data.action == 'skipWaiting') {
		self.skipWaiting();
	}
});
```

#### Notes:
This is only one possibility when it comes to handling app updates. We can ask the server for a change log between the new version and the current version. If our update only contains minor things, maybe don't bother the user at all. Let them get the update naturally. Of if the update contains an urgent security fix, maybe refresh the page no matter what the user is doing. That would be annoying experience but it's better than the user using something with a major security flaw.

Anyway, it's fair to say we're well on our way to a full offline first experience. We've got the user onto the latest version as quickly as possible. Next up, we need to work on updating the posts the user sees.

#### To-Do List:
- [X] Unobtrusive app updates
- [X] Get the user onto the latest version
- [ ] Continually update cache of posts
- [ ] Cache photos
- [ ] Cache avatars

- - -
Next up: [Quiz: Caching the Page Skeleton](ND024_Part2_Lesson17_26.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
