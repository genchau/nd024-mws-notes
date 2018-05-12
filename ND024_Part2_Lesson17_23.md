# Lesson 17.23 Quiz: Adding UX Quiz

#### Quiz:
Tell the user when there's an update available.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-update-notify`
- file: `public/js/main/indexController.js`

#### Objective:
- method: `_updateReady`, calling this will show a notification to the user.
- We need to call _updateReady at the correct times.
- Follow the comments in the code.
- Delete the service worker, then refresh the page.
- Make a change to the service worker. (commenting works.)
- Refresh the page.
- If the code is working, a notification should pop up.
- Use test ID: `update-notify`

#### Solution:
```
IndexController.prototype._registerServiceWorker = function() {
  if (!navigator.serviceWorker) return;

  var indexController = this;

  navigator.serviceWorker.register('/sw.js').then(function(reg) {
    // TODO: if there's no controller, this page wasn't loaded
    // via a service worker, so they're looking at the latest version.
    // In that case, exit early
    if (!navigator.serviceWorker.controller) {
      return;
    }

    // TODO: if there's an updated worker already waiting, call
    // indexController._updateReady()
    if (reg.waiting) {
      indexController._updateReady();
      return;
    }

    // TODO: if there's an updated worker installing, track its
    // progress. If it becomes "installed", call
    // indexController._updateReady()
    if (reg.installing) {
      indexController._trackInstalling(reg.installing);
      return;
    }

    // TODO: otherwise, listen for new installing workers arriving.
    // If one arrives, track its progress.
    // If it becomes "installed", call
    // indexController._updateReady()
    reg.addEventListener('updatefound', function() {
      indexController._trackInstalling(reg.installing);
    });
  });
};

IndexController.prototype._trackInstalling = function(worker) {
  var indexController = this;

  worker.addEventListener('statechange', function() {
    if (worker.state == 'installed') {
      indexController._updateReady();
    }
  });
};
```

#### Notes:


- - -
Next up: [Triggering an Update](ND024_Part2_Lesson17_24.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
