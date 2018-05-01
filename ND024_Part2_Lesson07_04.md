# Lesson 7.4 Relative Sizing

CSS sizing.

A standard 640x360 image (set at `width: 640px`):
- Looks good on browswer
- But looks bad on phones with a smaller viewport. We get a cropped image that results in horizontal scrolling. Yuck.

A standard 640x360 image (set at `width: 100%`):
- Looks good on small browswer
- Looks good on phone
- But starts pixelating and getting blurry on large browsers.
- We can fix this by setting `max-width: 100%`

Here's a code snippet of how to place 2 images side by side with both relative and absolute values using calc():
```
img {
  margin-right: 10px;
  max-width: 426px;
  width: calc( (100%-10px) / 2 );
}
img:last-of-type {
  margin-right: 0;
}
```

Do you need placeholder images? Try [http://lorempixel.com/](http://lorempixel.com/).

- - -
Next up: [IMPORTANT! Udacity Front End Feedback Extension](ND024_Part2_Lesson07_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
