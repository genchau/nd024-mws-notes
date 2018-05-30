# Lesson 14.9 Setting up a production task

To produce a production ready version of our site, we can skip the whole live editing and watching, and include the scripts distribution task instead. Nothing easier than that. Let's call the new task dist and include the following tasks in that order. Copy html. Copy images. Styles. Lint. And finally scripts-dist. Try running the tasks via gulp scripts-dist. If gulp takes slightly longer, and exists without opening the browser, we're all set, and have a production ready distribution in our dist folder. Before we continue, one word of advice regarding minification. Minification on its own is great, but GZIP is even more affective. GZIP compresses the file before it gets in, and out to the browser, and the browser deflates it. All of this happens transparently in the background and usually only requires a small server configuration change. Read more about GZIPing in the notes.

```
gulp.task('dist', [
  'copy-html',
  'copy-images',
  'styles',
  'lint',
  'scripts-dist',
]);
```

[The Difference Between Minification and Gzipping | CSS-Tricks](https://css-tricks.com/the-difference-between-minification-and-gzipping/)

- - -
Next up: [Writing Future Proof JavaScript](ND024_Part3_Lesson14_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
