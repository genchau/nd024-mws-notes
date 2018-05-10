# Lesson 17.4 Quiz: Registering a Service Worker

#### Quiz

The code in our service worker doesn't do anything yet, because it hasn't been registered, but I've been talking long enough, so this is a job for you. 

#### Initial Setup
- `git reset --hard`
- `git checkout task-register-sw`
- file `public/js/sw/index.js`
- file `public/js/main/indexcontroller.js`

#### Objective:
- Register the service worker as soon as our app starts up.
- Go into `indexController.js`.
- Look for `_registerServiceWorker`.
- Add code to register the service worker.
- Scope set to the whole origin, default scope is fine.
- Reload the page and check for errors.
- Use test ID: `registered`

<details>
<summary>Solution:</summary>
<p>

```
IndexController.prototype._registerServiceWorker = function() {
  // TODO: register service worker
  if (!navigator.serviceWorker) return;

  navigator.serviceWorker.register('/sw.js').then(function() {     
    console.log('Registration worked!') ;
  }).catch(function() {
    console.log('Registration failed!');
  });
};
```

</p>
</details>
<br>

Security note:

The scope of the service worker restricts the pages it controls. But it will intercept pretty much any request made by controlled pages, regardless of URL. Not only that, but as we'll start playing with soon, we can mess around with these requests, changing headers or responding with something entirely different. This is pretty powerful, but with great power comes great responsibility. Because of this, service workers are limited to HTTPS, the securer form of HTTP. Remember when we looked at the path requests take through the network? Well when we're serving across plain unencrypted HTTP, any one of these things in the middle can remove, modify, or even add content. This is bad, really bad. You could request a news story from a reputable source and without encryption, what you actually receive could be very different from what the journalist wrote. Malicious scripts could also capture data you input, alter databases, read cookies, entirely without your knowledge. So all around, not such a good thing really. But service workers live longer than pages. So they could be used to persist an attack like this, and that would be really bad. In fact, it's unacceptable to let a potentially evil middleman get control of our service worker. And that's why it only runs on HTTPS. **The service worker has a different life cycle to pages.** 

- - -
Next up: [The Service Worker Lifecycle](ND024_Part2_Lesson17_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
