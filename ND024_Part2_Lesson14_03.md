# Lesson 14.3 Quiz: First Steps with ARIA

#### Quiz:

Folder: `lesson5-aria/03-first-steps`, `checkboxes.js`

Objective: 
- Fully implement ARIA for the custom checkbox.
- Give it a role of checkbox.
- aria-checked that matches the checked state

Solution using `setAttribute`:

```
function Checkbox(el) {
  this.el = el;

  this.el.addEventListener('keydown', this.handleKeyDown.bind(this));
  this.el.addEventListener('click', this.toggle.bind(this));

  // Initialize role and aria-checked state.
  this.el.setAttribute('role', 'checkbox');
  if (this.el.hasAttribute('checked')) {
    this.el.setAttribute('aria-checked', 'true');
  } else {
    this.el.setAttribute('aria-checked', 'false');
  }
}

Checkbox.prototype.handleKeyDown = function(e) {
  switch(e.keyCode) {
    case VK_ENTER:
    case VK_SPACE: {
      this.toggle();
      break;
    }
  }
};

Checkbox.prototype.toggle = function() {
  if (this.el.hasAttribute('checked')) {
    this.el.removeAttribute('checked');

    // Keep checked attribute and aria-checked in sync.
    this.el.setAttribute('aria-checked', 'false');
  } else {
    this.el.setAttribute('checked', '');

    // Keep checked attribute and aria-checked in sync.
    this.el.setAttribute('aria-checked', 'true');
  }
};
```

- - -
Next up: [What can ARIA do for you?](ND024_Part2_Lesson14_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
