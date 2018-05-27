# Lesson 11.9 Using Gulp

Both SASS and Auto-prefixer have existing gulp plugins that we can use. So, let's install them as project dependencies.

`npm install gulp-sass` //on project folder

After install change the folder structure. Move css files into sass folder and rename files to scss.

Sample gulpfule.js for sass:
```
var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', function() {
	console.log('hello world!');
});

gulp.task('styles', function() {
	gulp.src('sass/**/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(gulp.dest('./css'));
});
```

- - -
Next up: [Using Gulp 2](ND024_Part3_Lesson11_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
