# Lesson 11.12 Quiz: Finding More Jank

[Here's the site for your analysis!](http://jsbin.com/woyoce/1/quiet)

In the instructor notes, you'll find a link to this kind of terrifying website. It may not look like much now but click this animate button and see what happens. So this is a really super janky animation. Even on my new MacBook Pro, this thing is barely chugging along. What I want you to do is record a timeline trace of what happens when you click the Animate button. When you've got the timeline try using both views. Like the waterfall view and the flame view. Play with both of them and see which works better for you as you're analyzing the website. Just like before, I want you to find where the ridiculous Jank in the timeline is coming from. So what is causing it? Is that there is too much JavaScript running? Is it because there is simply too much painting happening and the painting is being caused by a CSS animation? Is it because of compositing? Is it because there's too much painting which is being caused by JavaScript? Or is it happening because recalculate styles is taking way too long and it's being caused by JavaScript? Pick one of these answers.

I'm seeing a lot of green in the timeline, which is a pretty good indication that there's a Paint problem. I'll go ahead and zoom into one of these frames. It looks like each frame is starting with the script. There's an Animation Frame Fired followed immediately by style calculations and then a Paint. This looks like a JavaScript problem because if the problem was coming from CSS, then chances are I wouldn't be seeing an animation frame being fired. So in the end it's pretty clear that there is a paint problem and it's being caused by JavaScript.

- - -
Next up: [Lesson 3 Outro](ND024_Part4_Lesson11_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
