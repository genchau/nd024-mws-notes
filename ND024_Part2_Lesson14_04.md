# Lesson 14.4 What can ARIA do for you?

ARIA attributes can be used in a number of ways to augment the existing ways we can express semantics in HTML.

Div element explicitly and deliberately has no native semantis.

We can use ARIA attribute to modify existing elements semantics. For example a button element being implemented as an on/off switch by using `role="switch"`.

We can simply add `aria-label=`:
```
<button class="glyph" aria-label="Filter">
<div class="menu-glyph"></div></button>
```

`role="alert"` can immediately alert the screen reader to an event that needs attention:
```
<div role="alert">Could no connect!</div>
```

[Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/)

- - -
Next up: [Roleplaying](ND024_Part2_Lesson14_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
