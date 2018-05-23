# Lesson 6.23 Proxies Recap

A proxy object sits between a real object and the calling code. The calling code interacts with the proxy instead of the real object. To create a proxy:

- use the new Proxy() constructor
    - pass the object being proxied as the first item
    - the second object is a handler object
- the handler object is made up of 1 of 13 different "traps"
- a trap is a function that will intercept calls to properties let you run code
- if a trap is not defined, the default behavior is sent to the target object

Proxies are a powerful new way to create and manage the interactions between objects.

- - -
Next up: [Generators](ND024_Part3_Lesson06_24.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
