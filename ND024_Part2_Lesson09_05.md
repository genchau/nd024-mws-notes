# Lesson 9.5 Quiz: srcset and sizes

Example code with srcset and sizes syntax:
```
<img  src="images/great_pic_800.jpg"
      sizes="(max-width: 400px) 100vw, (min-width: 401px) 50vw"
      srcset="images/great_pic_400.jpg 400w, images/great_pic_800.jpg 800w"
      alt="great picture">
```
#### Quiz:
[Link to quiz](http://udacity.github.io/responsive-images/examples/srcsetAndSizes/index-quiz2.html).

Use srcset and sizes to help the browser decide which image to display when the image is displayed at less than the full viewport width. You should make your changes to the site linked in the instructor notes.

<details>
<summary>Solution:</summary>
<p>

```
<img class="w" src="images/Coffee_1280w.jpg" 
sizes="(max-width: 960px) 50vw, 100vw" 
srcset="images/Coffee_1280w.jpg 1280w, images/Coffee_640w.jpg 640w" 
alt="Coffee by Amy March from Turkey">
```

</p>
</details>

- - -
Next up: [The Picture Element](ND024_Part2_Lesson09_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
