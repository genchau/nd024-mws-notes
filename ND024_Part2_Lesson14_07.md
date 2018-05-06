# Lesson 14.7 More Ways to Label

ARIA design practices's advice for radio group pattern notes:
- It is recommended that both th radio group and the radio button have a label that is visible and referenced using the aria-labelledby property.
- And use an aria-describedby property to add additional information to the radio buttons or radio group.

ARIA has several mechanism for adding labels and description to elements. ARIA is the only way to add accessible help or description text.

Accessible labels:
- `aria-labelledby` allows us to specify an element ID to refer to another element in the DOM as this element's label.

`aria-labelledby` 
- can take a list of ID refs to compose a label out of multiple elements.
- overrides all other name sources for an element, such as `aria-label`, HTML label.

- - -
Next up: [Quiz: Name That Element!](ND024_Part2_Lesson14_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
