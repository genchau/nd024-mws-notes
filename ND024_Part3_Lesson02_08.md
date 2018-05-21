# Lesson 2.8 Walkthrough of .ajaxTransport

- send function is 3rd item in the call stack.
- This call creates a new XHR object and stores it in an appropriately named xhr variable.
- It then calls xhr.open method
- Passes in the data that we've provided in the configuration object.
- It then makes its way down to the headers and then loops over each one calling the setRequestHeader method.
- Then it sets up the callback function.
- If there's an error in the request then another code will run.
- If the requests completes successfully, then another code will run.

### $.ajax() Uses XHR Recap
jQuery's ajax method does a lot of things under the hood.
- creates a new XHR object each time it's called
- sets all of the XHR properties and methods
- sends the XHR request

- - -
Next up: [jQuery's Other Async Methods](ND024_Part3_Lesson02_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
