# Lesson 4.6 Quiz: Combining Fluid Layouts

Play with this quiz on [codepen.io](https://codepen.io/genchau/pen/Qrveba)

##### Solution:
```
.container {
  display: flex;
  flex-wrap: wrap;
}

.box {
  width: 100%;
}

@media screen and (min-width: 450px) {
  .light_blue, .green {
    width: 50%;
  }
}

@media screen and (min-width: 550px) {
  .red {
    width: 33.333%;
  }
  .orange {
    width: 66.666%;
  }
}

@media screen and (min-width: 800px) {
  .container {
    width: 800px;
    margin-left: auto;
    margin-right: auto;
  }
}
```

- - -
Next up: [Pattern - Layout Shifter](ND024_Part2_Lesson04_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
