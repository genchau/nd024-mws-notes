# Lesson 17.20 Quiz: Update Your CSS Quiz

#### Quiz:
Your task is to update the CSS in a way that doesn't disrupt the currently running version of the site.

#### Initial Setup:
- `git reset --hard`
- `git checkout task-handling-updates`
- file: `public/js/sw/index.js`

#### Objective:
- Change the theme of the site. (Site header color has to change.)
- `public/scss/_theme.scss`
- Then in service worker we need to update the cache name.
- Use the activate event to remove the old cache.
- A service worker should be waiting, **DON'T activate yet.**
- Use test ID: `new-cache-ready`

#### Solution:
```
var currentCacheName = 'wittr-static-v2';

self.addEventListener('activate', function(event) {
  event.waitUntil(
    // TODO: remove the old cache
    caches.keys().then(function(cacheNames) {
    	return Promise.all(
	    	cacheNames.filter(function(cacheName) {
	    		return cacheName.startsWith('wittr-') && 
	    					 cacheName != staticCacheName;
	    	}).map(function(cacheName) {
	    		return caches.delete(cacheName); 
	    	}) 
    	);
    })
  );
});
```

#### Note:
- This test was tricky. In order to pass the test, v1 and v2 cache needs to be alive. The main.css in v1 and v2 cache **has to be different**. If not it won't pass the test, "There's a new cache, but the CSS looks the same". 
- `Promise.all()` method returns a single promise that resolves when all of the promises in the iterable argument have resolved. 
- `filter()` method creates a new array with all elements that pass the test implemented by the provided function. It is looking for return true or false conditions.
- `map()` method creates a new array with the results of calling a provided function on every element in the calling array.

- - -
Next up: [Quiz: Update Your CSS 2](ND024_Part2_Lesson17_21.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
