# Lesson 13.3 Linting

Linting is a way to automatically check your JavaScript code for errors. And it can be done at various stages during development via our editor, our build process or our pre-commit hook in version control. There's not always a right or wrong way in linting. A lot of it is heavily opinionated. So we should choose the configuration that fits our coding style and project. There's also the difference of code style linting versus syntax or structural linting. Syntax or structural linting is what most people refer to when they say linting. These rules check for JavaScript anti-patterns, such as unreachable statements or forgetting to do a strict comparison against null. On the other hand, code style linting can complain about things such as variables that aren't properly camel cased, or a particular way of placing braces for a function. So if linting ensures our code looks sexy and checks for all these potential errors, does that mean our code will always run if the linter is happy? Nope. The linter only checks for potential errors. It doesn't actually have any idea what we are trying to accomplish. So now that we are familar with the concept of linting, let's talk solutions. There are three popular JavaScript linters out there that developers use, JSHint, JSCS, and ESLint. We'll stick with ESLint.

[Comparison of JavaScript linting tools](http://www.sitepoint.com/comparison-javascript-linting-tools/)

[ESLint](http://eslint.org/)

- - -
Next up: [Quiz: How Does Linting Help You Code](ND024_Part3_Lesson13_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
