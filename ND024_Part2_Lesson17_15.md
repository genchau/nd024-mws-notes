# Lesson 17.15 Quiz: Hijacking Requests 3 Quiz

#### Quiz:
We've seen a custom 404 response served by the service worker. But what if we wanted to serve an image instead?

#### Initial Setup:
- `git reset --hard`
- `git checkout error-handling`
- file `public/js/sw/index.js`

#### Objective:
- Instead of a custom 404 text, respond with dr-evil.gif.
- Use test ID: `gif-404`

#### Solution:
```
self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).then(function(response) {
      if (response.status == 404) {
        return fetch('imgs/dr-evil.gif');
      }
      return response;
    }).catch(function() {
      return new Response("Uh oh, that totally failed!");
    })
  );
});
```

#### Note:
- Return a promise within a promise, it passes the eventual value to the outer promise. 
- Rather than return a response we're going to return a fetch for the gif's URL and that's it.

- - -
Next up: [Caching and Serving Assets](ND024_Part2_Lesson17_16.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
