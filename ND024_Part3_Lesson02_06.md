# Lesson 2.6 Peek inside $.ajax()

Cake comparison: jQuery is like hiring a baker. The baker is doing the exact same thing I did to bake the cake. Behind the scenes of ajax, it is creating the XHR object and doing the same thing. It just made the process easier on the surface.


We're about to dig into jQuery's source for a second. To do that, you need to:
1. open up the project in a browser
2. open up DevTools
3. switch to the "Sources" pane
4. open up the jquery.js file
    - in Chrome, you can open a specific file by searching for it with ctrl/command + P
5. set a breakpoint on line 9036

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/March/58ba1156_ud109-l2-jquery-xhr-set-breakpoint/ud109-l2-jquery-xhr-set-breakpoint.gif">
A breakpoint set in the jQuery source file right where new XMLHttpRequest object is created

### Debugging in Chrome
TIP: If you've never done it before, debugging is a JavaScript application can seem like a complicated process. We'll be looking at the important parts of DevTools in this course, but if you're looking for a deeper dive, check out the following resources on Google's Developer site:
- [Pause Your Code With Breakpoints  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/javascript/breakpoints)
- [JavaScript Debugging Reference  |  Tools for Web Developers  |  Google Developers](https://developers.google.com/web/tools/chrome-devtools/javascript/reference)

- - -
Next up: [Review the Call Stack](ND024_Part3_Lesson02_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
