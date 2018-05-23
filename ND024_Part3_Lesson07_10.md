# Lesson 7.10 Transpiling

A compiler is a computer program that takes a program written in some source code language, let's say C++, and then converts it to a target language like machine code. Running code through a compiler changes its level of abstraction, how close it is to human readable code to machine runnable code. So that's compiling, taking a source language and converting it into a lower level language. 

Transpiling is a subset of compiling. So, it takes source code and converts it into target code. Just like a compiler but the source code and target code are at the same level of abstraction. Basically, if the source code starts out as human readable then the output language will also be human readable. 

But why would we want this? Well, we just saw that older browsers do not fully support ES6 but they do support ES5 code. This way we could write our JavaScript using ES6, syntax and functionality and then use a transpiler to convert it from ES6 code to ES5. So, we'll write code using the newest and best but convert it so that it will run everywhere.

To convert Java to JavaScript, would you use a compiler or a transpiler?
a transpiler

- - -
Next up: [Using Babel](ND024_Part3_Lesson07_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
