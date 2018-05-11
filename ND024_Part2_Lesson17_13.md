# Lesson 17.13 Quiz: Hijacking Requests 2 Quiz

#### Quiz:
Let's only serve the gif in response to a particular request.

#### Initial Setup:
- `git reset --hard`
- `git checkout gif-response`
- file `public/js/sw/index.js`

#### Objective:
- Only respond with a gif if the request URL ends with .jpg.
- Use event.request
- Use test ID: `gif-response`

#### Solution:
```
self.addEventListener('fetch', function(event) {
	if (event.request.url.endsWith('.jpg')) {
		event.respondWith(
			fetch('/imgs/dr-evil.gif')
		);
	}
});
```

#### Note:
- To figure out what comes back from event.request, we could had read the documentation or looked at it from dev tools after a console.log.

- - -
Next up: [Hijacking Requests 3](ND024_Part2_Lesson17_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
