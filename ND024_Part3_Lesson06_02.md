# Lesson 6.2 Symbols Intro

Symbols are the latest addition to the list of primitive data types available to us in JavaScript. Previously, JavaScript only had numbers, strings, booleans, null, and undefined as its primitives but now symbols have entered the mix.

A symbol is juat a unique identifier. It's most often used to uniquely identify properties within an object. For example, let's assume this bowl is an object. So we put in an apple, orange, and a banana. Keep in mind, these fruits are also objects but now they're properties of this bowl. Now here's where things get interesting. So if we add another banana to the bowl, can you see the problem? When we retrieve the banana, we won't know which specific one to get. We need a way to uniquely identify the bananas. In code we can do banana1 and banana2. But what happens when we have a lot of bananas? Thankfully, with the addition of symbols in ES6, we've got a solution.

- - -
Next up: [Symbols](ND024_Part3_Lesson06_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
