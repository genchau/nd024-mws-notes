# Lesson 17.12 Hijacking Requests 2

This time we're going to respond with a fetch from the network.

Side note: XHR API or XMLHttpRequests is 15 years old.

```
self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch('/imgs/dr-evil.gif')
  );
});
```

- - -
Next up: [Quiz: Hijacking Requests 2 Quiz](ND024_Part2_Lesson17_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
