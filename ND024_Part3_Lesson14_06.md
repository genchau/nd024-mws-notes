# Lesson 14.6 JS Concatenation

Onto the world of JavaScript. Concatenation here solves two problems at once. First and foremost, it reduces a number of HTTP requests needed to load our page in production. Which is a big deal, especially if we're on a mobile connection with up to 300ms of latency per request. Secondly, it's the most basic variant of dependency management. We put all our script into a folder and instead of having to add script blocks to load them one by one into HTML, we simply add a single script block that points to the generated output file, including all of them concatenated. I say most basic variant because it obviously isn't smart enough to detect dependency chains and the required load order. But solving these problems is a much harder task. Let's keep it simple for now.

- - -
Next up: [JS Concatenation Hands On](ND024_Part3_Lesson14_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
