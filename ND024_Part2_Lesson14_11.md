# Lesson 14.11 ARIA Relationships

`aria-labelledby` is a relationship attribute.
A relationship attribute creates some kind of semantic relationship between elements on the page. In the case of `aria-labelledby`, that relationship is this element is labeled by that element. The ARIA 1.1 lists several relationship attributes.

`aria-owns` This allows children element to be associated to the parent.

`aria-activedescendent` As the active element of a page is the one which has focus, setting the active descendent of an element allows us to tell assistive devices that when its parent has focus, it should be presented to the user as the actual focused element. For example, we can use aria-activedescendent to upate to the currently selected list item.

`aria-describedby` provides an accessible description similar to aria-labelledby. Useful for extra explantory text that a user might need. Common example is a password input field, which is accompanied by some descriptive text explaining the requirements for a valid password. So describedby is supplementary to the labeledby.

`aria-posinset` and `aria-setsize` works together. They define the relationship between sibling elements in a set, such as a list.

[Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/#attrs_relationships)

- - -
Next up: [Quiz: Combo Box](ND024_Part2_Lesson14_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
