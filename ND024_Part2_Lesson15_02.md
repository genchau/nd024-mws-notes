# Lesson 15.2 Working with focus styles

Previously any time we focused an element, we relied on the built-in browser focus ring to style that element for us. The focus ring is great because without it, it's impossible for a keyboard user to tell which element is currently focused. In fact, the WebAIM checklist specifically states in section 2.4.7 that it should be visually apparent which page element has the current keyboard focus as you tab through the page. But sometimes the default focus ring may not fit in well with your design. 

[WebAIM: WebAIM's WCAG 2.0 Checklist - for HTML documents](http://webaim.org/standards/wcag/checklist#sc2.4.7)

`:focus` pseudo-class. Example:
```
:focus {
  outline: 1px dotted #FFF;
}
```
Removing the focus outline such as, `outline: 0;`, is considered anti-pattern and should be avoided. We don't want to remove visual indication of where the keyboard focus is at.

Example solution of removing the focus ring and replacing it with the same hover styles:
```
button:hover,
button:focus {
  background: #E91E63; //red
  color: #FFFFFF; //white text
  text-decoration: underline;
}

// to make it more obvious what has focus
button:focus {
  outline: 0; //remove default ring
  box-shadow: 0 0 8px 3px rgba(255, 255, 255, 0.8); //add in a white shadow
}
```

Here's how we fix the radio group from the earlier lesson:
```
.radio:focus {
  outline: 0;
}

.radio:focus::before {
  box-shadow: 0 0 1px 2px #5B9DD9;
}
```

- - -
Next up: [Quiz: Write your own focus styles](ND024_Part2_Lesson15_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
