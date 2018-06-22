# Lesson 10.11 Quiz: RAIL Scenario 1

For this quiz. I want you to pretend that you're developing an app that displays a loading jiff like this one while video resources are being buffered. Do you think it's a good idea to request this jiff just during the animation phase? It's also worth noting that if you're requesting the jiff during the animation phase. You also have to insert it into the page during the animation phase.

The correct answer is either one of these. Realistically, there is no way that GIF is going to show up in less than milliseconds. And the request adds extra overhead, too, in the animation phase, which is not the time to handle it. Have the GIF prepared well in advance before the users actually click on video. It's small, so why not make it a part of the initial app load? Either way, don't request it now.

- - -
Next up: [Quiz: RAIL Scenario 2](ND024_Part4_Lesson10_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
