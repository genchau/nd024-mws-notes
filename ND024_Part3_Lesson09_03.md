# Lesson 9.3 Common Sense

Not all tools are created equal, and not all optimizations are worth doing.

1. I can build a better tool from scratch!
    - Web dev example, hundreds of engineering years went into tiny js libraries like jQuery. Yet, countless developers have tried to replicate it with a 90% similar feature set, only to fail hard, again and again. Even popular clones like Zepto, couldn't keep up when they realized that jQuery fixed a lot more cross-browser maintenance than people thought. 

2. This 2 week old build tool built by this random dude is 20% faster than Gulp! Get it in there!
    - Now we're talking idealistic versus pragmatic. Yes, that 20% increase will be ideal. But sticking to a tool that is well supported by the community, is pragmatic. Gulp might be a little slower than someone else's new tool But we'll find answers for our questions on stack overflow, plugins for virtually anything and can rest assured, that the tool is going to be maintained by its creators. Consider the long-term value for our project.

3. This tool is self contained and does everything we want right now.
    - Contained, all in one package? Be careful with these. If a tool promises to do it all, and stays away from offering any sort of connection points, say in API or modules, run. Life is too short to buy into an ecosystem that we can't escape from, especially if the success of our site depends on it.

4. If the user triggers the Konami code, it could theoretically result in app failure.
    - We should be careful with any micro optimizations that are just not worth it. If we are doing an optimization of our work floor that takes, say four hours, and cuts a second away from a task we perform once during the day, we need to do it for 40 years to justify the investment. And in 40 years, we could be sitting in an intergalactic flying car, exploring the outer realms of space instead. 

- - -
Next up: [On to the course!](ND024_Part3_Lesson09_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
