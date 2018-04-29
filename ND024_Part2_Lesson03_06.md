# Lesson 3.6 Quiz: Which styles are applied

##### Quiz:
[Link to the Quiz](http://udacity.github.io/RWDF-samples/quizzes/media-queries-quiz.html)
Objective: 
- Between 0 and 400 pixels, set background color to red.
- Between 401 pixels and 599 pixels set the background to green.
- 600 pixels or wider, set the background color to blue.

##### Solution:
```
@media screen and (min-width: 0px) and (max-width: 400px) {
  body { background-color: red; }
}
@media screen and (min-width: 401px) and (max-width: 599px) {
  body { background-color: green; }
}
@media screen and (min-width: 600px) {
  body { background-color: blue; }
}
```

- - -
Next up: [Breakpoints](ND024_Part2_Lesson03_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
