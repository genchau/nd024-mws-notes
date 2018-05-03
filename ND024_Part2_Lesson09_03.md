# Lesson 9.3 Sizes Attribute

The w unit tells the browser the dimensions of the image files.

The browser parses the HTML and starts image pre loading before the CSS is parsed. That's why the sizes attribute is so important. It'll determine then before parsing CSS which image file to download. 

`sizes="(max-width: 250px) 100vw, 50vw"` This simply tells the browser how the image will be displayed but it will not cause the image to be resized. That's still done in CSS.

```
<style>
  img {
    transition: width 0.5s;
    width: 50vw;
  }
  @media screen and (max-width: 250px) {
    img {
      width: 100vw;
    }
  }
</style>

<img src="small.jpg" srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 1500w" 
sizes="(max-width: 250px) 100vw, 50vw" alt="Wallaby" />
```

In console run this to find the current source of the image:
`$0.currentSrc`


- - -
Next up: [Quiz: srcset Quiz](ND024_Part2_Lesson09_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
