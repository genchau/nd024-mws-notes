# Lesson 13.8 Link Text

There are 3 common patterns that can cause the screen reader to miss links in the page:

First pattern, link anti-patterns:
- Using a span
- anchor tag without an href attribute
- also when you want something performs an action, but looks like a link.

**We should absolutely use an anchor tag with an href attribute, no exceptions.**

[WebAIM: WebAIM's WCAG 2.0 Checklist - for HTML documents](http://webaim.org/standards/wcag/checklist#sc2.4.9)

Second pattern is the opposite problem. Something which was implemented as a link but really acts like a button. Just simply use the button tag.

Third example is where we have an image used as link content. Just simply add an alt text.

learn more: these should be changed to "learn more about responsive layouts" instead of just "learn more". Imagine having 10 of these links.

- - -
Next up: [Quiz: Link Text](ND024_Part2_Lesson13_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
