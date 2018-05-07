# Lesson 14.13 Hidden in Plain Sight

Another important technique in fine tuning the experience for assistive technology users involve ensuring that only the relevant parts of the page are exposed to assistive technology.

Firstly, anything which is explicitly hidden will also not be inluded in the accessibility tree.
- `visibility: hidden`
- `display: none`

Second, not visually rendered, but not explicitly hidden, is still included in the accessibility tree.
- An element that is absolutely positioned off-screen.
- `aria-label` can be used as screen reader only text.
- `aria-labeledby` or `aria-describedby` attribute

Thirdly, excluding content from assistive technology but not visually hidden:
- `aria-hidden` attribute.

[WebAIM: CSS in Action - Invisible Content Just for Screen Reader Users](http://webaim.org/techniques/css/invisiblecontent/)


- - -
Next up: [Quiz: Name That Element Round 2](ND024_Part2_Lesson14_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
