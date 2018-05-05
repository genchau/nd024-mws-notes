# Lesson 11.13 Keyboard Design Patterns

For a custom radio group, to determine what kind of keyboard support it needs, we check ARIA design patterns guide.

[WAI-ARIA Authoring Practices 1.1](https://www.w3.org/TR/wai-aria-practices-1.1/#radiobutton)

We are going to use **roving focus.** We will set `tabindex="0"` for the current focused element. We'll use a keyboard event listener to determine which key the user has pressed to pass the focus to the next element.


Example:
```
Water         <li tabindex="-1">
Tea             <li tabindex="0" checked>
Coffee        <li tabindex="-1">
Cola           <li tabindex="-1">
Ginger Ale  <li tabindex="-1">
```

- - -
Next up: [Quiz: Implementing Keyboard Event Listeners](ND024_Part2_Lesson11_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
