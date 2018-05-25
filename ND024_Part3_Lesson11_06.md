# Lesson 11.6 Hello Gulp

Every Gulp project starts with a Gulp file. This file sits in the root directory of our project and defines all the task that we should execute when running Gulp. 

Since Gulp is essentially a node JS script, we first require Gulp as a dependency. Then we setup a default task. 

gulpfile.js
```
var gulp = require('gulp');

gulp.task('default', defaultTask);

function defaultTask(done) {
  console.log("Hello Michael Phan");
  done();
}
```

- - -
Next up: [Grunt Tasks vs Gulp Streams](ND024_Part3_Lesson11_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
