# Lesson 10.9 Quiz: Interactions and Animations

During the response section of rails. You saw that you have about milliseconds to respond to user input. But, some user interactions also require animations which then need to run at frames per second. What kind of interactions do you think require frames per second animations? Should spinners always be running at frames per second? What about scrolling? Dragging and dropping. Pinching. Pulling to refresh. Menus sliding out from the side. Comment section opening from below. Changing the state of items and forms. Or last but not least, changing the themes of an app. Check all that apply.

As it turns out, anything that involves movement or finger on screen interactions will need to run at frames per second. The only two items that don't fall into those categories are toggling form controls and app theme changes. For these two, you still have milliseconds to respond, but afterwards, the app must continue running at frames per second if it's going to keep feeling responsive.

- - -
Next up: [RAIL Thresholds Review](ND024_Part4_Lesson10_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
