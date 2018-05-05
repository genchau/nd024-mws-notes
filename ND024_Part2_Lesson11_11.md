# Lesson 11.11 Skip Links

Websites can have quite a bit of page scaffolding, such as navigation, sublists, side bars, hamburger menus. That's a lot of things to go through before reaching the main content.

Imagine using a switch device, which is activated by tapping your head, to go through 20 navigational links before reaching the main content. click, click, click, click, click, click, click, click, click, click, click, click, click, click, click, click, click, click. 

There's an easy solution to this. We can create a hidden link that allows the user to jump straight to the page content.

We call these **skip links**.

Example implementation (placed at top of DOM so it's first on tab order):
```
<a href="#maincontent" class="skip-link" >Skip to main content</a>

<main id="maincontent" tabindex=-1>
...
</main>

.css
.skip-link {
  position: absolute;
  top: -40px;  // this is to hide the element
  left: 0;
  background: #BF1722;
  color: white;
  padding: 8px;
  z-index: 100;
}
.skip-link:focus {
  top: 0;
}
```

- - -
Next up: [Focus in Complex Components](ND024_Part2_Lesson11_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
