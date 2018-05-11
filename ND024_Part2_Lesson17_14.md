# Lesson 17.14 Hijacking Requests 3

This time we're going to fetch the request and then look at it before deciding what to return.

```
self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).then(function(response) {
      if (response.status == 404) {
        return new Response("Whoops, not found");
      }
      return response;
    }).catch(function() {
      return new Response("Uh oh, that totally failed!");
    })
  );
});
```

- If we navigate to a non-existent page, we'll return "Whoops, not found". 
- If we take the server offline, we'll return "Uh oh, that totally failed!". 
- If everything is working, we are returning the network fetch per usual.

- - -
Next up: [Quiz: Hijacking Requests 3 Quiz](ND024_Part2_Lesson17_15.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
