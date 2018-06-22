# Lesson 9.6 Quiz: Milliseconds Per Frame

In order to avoid jank, you need to carefully budget the task that your app performs. Each frame needs to render quickly, but just how quickly, exactly? In order to render frames every , ms, how much time do you have to render a single frame? Type your answer into this box.

16ms

I'll take milliseconds and divide it by frames per milliseconds and I'll get about milliseconds per frame. This means that in order to achieve a silky smooth frames per second, you need to keep all of the work in making the frame under milliseconds. But actually, the browser also has some housekeeping work to do in every frame. So realistically, you have somewhere in the region of 12 milliseconds to get everything done and make sure the frame arrives on time.

- - -
Next up: [What Goes Into One Frame](ND024_Part4_Lesson09_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
