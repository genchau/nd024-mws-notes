# Lesson 7.1 Quiz: Sizing Intro

By the end of this lesson:
- Learn the workflow to make it easy to optimize our images for low bandwidth but still looking great.
- We'll be thinking about image quality and size.

##### Quiz:
[Link to quiz.](http://udacity.github.io/responsive-images/examples/1-05/identicalImagesDifferentCompressionAndSize/index.html)

##### How are these images different?
Use DevTools to inspect the three images in the site. What's different between them? Select all the differences that you can find.

- [ ] Compression Level
- [ ] Display Resolution
- [ ] Actual (Natural) Resolution
- [ ] File Type

Using DevTools to analyze the image:
- Navigate to Network tab.
- Disable Cache.
- Refresh page to start recording the network traffic.
- Find the 3 horse images.
- We notice that their sizes are different.
- Click on element tab.
- Click on horse1.jpg
- In the console, type `$0` and enter. 
- Now try `$0.naturalWidth` and enter. This will show the width.
- Or we can simple hover over the `<img>` tag in the Elements tab. It will show us the resolution of the image.
- We can now compare resolution, byte sizes to determine how these 3 pictures are different.

<details>
<summary>Solution</summary>
<p>
<ul>
<li>[x] Compression Level</li>
<li>[ ] Display Resolution</li>
<li>[x] Actual (Natural) Resolution</li>
<li>[ ] File Type</li>
</ul>
</p>
</details>

- - -
Next up: [All about Bits and Pixels](ND024_Part2_Lesson07_02.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
