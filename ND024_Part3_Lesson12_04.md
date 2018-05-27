# Lesson 12.4 Using Browser-Sync

1. Install browser-sync. 
```
npm install -g browser-sync
```
2. Create a browser-sync object and initialize the server.
```
var browserSync = require('browser-sync').create();
 browserSync.init({
     server: "./"
 });
 browserSync.stream();
```
3. Run gulp in Terminal, see how browser opens with the page open.

- - -
Next up: [Lesson Outro](ND024_Part3_Lesson12_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
