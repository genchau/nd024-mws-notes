# Lesson 15.5 Styling with Aria

When we're building components, it's a very common practice to reflect the state of the component using CSS classes. For instance here is a toggle button that I've built and when I click on it, it's going to go into a pressed state. And in order to style that state, my JavaScript has added a pressed class up here to my class list. And because I want to have good semantics, my JavaScript has also set the aria-pressed for this toggle button to true. And the style of a pressed state of the button in my CSS, I have a selector that targets any instance of the button that has this pressed class. Now a useful technique which we can employ in this situation is to actually remove this pressed class, and instead replace it with aria attributes. So I'm going to update the selector so that it looks like this. Here I'm using a CSS attribute selector to target the element when aria-pressed is true. And the effect is the same as before, but now I get this nice verification that I've set the aria state properly because it's visually reflected by my element. Not to mention I can cut down on some of my CSS noise by getting rid of additional selectors and replacing them with aria attributes.

Example code:
```
<div class="toggle pressed"
      tabindex="0"
      role="button"
      aria-labelledby="muteLbl"
      aria-pressed="true"></div>
```

`.toggle.pressed` vs `.toggle[aria-pressed="true"]`
```
.toggle[aria-pressed="true"] {
  // transition to pressed state
}
```

- - -
Next up: [Quiz: Quiz: Styling with ARIA](ND024_Part2_Lesson15_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
