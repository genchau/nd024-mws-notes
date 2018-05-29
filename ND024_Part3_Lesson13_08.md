# Lesson 13.8 Unit Testing in Gulp

The key to make Jasmine, the unit test framework used in our sample repo work with our build, is to use a headless browser that we can execut and instruct from the command line because that's what gulp can deal with. Luckily, such a browser exists. It's called PhantomJS, and it's basically a headless version of webkit. And we don't need to know much more about it right now. Just the fact that the gulp-jasmine, phantom plugin uses that to its advantage to actually run our tests in a real browser environment. Install [PhantomJS](http://phantomjs.org/download.html) first using the instructor notes. And then like always, install `npm install gulp-jasmine-phantom` in our project directory. Then update our gulpfile.js.

1. Install [PhantomJS](http://phantomjs.org/download.html)
    - Download from website
    - Unzip to Program Files. And add to PATH variables. [Reference](https://www.joecolantonio.com/2014/10/14/how-to-install-phantomjs/)
2. run `npm install gulp-jasmine-phantom`
3. update gulpfile.js:
```
/*eslint-env node */

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();
var eslint = require('gulp-eslint');
var jasmine = require('gulp-jasmine-phantom');

gulp.task('default', ['styles', 'lint'], function() {
	gulp.watch('sass/**/*.scss', ['styles']);
	gulp.watch('js/**/*.js', ['lint']);

	browserSync.init({
		server: './'
	});
});

gulp.task('lint', () => {
	// ESLint ignores files with "node_modules" paths.
	// So, it's best to have gulp ignore the directory as well.
	// Also, Be sure to return the stream from the task;
	// Otherwise, the task may end before the stream has finished.
	return gulp.src(['js/**/*.js','!node_modules/**'])
		// eslint() attaches the lint output to the "eslint" property
		// of the file object so it can be used by other modules.
		.pipe(eslint())
		// eslint.format() outputs the lint results to the console.
		// Alternatively use eslint.formatEach() (see Docs).
		.pipe(eslint.format())
		// To have the process exit with an error code (1) on
		// lint error, return the stream and pipe to failAfterError last.
		.pipe(eslint.failAfterError());
});

gulp.task('tests', function() {
	gulp.src('tests/spec/extraSpec.js')
		.pipe(jasmine({
			integration: true,
			vendor: 'js/**/*.js'
		}));
});

gulp.task('styles', function() {
	gulp.src('sass/**/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(autoprefixer({
			browsers: ['last 2 versions']
		}))
		.pipe(gulp.dest('./css'))
		.pipe(browserSync.stream());
});
```
Personal note: I get an error running `gulp tests`:
```
events.js:183
      throw er; // Unhandled 'error' event
      ^
Error: ENOENT: Tests contained failures. Check logs for details.
```

- - -
Next up: [What's Next?](ND024_Part3_Lesson13_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
