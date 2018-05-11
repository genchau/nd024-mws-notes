# Lesson 17.11 Quiz: Hijacking Requests 1 Quiz

#### Quiz:

#### Initial Setup:
- `git reset --hard`
- `git checkout task-custom-response`

#### Objective:
- Respond with some HTML.
- class="a-winner-is-me"
- Use test ID: html-response

#### Solution:
```
self.addEventListener('fetch', function(event) {
  event.respondWith(
    new Response('<div class="a-winner-is-me"><h1>I just hijacked this page with some custom HTML.</h1><p>Yes, I did.</p></div>', {
      headers: {'Content-Type': 'text/html'}
    })
  );
});
```

#### Note:
- We've created something that works entirely offline first.
- This page will work instantly while offline and even lie-fi.

- - -
Next up: [Hijacking Requests 2](ND024_Part2_Lesson17_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
