# Lesson 14.4 Quiz: Automatically Reload the index.html

Make index.html automatically reload.

Write the code needed for browser-sync to listen to changes in index.html.

Setup another gulp.watch, but this time it isn't watching the original index.html, but the copied one. And everytime that the copy operation is done, we can now execute browserSync.reload to reload the whole page. 
```
gulp.watch('./dist/index.html')
  .on('change', browserSync.reload)
```

- - -
Next up: [CSS Concatenation](ND024_Part3_Lesson14_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
