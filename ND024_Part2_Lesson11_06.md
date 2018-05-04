# Lesson 11.6 Using Tabindex

We can use tabindex attribute to add non-native elements to the tab order. Such as dropdowns, or something off screen like a modal.

tabindex:
- -1 means that the element will NOT be in the tab order. But we can use javascript to programatically focus it, if needed. Useful for off-screen content which comes on-screen at an event.
- 0 means that it will add the element to the natural tab order.
- greater than 0, will bring it to the front of the tab index. If there are more than one element with a tabIndex greater than 0, then the order will be lowest to highest.

Note it is discouraged to use a greater than 0 tabIndex, it is considered anti-pattern. Ideally we are ordering tab order by moving it in the DOM.

- - -
Next up: [Deciding what's in focus](ND024_Part2_Lesson11_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
