# Lesson 1.13 XHR Recap

### XHR Usage Review
There are a number of steps you need to take to send an HTTP request asynchronously with JavaScript.

### To Send An Async Request
- create an XHR object with the XMLHttpRequest constructor function
- use the .open() method - set the HTTP method and the URL of the resource to be fetched
- set the .onload property - set this to a function that will run upon a successful fetch
- set the .onerror property - set this to a function that will run when an error occurs
- use the .send() method - send the request

### To Use The Response
- use the .responseText property - holds the text of the async request's response

- - -
Next up: [XHR Outro](ND024_Part3_Lesson01_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
