# Lesson 15.3 Quiz: Write your own focus styles

#### Quiz:
folder: `lesson6-styling/01-focus-styles` 

Objective: 

The buttons on this page don’t currently have focus styles, making them pretty much useless to a keyboard user. With your new CSS knowledge, try using the :focus pseudo-class to give these buttons interesting focus states.

#### Solution:

First we find all the anchor and button tags from the page.
Then add some styling to the bottom of the css file.
```
.nav > li > a:hover,
.nav > li > a:focus,
.jumbotron .mdl-button:hover,
.jumbotron .mdl-button:focus,
.mdl-button.raised:hover,
.mdl-button.raised:focus {
  //white text on red background
  background: #C2185B;
  color: #FFFFFF;
  text-decoration: underline;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14),
              0 3px 1px -2px rgba(0, 0, 0, .2),
              0 1px 5px 0 rgba(0, 0, 0, .12);
}

```

- - -
Next up: [Input Modality](ND024_Part2_Lesson15_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
