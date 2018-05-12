# Lesson 17.26 Quiz: Caching the Page Skeleton

#### Quiz:
Swap out the root page for the skeleton page, but continue to make everything work offline first.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-page-skeleton`
- file: `public/js/sw/index.js`

#### Objective:
- The root page is currently being cached and served in the fetch event.
- My job is to cache the page skeleton instead and serve that if the root page is requested.
- Change the code, refresh the page.
- Reload the page with notification.
- Right-click and view page source. It should be small.
- Use test ID: `serve-skeleton`

#### Solution:
```
self.addEventListener('fetch', function(event) {
  // TODO: respond to requests for the root page with
  // the page skeleton from the cache
  var requestUrl = new URL(event.request.url);

  if (requestUrl.origin == location.origin) {
  	if (requestUrl.pathname == '/') {
  		event.respondWith(caches.match('/skeleton'));
  		return;
  	}
  }
  ...
});
```

#### Notes:


- - -
Next up: [Project Overview](ND024_Part2_LessonProject_01.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
