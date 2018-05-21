# Lesson 2.7 Review the Call Stack

The DevTools has a ton of helpful information! If you're not familiar with them, you really should spend some learning about all of its features. It'll make developing and debugging websites a lot easier! One helpful piece of info that DevTools provides is the JavaScript Call Stack. This displays the order of function calls that are in progress. The function at the bottom of the stack is the first one to run. It calls the second one on the stack...the second calls the third, the third… you get the idea. A function stays on the stack until the one above it returns.

We can click on the bottom function in the stack (the `anonymous function`) to see that what kicked all this code off was the `$.ajax()` call for the Unsplash images. That `$.ajax()` call in turn calls `transport.send()`, which calls `options.xhr()`, which creates a new `XMLHttpRequest()` object!

So the order is:

our code in an anonymous function calls `.ajax()`
`.ajax()` calls a `.send()` method
`.send()` calls `options.xhr()`
`options.xhr()` calls `jQuery.ajaxSettings.xhr` which creates a new XHR object

<img src="./images/ud109-l2-jquery-xhr-call-stack.gif">
Clicking through the call stack to see the order of function calls

- - -
Next up: [Walkthrough of .ajaxTransport](ND024_Part3_Lesson02_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
