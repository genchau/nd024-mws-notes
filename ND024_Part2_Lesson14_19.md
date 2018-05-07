# Lesson 14.19 Quiz: Modal Dialog Quiz

#### Quiz:
folder: `lesson5-semantics-aria\21-dialog` -> `modal.js`

Problems:
- ChromeVox does not announce the modal heading.
- We are able to tab out of the modal elements.

#### Solution:

Use `role="dialog` for when the modal opens.

Use `aria-hidden:"true"` on .wrapper. Then set it back to false when closing modal.

- - -
Next up: [Outro Lesson 5](ND024_Part2_Lesson14_20.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
