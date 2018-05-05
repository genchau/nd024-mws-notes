# Lesson 12.13 Writing Semantic HTML: The Name Game

'Label' interchangeably with 'Name'.

2 types:
- Visible labels
- text alternative

The WebAIM Guideline 1.1, checklist talks about how to create visible and non-visible labels.

Easy one:
`<button>Search</button` there's no extra accessible work needed.

Problem: with form inputs:
`<input type="checkbox" checked name="jLetter'> Receive promotional offers?`
The checkbox for this element does not create a programmatically accessible label. :unamused:

Fix: 
```
<label>
  <input type="checkbox" checked name="jLetter'> Receive promotional offers?
</label>
```

or:
```
<input type="checkbox" checked name="jLetter' id="letter">
<label for="letter">Receive promotional offers?</label>
```

[WebAIM: WebAIM's WCAG 2.0 Checklist - for HTML documents](http://webaim.org/standards/wcag/checklist#g1.1)

- - -
Next up: [Quiz: Labeling Input Elements](ND024_Part2_Lesson12_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
