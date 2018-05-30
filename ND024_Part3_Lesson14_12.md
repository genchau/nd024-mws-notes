# Lesson 14.12 Source Maps

### JavaScript Source Maps
Imagine you’re running your page now and there’s a bug in your JavaScript. so you head over to the Sources panel to set a breakpoint, only to realize you’re looking at Spaghetti instead of source code.

After all the optimizations, none of your code is particularly readable anymore.

That's a major rationale for source maps.

Source maps are files that associate line numbers from the processed file to the original. This way the browser can lookup the current line number in the sourcemap and open the right source file at the correct line when debugging. In Chrome for instance, the DevTools support source maps both for CSS and JavaScript.

You can read a bit more about the source map specification [here](https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit).

### Setup
Source maps in gulp are easy to setup. It’s a use case where pipes really shine.

1. Install the gulp-sourcemaps [plugin](https://www.npmjs.com/package/gulp-sourcemaps).
2. Require the gulp-sourcemaps plugin and in your scripts-dist or scripts (or styles) task, add a pipe to sourcemaps.init() after you get the source but before you send the source files through any pipes that transform them materially. After all plugins and pipes have been applied but before you save to the destination, pipe through sourcemaps.write() with an optional location parameter if you don't want the source maps to be inlined.
```
var sourcemaps = require('gulp-sourcemaps');

 gulp.task('scripts-dist', function() {
   gulp.src('js/**/*.js')
    .pipe(sourcemaps.init())
    .pipe(concat('all.js'))
    .pipe(uglify())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('dist/js'));
});
```

All of the pipes between init and write must have support. Check the list [here](https://github.com/floridoo/gulp-sourcemaps/wiki/Plugins-with-gulp-sourcemaps-support) to verify. In the developer console, the output of app should automically link errors in the generated code to their line numbers in the original source.

### Source map Support for other languages
In addition to things like concatenation and minification, source maps also support some languages/extensions that transpile to JavaScript like Typescript, CoffeeScript and ES6 / JSX.

You can read more some of the technical aspects of Source Maps on [HTML5Rocks](http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/).

- - -
Next up: [Image Optimization](ND024_Part3_Lesson14_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
