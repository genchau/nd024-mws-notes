# Lesson 4.3 Pattern - Mostly Fluid

Mostly fluid is when elements move around the layout as the screen viewport changes.

Example of mostly fluid pattern:
```
@media screen and (min-width: 450px) {
  .light_blue, .green {
    width: 50%;
  }
}

@media screen and (min-width: 550px) {
  .dark_blue, .light_blue {
    width: 50%;
  }
  .green, .red, .orange {
    width: 33.3333333%;
  }
}

@media screen and (min-width: 700px) {
  .container {
    width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
}
```

This looked really similar to column drop, with the exception that we are manually defining the width % of certain elements at each viewport setting, so that the layout is slightly different.

- - -
Next up: [Quiz: Mostly Fluid Part 1](ND024_Part2_Lesson04_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
