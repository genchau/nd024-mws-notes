# Lesson 2.11 Performance Details

But even then we have to fight the sheer nature of the web and network architecture. In this example, over 50 percent of the time from pressing enter in the address bar to the page being displayed is spent waiting for the answer. This waiting period is called **Time to First Byte or TTFB**. If this website needed to grab additional resources, we would have to wait for the response of our first request before we could send out a second request. That in turn means that we have another period of time waiting that is not being used effectively. This problem is called Head of Line Blocking. Let's see an example of what Head of Line Blocking is and how it is bad for the user experience. With HTTP, a connection is like a queue. While the first request is being handled, all other requests have to wait until it is their turn. A lot of time is being wasted here. 

Coffee scene:
While Richard's drink is being prepared, the other customers are left waiting. Even though their request would be much faster to make, the head of line is blocking the rest of the customers. To counteract this limitation a little bit, browsers open up to 6 parallel connections, or in our coffee shop comparison, they hire another barista.

So while the first connection is waiting for its first byte, a second request can already be sent on the second connection, and so on. Of course, hiring a new barista takes off time and training. In the browser, opening all these connections is also quite costly because of the TCP handshakes necessary. The 6 parallel connections browsers can make is still only a band aid for the head of line blocking. If you have a lot of resources on our page, we will spend most of our time waiting or staring at the cashier. Head of line blocking is a huge bottleneck to website performance. Browsers being able to open up 6 parallel connections help, but it's not great. Later, we will see how HTTP 2 fix this issues with head of line blocking.

- - -
Next up: [Performance Details 2](ND024_Part4_Lesson02_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
