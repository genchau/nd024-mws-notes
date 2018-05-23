# Lesson 8.10 Quiz: Cache Photos Quiz

#### Quiz:
Cache photos

#### Initial Setup:
- `git reset --hard`
- `git checkout task-cache-photos`
- file: `public/js/sw/index.js`

#### Objective:
- Implement servePhoto()
- Serve photos from the cache if they're there.
- Otherwise, get them from the network.
- On the response, put in the response and return to display.
- Use storageURL when matching and putting stuff into the image cache.
- `cache.put(URL, response)`
- Use test ID: `cache-photos`

#### Solution:
My first attempt didn't work. Because I didn't return the caches.open(). 
```
function servePhoto(request) {
  // Photo urls look like:
  // /photos/9-8028-7527734776-e1d2bda28e-800px.jpg
  // But storageUrl has the -800px.jpg bit missing.
  // Use this url to store & match the image in the cache.
  // This means you only store one copy of each photo.
  var storageUrl = request.url.replace(/-\d+px\.jpg$/, '');

  // TODO: return images from the "wittr-content-imgs" cache
  // if they're in there. Otherwise, fetch the images from
  // the network, put them into the cache, and send it back
  // to the browser.
  //
  // HINT: cache.put supports a plain url as the first parameter
  return caches.match(storageUrl).then(function(response) {
    return response || fetch(request).then(function(networkResponse) {
      return caches.open(contentImgsCache).then(function(cache) {
        cache.put(storageUrl, networkResponse.clone() );
        return networkResponse;
      });
    });
  });
}
```

#### Notes:
My first attempt didn't work. Because I didn't return the caches.open(). I need to pay attention to how the response is being returned in the chain.

These are the initial changes that Jake start us out with:
- setup image cache.
- create variable for the image cache name.
- create an array to hold all the cache names we keep.
- Delete caches that aren't in our array of caches we keep.
- In fetch handler, we're going to handle URLs that have same origin and have a path that starts with /photo/
- We're going to return with servePhoto().
- In servePhoto() we strip out the width information.
- We used regular expression for the stripping.
```
var contentImgsCache = 'wittr-content-imgs';
var allCaches = [
  staticCacheName,
  contentImgsCache
]
...
return cacheName.startsWith('wittr-') && 
        !allCaches.includes(cacheName);
...
if (requestUrl.pathname.startsWith('/photos/')) {
  event.respondWith(servePhoto(event.request));
  return;
}
...
function servePhoto(request) {
  // /photos/3-2235-2196242458-beb1ff4851-800px.jpg
  var storageUrl = request.url.replace(/-\d+px\.jpg$/,'');
}
```

- - -
Next up: [Cleaning Photo Cache](ND024_Part3_Lesson08_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
