# Lesson 9.12 Quiz: Rendering Quiz

Here's a scenario for you to consider. The flex box is a very useful tool for responsive design. It's a CSS display property that resizes elements, and reflows them on the page. For instance, imagine you've got these three elements on a page and then the user resizes the screen to become larger. As a result, the elements themselves become larger. In this scenario, which of the following processes does the browser perform to render the new page? Does the browser perform style, layout, paint, or composite? Check all that apply.

I'll start with style. There are no style calculations here, because the element styles are already known. So, on the screen resize event, the styles are actually applied through layout. And as you just learned, if the browser runs layout, it also has to paint the elements in their new positions on the page, and then composite them together. There are actually exceptions to the lack of style here, however. If there was a resize handler that changed the style, or if a media query break point was hit, then the browser would actually have to recalculate styles. But that's not happening here, so don't check that box.

[Introducing 'layout boundaries' | Wilson Page](http://wilsonpage.co.uk/introducing-layout-boundaries/)

- - -
Next up: [Quiz: CSS Research](ND024_Part4_Lesson09_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
