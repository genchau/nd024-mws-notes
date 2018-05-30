# Lesson 14.7 JS Concatenation Hands On

We create a scripts task. However, since we want to do slightly different things in development and prouction mode. We add another task called scripts-dist, which will be used when we want to distribute our fights for production. In the first step, both of these tasks will look the same. We gulp source the files we need, in this case, our JavaScript files. Then pipe them to the correct destination, in our case, the dist/js folder. Now install the gulp-concat plug-in via npm, and require in the gulpfile, then add a new pipe to both tasks with concat all JS before the destination pipe. This plugin takes the files in the stream, and combines them into a single file named whatever we provide as the argument. Try running one of those task in our terminal, to make sure the concatenated all.js ends up in the correct folder. All good. Then we're missing only one last thing. We need to change the references to the individual js files in our index html to point to the single js file, at js/all.js. And now our page should run fine again.

```
npm install gulp-concat
```

```
var concat = require('gulp-concat');

gulp.task('scripts', function() {
	gulp.src('js/**/*.js')
		.pipe(concat('all.js'))
		.pipe(gulp.dest('dist/js'));
});

gulp.task('scripts-dist', function() {
	gulp.src('js/**/*.js')
		.pipe(concat('all.js'))
		.pipe(gulp.dest('dist/js'));
});
```

- - -
Next up: [Minification](ND024_Part3_Lesson14_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
