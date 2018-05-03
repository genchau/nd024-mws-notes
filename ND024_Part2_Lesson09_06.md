# Lesson 9.6 The Picture Element

With the picture element, the browswer will pick the first source it can work with, if not it'll work down the list.
```
  <picture>
    <source srcset="kittens.webp" type="image/webp">
    <source srcset="kittens.jpg" type="image/jpeg">
    <img src="kittens.jpg" alt="Two grey tabby kittens">
  </picture>
  ```
  
  webp provides better compression, smaller files vs jpeg.
  
  For browser that don't support <picture> it'll simply fallback on <img>. The <img> element is not optional inside the <picture>.

- - -
Next up: [The Full Monty](ND024_Part2_Lesson09_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
