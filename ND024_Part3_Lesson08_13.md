# Lesson 8.13 Quiz: Caching Avatars

#### Quiz:
Cache the avatar, but fetch a new one too.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-cache-avatars`
- file: `public/JS/sw/index.js`

#### Objective:
- Retrieve avatar from cache.
- Also fetch avatar from network to update cache.
- Avatars are responsive with density.
- Cache avatars in same cache as images.
- call serveAvatar for avatar URLs.
- implement serveAvatar
- return from cache if exist.
- get from network and add to cache.
- Use test ID: `cache-avatars`

#### Solution:
I got it to work, yay!
```
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);

  if (requestUrl.origin === location.origin) {
    if (requestUrl.pathname === '/') {
      event.respondWith(caches.match('/skeleton'));
      return;
    }
    if (requestUrl.pathname.startsWith('/photos/')) {
      event.respondWith(servePhoto(event.request));
      return;
    }
    // TODO: respond to avatar urls by responding with
    // the return value of serveAvatar(event.request)
    if (requestUrl.pathname.startsWith('/avatars/')) {
      event.respondWith(serveAvatar(event.request));
      if (needUpdateAvatar) updateAvatar(event.request);
      return;
    }
  }

  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});

function serveAvatar(request) {
  // Avatar urls look like:
  // avatars/sam-2x.jpg
  // But storageUrl has the -2x.jpg bit missing.
  // Use this url to store & match the image in the cache.
  // This means you only store one copy of each avatar.
  var storageUrl = request.url.replace(/-\dx\.jpg$/, '');

  // TODO: return images from the "wittr-content-imgs" cache
  // if they're in there. But afterwards, go to the network
  // to update the entry in the cache.
  //
  // Note that this is slightly different to servePhoto!
  return caches.open(contentImgsCache).then(function(cache) {
    return cache.match(storageUrl).then(function(response) {
      if (response) {
        needUpdateAvatar = true;
        return response;
      }
       
      needUpdateAvatar = false;
      return updateAvatar(request);
    });
  });
}

function updateAvatar(request) {
  var storageUrl = request.url.replace(/-\dx\.jpg$/, '');

  return caches.open(contentImgsCache).then(function(cache) {
    return fetch(request).then(function(networkResponse) {
      cache.put(storageUrl, networkResponse.clone());
      return networkResponse;
    });
  });
}
```

#### Notes:
Instructor's solution:
```
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);

  if (requestUrl.origin === location.origin) {
    if (requestUrl.pathname === '/') {
      event.respondWith(caches.match('/skeleton'));
      return;
    }
    if (requestUrl.pathname.startsWith('/photos/')) {
      event.respondWith(servePhoto(event.request));
      return;
    }
    // TODO: respond to avatar urls by responding with
    // the return value of serveAvatar(event.request)
    if (requestUrl.pathname.startsWith('/avatars/')) {
      event.respondWith(serveAvatar(event.request));
      return;
    }
  }

  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});

function serveAvatar(request) {
  // Avatar urls look like:
  // avatars/sam-2x.jpg
  // But storageUrl has the -2x.jpg bit missing.
  // Use this url to store & match the image in the cache.
  // This means you only store one copy of each avatar.
  var storageUrl = request.url.replace(/-\dx\.jpg$/, '');

  // TODO: return images from the "wittr-content-imgs" cache
  // if they're in there. But afterwards, go to the network
  // to update the entry in the cache.
  //
  // Note that this is slightly different to servePhoto!
  return caches.open(contentImgsCache).then(function(cache) {
    return cache.match(storageUrl).then(function(response) {
      var networkFetch = fetch(request).then(function(networkResponse) {
        cache.put(storageUrl, networkResponse.clone());
        return networkResponse;
      });

      return response || networkFetch;
    });
  });
}
```

- - -
Next up: [Outro](ND024_Part3_Lesson08_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
