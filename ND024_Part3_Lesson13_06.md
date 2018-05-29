# Lesson 13.6 Setting up ESLint in Gulp

If we're collaborating or working on another computer, the other party might not have the linter configured. Since our colleague needs to run the build to work with the site anyway, why not have the build run the linter, and complain when something goes wrong? Install the gulp-eslint package and require it in the head of your gulp file. Turns out the basic example on the gulp-eslint readme works well for us. So we're just going to copy it and paste it into my gulp file. As we'll notie, this task looks very familiar. It has the gulp source code, but this time fetches js files, then uses pipes to do a few things with eslint. The first pipe executes eslint and all files matched. The second line outputs the errors to the console, so we actually see what happened. And the third pipe ensures that gulp exits with an error code and fails. Without that line, gulp would show the errors but would proceed with everything else. Now we could execute the task manually. But let's integrate it into our default task. First, add it to the second argument area after styles. So it runs right after running Gulp in the terminal. Then add a new line after gulp.watch to add a new Gulp watch. This time watching the js files and calling lint, instead of styles. The best thing is wthat we can later reuse this new watcher to do even more great things to our js. And there we go. Try resetting Gulp in the terminal and makes some changes through our JS to see linting appear on our terminal after every save. To wrap things up, there's a third almost desperate way of forcing ESLint up on our project collaborators. With a pre-commit hook, we can let everyone go crazy on our own file systems. But as soon as they want to commit a change to the shared git repository, ESLint will run error out and not let a commit through. In order to learn more about pre-commit hooks, we should check out the source control Udacity course.

Install `npm install gulp-eslint`

Update gulpfile.js:
```
/*eslint-env node */

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();
var eslint = require('gulp-eslint');

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
	return gulp.src(['**/*.js','!node_modules/**'])
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
Run gulp on terminal and see it work.

Further learning: Learn about commit hooks. 
[Git Hooks | Learn how to use pre-commit hooks, post-commit hooks, post-receive hooks, and more. | Matthew Hudson](https://githooks.com/)

- - -
Next up: [Unit Testing in Gulp](ND024_Part3_Lesson13_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
