# Lesson 10.8 Quiz: Rendering Animations

Paul just explained how he used Flip to create a pretty snazzy animation. He performed all the hard calculations up front, so that he would touch as little of the pipeline as possible during the actual animation. This is how he kept it going at a silky smooth frames per second. When he applied opacity and transform changes to reverse the animation, what steps in the rendering pipeline did Paul trigger? Did the HTML need to get converted to the DOM? Did the CSS need to get converted to the CSSOM? Did the DOM and CSSOM need to be combined into the Render Tree? Did the browser have to run Layout again, Composite again, or Paint again? Check all that apply.

As you just discovered, changes to opacity and transform only trigger composite when the elements are on their own layers. But remember, Paul also had to use clip to reverse the animation. And that, unfortunately, requires paint. It's important to always understand the implications of any property you choose to animate, because some are definitely cheaper than others.

- - -
Next up: [Quiz: Interactions and Animations](ND024_Part4_Lesson10_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
