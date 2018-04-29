# Lesson 3.4 Adding a basic media query 2

Options to using media query:
- media attribute on a linked style sheet
  - many small http requests
```
<link rel="stylesheet" media="screen and (min-width: 500px)" href="over500px.css">
```
- embed with @media tag
  - few big http requests
```
@media screen and (min-width: 500px) {
  body { background-color: green; }
}
```
- embed with @import tag
  - avoid, big hit on performance
```
@import url("no.css") only screen and (min-width: 500px);
```

- - -
Next up: [Next Step Media Queries](ND024_Part2_Lesson03_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
