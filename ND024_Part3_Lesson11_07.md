# Lesson 11.7 Grunt Tasks vs Gulp Streams

Before we move on and create more complex tasks, let's talk about the concept of streams in Gulp. Other built systems, like Grunt, have tabbed their copier files to a temporary place where they make some change on them. As a result, every task incurs a penalty for I/O in file system operations. Gulp on the other hand, converts your input files into an in memory strea. So the I/O is only done initially, and at the veny end of all tasks. This is what gives Gulp such a great speed increase in many situations.

- - -
Next up: [Making CSS Suck Less](ND024_Part3_Lesson11_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
