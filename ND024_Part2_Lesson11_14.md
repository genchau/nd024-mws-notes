# Lesson 11.14 Quiz: Implementing Keyboard Event Listeners

#### Quiz:
Folder `lesson2-focus/05-radio-group`

Objective: 
- In radiogroup.js add events for Up, Down, Right, Left keystrokes.

<details>
<summary>Solution:</summary>
<p>

```
  RadioGroup.prototype.handleKeyDown = function(e) {
    switch(e.keyCode) {

      case VK_UP:
      case VK_LEFT: {
        
        e.preventDefault();

        if (this.focusedIdx === 0) {
          this.focusedIdx = this.buttons.length - 1;
        }
        else {
          this.focusedIdx -= 1;
        }
        
        break;

      }

      case VK_DOWN:
      case VK_RIGHT: {

        e.preventDefault();

        if (this.focusedIdx === this.buttons.length -1) {
          this.focusedIdx = 0;
        }
        else {
          this.focusedIdx += 1;
        }

        break;
      }

    }

    this.changeFocus(this.focusedIdx); // <-- Hmm, interesting...
  };
```

</p>
</details>

- - -
Next up: [Offscreen Content](ND024_Part2_Lesson11_15.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
