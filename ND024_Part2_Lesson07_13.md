# Lesson 7.13 Quiz: Spot the Diffrences

#### Quiz:
[Link to quiz](http://udacity.github.io/responsive-images/examples/1-17/sameImage/index.html)

Use DevTools to inspect the two images in the linked page. What's different between them? Select all the difference that you can find.

- [ ] Compression Level
- [ ] Display Size
- [ ] Actual (Natural) Size
- [ ] Type

<details>
<summary>Solution:</summary>
<p>

- [ ] Compression Level
- [ ] Display Size
- [X] Actual (Natural) Size
- [ ] Type

```
Both image looks almost identical when presented. 
Yet one image is almost twice the size in bytes. We can consider this wasted bytes.
Remember sometimes phones are on limited bandwidth.
Which can mean long wait times for images to download.
```

</p>
</details>
<br>
<br>

Tip: Remember to check size of elements in Network tab. And use $0 to query details on the selected element in Elements tab. Such as `$0.naturalWidth`.

Note: Some of the sublessons were removed from this main lesson. 
- Compression, Optimization and Automation (#19 in subtitles)
- Image Optimization Environment (#20 in subtitles)
- These covered batch image processing.
- Using tools like ImageMagick, Grunt, ImageOptim, Pngout, pngcrush, jpegoptim, Giftical, ImageAlpha, pngquant.
- Grunt allows us to incorporate automated image optimization in our work flow.
- Recommended Image Optimization Environment: Grunt, ImageOptim, ImageMagick.

- - -
Next up: [Quiz: Spot the Differences 2](ND024_Part2_Lesson07_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
