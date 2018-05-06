# Lesson 14.6 Quiz: Custom radio button group with ARIA

We can apply ARIA roles and properties to an element to modify the way it is exposed in the accessibility tree.

We're going to start with the radio group example.
Make sure the state is kept in sync with the visual state of the button.


#### Quiz:
folder: `lesson5-semantics-aria/06-radio-group` -> `radiogroup.js`

Objective: 
- In ARIA practices document, find the requirements for radio groups.
- Implement the requirements into the code.

#### Solution:
The ARIA practices document:
- Container with a `role="radiogroup"`.
- Individual radio buttons `role="radio"`
- If selected, `aria-checked="true"`
- If not selected, `aria-checked="false"`

Implementation:
- In function RadioGroup(id), add:
`this.el.setAttribute('role', 'radiogroup');`
- In the button iteration,  add:
`button.setAttribute('role', 'radio');`
- In the changeFocus(), in the old button add:
`this.focusedButton.setAttribute('aria-checked', 'false');`
- In the new button add:
`this.focusedButton.setAttribute('aria-checked', 'true');`


[WAI-ARIA Authoring Practices 1.1](https://www.w3.org/TR/2016/WD-wai-aria-practices-1.1-20160317/#radiobutton)

- - -
Next up: [More Ways to Label](ND024_Part2_Lesson14_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
