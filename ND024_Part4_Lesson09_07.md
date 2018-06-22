# Lesson 9.7 What Goes Into One Frame

You can't optimize your app's frame rate if you don't understand how the browser actually renders a frame. So you need to learn how a page is actually put together when it's first loaded. I'll go over the process briefly right now, but if you want a more in-depth look at how the page is built I highly recommend checking out the link to Cam's and Ilia's website performance optimization course in the instructor notes. Cam already mentioned it, but it's a super good course. Although, don't go just yet, right? Just stay here and, you know, I'd miss you if you went. Check it out later. Okay, so let's take a look at what goes into making a frame. Initially the browser makes a get request to a server. The server responds by sending some HTML. At this point, the browser does some pretty clever stuff with lookahead parsing. But what we care about is that it parses the document and gives us these notes. 

In Chrome DevTools, you'll see it as Parse HTML. Okay, so this is what the DOM looks like as a tree. But let's just make it a bit easier for ourselves, and call it the DOM. As well as the DOM, we also have CSS. And this comes from the user agent, it comes from your style sheets or any inline styles you have, and perhaps third party styles. The next part of the process is to combine the DOM and CSS. 

In the tools you're going to see this as Recalculate Styles. And when combined, we get a new tree called the Render Tree. 

The Render Tree looks pretty similar to the DOM, except that some things are missing. For example, we don't have the head anymore, we don't have any scripts. In fact, if we had some CSS that set the section paragraph to display none, then it would be removed from the render tree. Equally if we had some CSS that added a pseudo element like after or before, this would get added to the render tree even though it doesn't live in the DOM. It's important to note that only elements that will actually be displayed on the page will make it into the render tree. So this is essentially a simplified view of where the critical rendering path optimization gets you.

- - -
Next up: [Quiz: Render Tree Quiz](ND024_Part4_Lesson09_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
