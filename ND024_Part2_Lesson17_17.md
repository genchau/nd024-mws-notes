# Lesson 17.17 Quiz: Install and Cache Quiz

#### Quiz:

#### Initial Setup:
- `git reset --hard`
- `git checkout task-install`
- file `public/js/sw/index.js`

#### Objective:
- There's an array of URLs to cache in the code.
- Cache the URLs in a cache named wittr-static-v1.
- Use test ID: `install-cached`

#### Solution:
```
self.addEventListener('install', function(event) {
  event.waitUntil(
    // TODO: open a cache named 'wittr-static-v1'
    // Add cache the urls from urlsToCache
    caches.open('wittr-static-v1').then(function(cache) {
    	return cache.addAll([
			'/',
			'js/main.js',
			'css/main.css',
			'imgs/icon.png',
			'https://fonts.gstatic.com/s/roboto/v15/2UX7WLTfW3W8TclTUvlFyQ.woff',
			'https://fonts.gstatic.com/s/roboto/v15/d-6IYplOFocCacKzxwXSOD8E0i7KZn-EPnyo3HZu7kw.woff'
    	]);
    })
  );
});
```

#### Note:
`cache.addAll` returns a promise, so we return it.

- - -
Next up: [Quiz: Cache Response Quiz](ND024_Part2_Lesson17_18.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
