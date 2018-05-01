# Lesson 7.6 Quiz: calc()

##### Quiz:

[Link to quiz](http://udacity.github.io/responsive-images/examples/1-08/imageRelativeWidth/index-quiz.html)

Objective:
- Fit 3 images horizontally.
- 10px margin in between images
- Use `calc()`

Procedure:
- Open the webpage
- Open Chrome DevTools
- Click on Elements tab
- Open `<head>` tag
- Open `<style>` tag
- Add your CSS code to fulfill the objectives

<details>
<summary>Solution</summary>
<p>

```
    body {
      margin: 0;
    }
    img {
      float: left;
      margin-right: 10px;
      width: calc( ( 100% - 20px ) / 3 );
    }
    img:last-of-type {
      margin-right: 0;
    }
```

</p>
</details>



- - -
Next up: [Landscape and Portrait](ND024_Part2_Lesson07_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
