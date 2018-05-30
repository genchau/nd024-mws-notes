# Lesson 14.3 Development and Production Modes Part 2

Generated files (separated from source files):
- dist/
    - css/ (generated from sass)
    - js/ (combined JavaScript file)
    - img
    - index.html (copy)

In our gulpfile.js we are simply changing the dest:
`.pipe(gulp.dest('dist/css'))`

We also want to setup gulp.watch for index.html.

Sample gulpfile.js snippets:
```
gulp.task('default', ['copy-html', 'copy-images', 'styles', 'lint', 'scripts'], function() {
	gulp.watch('sass/**/*.scss', ['styles']);
	gulp.watch('js/**/*.js', ['lint']);
	gulp.watch('/index.html', ['copy-html']);
	gulp.watch('./dist/index.html').on('change', browserSync.reload);

	browserSync.init({
		server: './dist'
	});
});
. . .
gulp.task('copy-html', function() {
	gulp.src('./index.html')
		.pipe(gulp.dest('./dist'));
});

gulp.task('copy-images', function() {
	gulp.src('img/*')
		.pipe(gulp.dest('dist/img'));
});
```

- - -
Next up: [Quiz: Automatically Reload the index.html](ND024_Part3_Lesson14_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
