# Lesson 15.6 Quiz: Quiz: Styling with ARIA

#### Quiz:
folder: `lesson6-styling/02-style-aria-states`

Objective: 
See if you can do a better job styling this button using ARIA states. One huge benefit to styling with ARIA is that it provides visual feedback that you've applied the state correctly, which can act as a safeguard when you're testing and debugging your code.

#### Solution:

```
.disclosure-button[aria-expanded="false"] .icon::after {
  content: '▶';
}

.disclosure-button[aria-expanded="true"] .icon::after {
  content: '▼';
}

.disclosure-content[aria-hidden="true"] {
  visibility: hidden;
  opacity: 0;
}

.disclosure-content[aria-hidden="false"] {
  visibility: visible;
  opacity: 1;
}

```

- - -
Next up: [Responsive design for multi-device](ND024_Part2_Lesson15_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
