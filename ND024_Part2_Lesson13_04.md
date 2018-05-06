# Lesson 13.4 Using Headings

DOM order matters. See 1.3.2 on the WebAIM checklist.

Think of screen readers as losing the 2nd dimension in visual web browsers. Everything becomes serialized into a single stream.

Javascript headings snippet:
```
for (var i = 0, headings = $$('h1,h2,h3,h4,h5,h6');
     i < headings.length; i++) {
   console.log(headings[i].textContent.trim() + " " +  
               headings[i].tagName,
               headings[i]);
}
```

Some websites place headings off screen to accomodate assistive devices, but are not used in the visual display.

- - -
Next up: [Quiz: Using Headings](ND024_Part2_Lesson13_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
