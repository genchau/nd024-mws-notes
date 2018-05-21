# Lesson 2.9 jQuery's Other Async Methods

jQuery has a number of other methods that can be used to make asynchronous calls. These methods are:

- .get()
- .getJSON()
- .getScript()
- .post()
- .load()

Each one of these functions in turn calls jQuery's main `.ajax()` method. These are called "convenience methods" because they provide a convenient interface and do some default configuration of the request before calling `.ajax()`.

Let's look at the `.get()` and `.post()` methods to see how they just call `.ajax()` under the hood.

### Add a Breakpoint
With the project open in a browser:
- load up DevTools
- open the Sources pane
- open the jQuery file
- add a breakpoint to line 8797
- reload the page (this will pause the code at the breakpoint you just made!)

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/March/58ba12cb_ud109-l2-jquery-xhr-set-breakpoint/ud109-l2-jquery-xhr-set-breakpoint.gif">
Breakpoint added to jQuery source file in DevTools. The browser has been reloaded and is paused at the newly added breakpoint.

The first time through the loop, the `method` variable will be `get`. This makes
```
jQuery[ method ] = function(...) { … }
```
become
```
jQuery[ 'get' ] = function( … ) { … }
```
which gives us the `$.get()` method!

On line 8807 you can see that this new `jQuery[ 'get' ]` function returns a call made to `jQuery.ajax( … );`! Notice that before the `.ajax()` call is run, the `type` property is set to the `method` variable (which is still `'get'`). So calling `$.get()` calls `$.ajax()` with some preset properties.

All this was for `'get'`. This exact same code runs right after this for `'post'`! So the code creates a `jQuery[ 'post' ]` function that will call `jQuery.ajax( … )` and set the `type` property to `'post'`.

Isn't it pretty cool how jQuery provides these convenience methods that just end up calling the main `.ajax()` method!?

<img src="./images/ud109-l2-jquery-get-post-methods.gif">
Walking through the jQuery source to see how the $.get() and $.post() methods are created, set some default properties, and then end up running $.ajax().

### Which Method Should You Use?
[From the jQuery website](https://learn.jquery.com/ajax/jquery-ajax-methods/):

It's often considered good practice to use the $.ajax() method over the jQuery provided convenience methods.

- - -
Next up: [Async with jQuery Outro](ND024_Part3_Lesson02_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
