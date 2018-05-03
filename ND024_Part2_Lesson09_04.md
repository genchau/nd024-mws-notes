# Lesson 9.4 Quiz: srcset Quiz



Syntax:
Use the identifier `x` to identify DPR. Example:
`<img src="image_2x.jpg" srcset="image_2x.jpg 2x, image_1x.jpg 1x" alt="a cool image">`

Use the identifier `w` to identify width. Example:
`<img src="image_200.jpg" srcset="image_200.jpg 200w, image_100.jpg 100w" alt="a cool image">`

#### Quiz:

Use srcset to help the browser decide which image to display depending on the browser's width and display density. You should make your changes to the site linked in the instructor notes.

[Link to quiz](http://udacity.github.io/responsive-images/examples/srcsetAndSizes/index-quiz1.html).

<details>
<summary>Solution:</summary>
<p>

```
<img class="dpi" src="images/Den_Haag_2x.jpg" 
srcset="images/Den_Haag_1x.jpg 1x, 
images/Den_Haag_2x.jpg 2x" alt=" den=" haag="">

<img class="w" src="images/Australia_1280w.jpg" 
srcset="images/Australia_1280w.jpg 1280w, 
images/Australia_640w.jpg 640w" alt="Australia from Space">
```

</p>
</details>

- - -
Next up: [Quiz: srcset and sizes](ND024_Part2_Lesson09_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
