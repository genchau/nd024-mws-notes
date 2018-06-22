# Lesson 9.13 Quiz: CSS Research

For this quiz, I want you to head over to csstriggers.com and do some research. I want you to find a CSS property that triggers layout, paint, and composite, and type it into this box. Then find a CSS property that only triggers paint and composite and type it into this box. And then lastly, find a CSS property that only triggers composite and type it into this box. The reason you're checking out csstriggers.com is because a, Paul made it and he's forcing us to include it in the course, and b, it's a super useful resource for determining the amount of work your CSS will trigger. It's really important to become familiar with it if you want to write performant websites. Okay. Well, good luck!

This quiz, I picked margin-left for layout, paint, and composite, color for paint and composite, and then transform for just composite. Not all CSS is created equal. Some CSS properties have much wider-reaching consequences than others. Your CSS should trigger the least amount of work possible, and that's going to mean avoiding paint and layout whenever possible. Transforms and opacity are far and away the best properties to change, because they can be handled just by the compositor if the element has its own layer. You'll learn more about how to create and manage layers later in the course.

[CSS Triggers](https://csstriggers.com/)


- - -
Next up: [Final Project](ND024_Part4_Lesson09_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
