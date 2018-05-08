# Lesson 16.3 The Benefits of Offline First

So how can we deal with these kind of failures and delays? 

We could attempt a network fetch and if that fails, get fallback content from some kind of cache, perhaps the last content we were able to get from the network. However, we have to wait for the network to fail before showing fall back content. And if the connection is slow, users still get nothing, that rage inducing lie-fi experience.

The **Gold standard** is to build offline first.

Offline first means getting as many things on the screen as possible, using stuff already on the user's device in caches and such. We might still go to the network, but we're not going to wait for it. We'll get stuff from a cache as much as we can and then update the page if we finally get content from the network. When we get that fresh data from the network, we can update what the user is looking at and also save that new data into the cache for next time. If we can't get fresh data from the network, we stick with what we've got. Maybe it's out of date stale data, maybe it isn't. Without the network, we might not know but one thing's certain, it's way better than nothing. Taking an offline first approach means the user is happy online, happy offline, and even happy with lie-fi. The less the user has to care about connectivity, the better. 

This course covers exactly how we achieve that. 

- - -
Next up: [Quiz: What Can Slow Us Down](ND024_Part2_Lesson16_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
