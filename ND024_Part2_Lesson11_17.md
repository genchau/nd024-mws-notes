# Lesson 11.17 Modals and Keyboard Traps

Keyboard Trap - Tabbing does not move out of the current focus to the next link element. 

WebAIM checklist section 2.1.2 specifically states they keyboard focus should never be locked or trappedd at any one particular page element.

There are times when we do need to trap the keyboard, for instance, in a modal. We do want a temporary keyboard trap while in the modal. This is a tricky technique to implement.


Example code of keyboard trap for modal windows:
```
// Will hold previously focused element
var focusedElementBeforeModal;

// Find the modal and its overlay
var modal = document.querySelector('.modal');
var modalOverlay = document.querySelector('.modal-overlay');

var modalToggle = document.querySelector('.modal-toggle');
modalToggle.addEventListener('click', openModal);

function openModal() {
  // Save current focus
  focusedElementBeforeModal = document.activeElement;

  // Listen for and trap the keyboard
  modal.addEventListener('keydown', trapTabKey);

  // Listen for indicators to close the modal
  modalOverlay.addEventListener('click', closeModal);
  // Sign-Up button
  var signUpBtn = modal.querySelector('#signup');
  signUpBtn.addEventListener('click', closeModal);

  // Find all focusable children
  var focusableElementsString = 'a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [tabindex="0"], [contenteditable]';
  var focusableElements = modal.querySelectorAll(focusableElementsString);
  // Convert NodeList to Array
  focusableElements = Array.prototype.slice.call(focusableElements);

  var firstTabStop = focusableElements[0];
  var lastTabStop = focusableElements[focusableElements.length - 1];

  // Show the modal and overlay
  modal.style.display = 'block';
  modalOverlay.style.display = 'block';

  // Focus first child
  firstTabStop.focus();

  function trapTabKey(e) {
    // Check for TAB key press
    if (e.keyCode === 9) {

      // SHIFT + TAB
      if (e.shiftKey) {
        if (document.activeElement === firstTabStop) {
          e.preventDefault();
          lastTabStop.focus();
        }

      // TAB
      } else {
        if (document.activeElement === lastTabStop) {
          e.preventDefault();
          firstTabStop.focus();
        }
      }
    }

    // ESCAPE
    if (e.keyCode === 27) {
      closeModal();
    }
  }
}

function closeModal() {
  // Hide the modal and overlay
  modal.style.display = 'none';
  modalOverlay.style.display = 'none';

  // Set focus back to element that had it before the modal was opened
  focusedElementBeforeModal.focus();
}
```

`var focusedElementBeforeModal;` is used to remember the last focused element before modal is open.

The following allows javascript to find the modal, overlay, and toggle button.
```
var modal = document.querySelector('.modal');
var modalOverlay = document.querySelector('.modal-overlay');

var modalToggle = document.querySelector('.modal-toggle');
modalToggle.addEventListener('click', openModal);
```

`function openModal()`
1. `focusedElementBeforeModal = document.activeElement;` // Saves the current focus.
2. `modal.addEventListener('keydown', trapTabKey);` // Listens for keyboard stroke, and runs the trapTabKey function.
3. `modalOverlay.addEventListener('click', closeModal);` // Closes the modal when overlay is clicked.
4. `signUpBtn.addEventListener('click', closeModal);` // Closes the modal after sign up button is clicked.
5. The following finds all the focusable children in the modal. It's long and drawn out. 
```
  // Find all focusable children
  var focusableElementsString = 'a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [tabindex="0"], [contenteditable]';
  var focusableElements = modal.querySelectorAll(focusableElementsString);
  // Convert NodeList to Array
  focusableElements = Array.prototype.slice.call(focusableElements);
  ```
  6. The following sets up our first and last tab stops.
```
  var firstTabStop = focusableElements[0];
  var lastTabStop = focusableElements[focusableElements.length - 1];
```
7. `  firstTabStop.focus();` // This focuses the first child when modal is open.
8. The tab key is basically trapped by this code checking where the focus is at and taking control over it.
```
  function trapTabKey(e) {
    // Check for TAB key press
    if (e.keyCode === 9) {

      // SHIFT + TAB
      if (e.shiftKey) {
        if (document.activeElement === firstTabStop) {
          e.preventDefault();
          lastTabStop.focus();
        }

      // TAB
      } else {
        if (document.activeElement === lastTabStop) {
          e.preventDefault();
          firstTabStop.focus();
        }
      }
    }

    // ESCAPE
    if (e.keyCode === 27) {
      closeModal();
    }
  }
```
We basically hide the modal to close it. And then set the focus back to what it was before the modal open.
```
function closeModal() {
  // Hide the modal and overlay
  modal.style.display = 'none';
  modalOverlay.style.display = 'none';

  // Set focus back to element that had it before the modal was opened
  focusedElementBeforeModal.focus();
}
```

- - -
Next up: [Lesson 2 Outro](ND024_Part2_Lesson11_18.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
