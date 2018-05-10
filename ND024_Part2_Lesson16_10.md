# Lesson 16.10 Exploring the Demo Apps Code

Here's how the site works at the moment:
- We navigate to wittr.
- The browser makes a request for some HTML.
- Like all web requests, this goes via the browser's HTTP cache.
- If there's no match, it continues on to the internet.
- Then hopefully, the response makes its way back to the browser.
- The html the browser receives tells it it needs some CSS, so that's fetched.
- Once that arrives, we get our first render, a page full of content.
- The javascript opens a websocket, a persistent connection that lets the server continually stream newer posts as they arrive. This provides the live updates so the user doesn't miss out on a single piece of *nonsense* posted by the other users.

We'll be working on the javascript files in (video at 0:50):
- `wittr\public\js\main\index.js`
- This file loads the page
- Starting with polyfill that some browsers may need such as promises and URL API
- The main work happens in `wittr\public\js\main\IndexController.js`
- The constructor is run for every page load.
- We have PostsView which helps us update the post on the page.
- ToastsView helps us display error messages.
- Then opens a socket connection, WebSocket.
- The message event is fired when data is received for a new post to display.
- When socket message is called, this method passes the data to PostView.
- While the server is running, any changes you make to these files will be processed and built.
- ES5 is used in the course. The build system uses babel.

- - -
Next up: [Quiz: Changing Connection Types](ND024_Part2_Lesson16_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
