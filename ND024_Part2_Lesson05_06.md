# Lesson 5.6 Responsive Tables - No More Tables

*No More Tables Technique* - below a certain viewport the table is collapsed and resembles a long list. The nice thing is that all the data is still visible. 

Example code:
```
@media screen and (max-width: 500px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }
  thead tr {
    position: absolute;
    top: -9999px;
    left: -9999px;
  }
  td {
    position: relative;
    padding-left: 50%;
  }
  td:before {
    position: absolute;
    left: 6px;
    content: attr(data-th);
    font-weight: bold;
  }
}
```

`display: block` turns every table element into its own block.
`thead tr { ... top: -9999px; ... }` moves the header away instead of display none for accessibility reasons.
`td { position: relative; padding-left: 50%; }` formats the block elements.
`td:before` modifies each td tags. 
`content: attr(data-th);` pulls this data from the th tag.

- - -
Next up: [Responsive Tables - Contained Scrolling](ND024_Part2_Lesson05_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
