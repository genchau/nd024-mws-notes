# Lesson 17.18 Quiz: Cache Response Quiz

#### Quiz:


#### Initial Setup:
- `git reset --hard`
- `git checkout task-cache-response`
- file: `public/js/sw/index.js`

#### Objective:
- `caches.match`
- `event.respondWith`
- Use them together for this quiz.
- Respond to the request with an entry from the cache if there is one.
- Hint: call event.respondWith synchronously. We can't call it within a promise handler.
- Otherwise fetch it from the network.
- Put the site in offline mode and see if we get a response.
- Use test ID: `cache-served`

#### Solution:
```
self.addEventListener('fetch', function(event) {
  // TODO: respond with an entry from the cache if there is one.
  // If there isn't, fetch from the network.
  event.respondWith(
  	caches.match(event.request).then(function(response) {
  		return response || fetch(event.request);
  	})
  );
});
```

#### Note:
- If `caches.match(event.request)` doesn't have a match, the promise will resolve with undefined.
- So if the request is truthy, meaning I got a match in the cache I'll return it. 
- Otherwise I'll return a fetch to the network for the original request.
- We are now getting content even when off-line.

#### To-Do List:
- [ ] Unobtrusive app updates
- [ ] Get the user onto the latest version
- [ ] Continually update cache of posts
- [ ] Cache photos
- [ ] Cache avatars

- - -
Next up: [Updating the Static Cache](ND024_Part2_Lesson17_19.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
