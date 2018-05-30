# Lesson 14.5 CSS Concatenation

The first optimizations we do are easy to implement and make our code load faster. We first glue our CSS and JavaScript files together through concatenation, then crunch them with a minifile. In previous lessons, we applied a couple tasks to our CSS. But this time it's mostly about JavaScript. I say mostly because thse topics still apply to CSS. It's simply that we're already mostly covered. Sass does both concatenation  and minification for us. Manual concatenation isn't necessary, because we can simply include a single sass file in our html. Then use the import directive in our sass to input other files into our base file. When the sass compiler processes the sass into CSS, it will automatically inline those inputs and generate one big CSS file. A minification is just an optional way. Just modify the sass pipe slightly and add outputStyle: 'compressed' as config which will produce a nicely compressed file.

- - -
Next up: [JS Concatenation](ND024_Part3_Lesson14_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
