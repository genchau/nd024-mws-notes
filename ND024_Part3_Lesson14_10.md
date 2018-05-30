# Lesson 14.10 Writing Future Proof JavaScript

There's another very worthwhile optimization we can do to our JavaScript, and it's quite similar to how we use SASS instead of CSS. Turns our there is a way of running the very latest spec of JavaScript, ECMAScript 6, even though there's no native browser support for many of the features. All we need is a transpiler, which takes one programming language, and converts it into another. Sometimes transpilers stay very close to ECMAScript syntax, adding in a few features here and there. In other cases, they are full implementations of languages we don't typically find in purely front end web development. We'll stick to the former category. Our transpiler of choice is Babel JS. It's very popular, feature rich and well supported by the community. Now of course this step is purely optional. If we're happy with today's JavaScript and don't need all the fanciness, great. But if we're curious to try out arrow functions, generators, and classes, now is the perfect time. And sure enough, getting this into our code is as simple as everything else. Just grab the gulp-babel plugin and require it in our gulpfile. And in both script task, pipe it after the gulp.src, but before the concatenation. We won't see any difference right away, as we're not actually using any ES6 magic in our current code. So head over to Babel's ES6 learning page and get familiar with some of the concepts.

```
var babel = require('gulp-babel');

gulp.task('scripts', function() {
	gulp.src('js/**/*.js')
		.pipe(babel())
		.pipe(concat('all.js'))
		.pipe(gulp.dest('dist/js'));
});

gulp.task('scripts-dist', function() {
	gulp.src('js/**/*.js')
		.pipe(babel())
		.pipe(concat('all.js'))
		.pipe(uglify())
		.pipe(gulp.dest('dist/js'));
});
```

- - -
Next up: [Quiz: Why Transpile](ND024_Part3_Lesson14_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
