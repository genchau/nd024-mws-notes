# Lesson 2.8 Setting the Viewport

meta tag for the viewport:
`<meta name="viewport" content="width=device-width, initial-scale=1">`

Example of meta tag in the head section of html:
```
<head>
  <meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML,CSS,XML,JavaScript">
  <meta name="author" content="John Doe">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

This simple meta tag tells the browser that this will be a responsive page and reflow properly without scaling.

`width=device-width `
This will match the page to the screen's width in device independent pixels.

`initial-scale=1`
This tells the browser to establish a one-to-one relationship between device independent pixels and CSS pixels.


- - -
Next up: [Large Fixed Width Elements](ND024_Part2_Lesson02_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
