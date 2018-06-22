# Lesson 9.8 Quiz: Render Tree Quiz

Knowing that only visible elements are in the Render Tree, which of the following elements would not be inside the Render Tree? Would .style with display none not be in the Render Tree? Would .style with the before selector and display block not be in the Render Tree? Would .style with height of zero not being in the Render Tree, or would .style with position absolute in left, %, meaning it's pushed all the way off the right side of the page, not be in the Render Tree? Pick one of these four answers.

Right! Elements that are display: none don't show up in the Render Tree.

And the correct answer is any element with a class of style none. If an element is set to display none that means that the element is not going to be rendered whatsoever. For the other three options, though they may not take up any space on the page that you're seeing they're still a part of the page. Which means that the browser will still put style three, style four, and style two before on the render tree.

- - -
Next up: [DOM, CSSOM, Render Tree](ND024_Part4_Lesson09_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
