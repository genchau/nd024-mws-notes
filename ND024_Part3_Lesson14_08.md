# Lesson 14.8 Minification

After concatenation, it's now time for minification to shrink the file size of our JavaScript. The most popular minifier today is which does some heavy but safe optimizations to squeeze every last bit out of our raw source code. And we might have guessed it, plug-in and include it into the gulp-file. Now this is where our scripts and scripts-dist tasks are starting to become slightly different. As JavaScript minification is a very time-intensive stop. Therefore, it makes no sense to do this while live-editing our code. Add the missing pipe to the scripts-dist task right after the concat pipe and call it pipe uglify. Yes, that's all we need and calling this task now will produce nicely concatenated and minified JavaScript.

```
gulp.task('scripts-dist', function() {
	gulp.src('js/**/*.js')
		.pipe(concat('all.js'))
		.pipe(uglify())
		.pipe(gulp.dest('dist/js'));
});
```

- - -
Next up: [Setting up a production task](ND024_Part3_Lesson14_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
