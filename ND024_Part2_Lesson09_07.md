# Lesson 9.7 The Full Monty

*Nice!* I love how this website responds: [Cute cat art direction.](http://udacity.github.io/responsive-images/examples/3-08/pictureArtDirection/)

Art direction: Choosing images to suit the viewing context.

The full monty:
- Combined media queries and source set
- To specify images for smaller and larger viewports
- with different images for different pixel densities.

Example code:
```
<picture>
  <source
    media="(min-width: 1000px)"
    srcset="kookaburra_large_1x.jpg 1x, kookaburra_large_2x.jpg 2x">
  <source
    media="(min-width: 500px)"
    srcset="kookaburra_medium_1x.jpg 1x, kookaburra_medium_2x.jpg 2x">
  <img src="kookaburra_small.jpg"
    alt="The kookaburra: a terrestrial tree kingfisher native to Australia and New Guinea">
</picture>
```

- - -
Next up: [Accessibility](ND024_Part2_Lesson09_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
