# Lesson 10.3 Load and Idle

So the first we're going to look at is Load. Whatever it is, users want it to load quickly, and it's super important that we optimize for the critical rendering path. Earlier in Cam's course, and this is the fourth plug I've given it now, oh I should be on some kind of commission, seriously. Anyway it's linked in the instructor notes and it will take you through the fine details of that. I took you through a quick tour of the rendering process in the first lesson, but essentially you want your initial load to be done in one second. 

Okay, I'm going to switch across to Chrome, and I'm going to load Google Play Music, and I suspect it'll load in about one second. There we go. Now after an app's loaded, it's normally idle, it's waiting for a user to interact. And this is our opportunity to deal with things that we **deferred** to meet that one second load time. Normally, these idle blocks are around milliseconds long, although you may several of them in one go. These idle blocks are fantastic times to get some heavy lifting done so that when the user interacts things are nice and snappy. I'll stop for a second and let you think through the best way to approach an app's idle time.

- - -
Next up: [Quiz: Idle Time](ND024_Part4_Lesson10_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
