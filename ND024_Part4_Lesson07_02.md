# Lesson 7.2 What about `.encode()`?

Sometimes in writing code, there are things that we have to do that don't immediately make sense, but when you look closely, they actually turn out to be pretty important. On the last page, I promised you that I'd explain this one-- the .encode() method call that we do when we're writing an HTTP response. Check it out.

### What about .encode()?
In the last exercise you saw this bit of code in the hello server:
```
self.wfile.write("Hello, HTTP!\n".encode())
```
I mentioned that I'd explain the .encode() part later. Well, here goes!

### The short version
An HTTP response could contain any kind of data, not only text. And so the self.wfile.write method in the handler class expects to be given a bytes object — a piece of arbitrary binary data — which it writes over the network in the HTTP response body.

If you want to send a string over the HTTP connection, you have to encode the string into a bytes object. The encode method on strings translates the string into a bytes object, which is suitable for sending over the network. There is, similarly, a decode method for turning bytes objects into strings.

That's all you need to know about text encodings in order to do this course. However, if you want to learn even more, read on ...

### The long version
Text strings look simple, but they are actually kind of complicated underneath. There are a lot of different ways that computers can represent text in memory and on the network.

Older software — including older versions of Python — tended to assume that each character takes up only one byte of memory. That works fine for some human languages, like English and Russian, but it doesn't work at all for other human languages, like Chinese; and it really doesn't work if you want to handle text from multiple languages in the same program.

    These words all mean cat:
    gato قط 猫 گربه кіт बिल्ली ねこ

The Web is international, so browsers and servers need to support all languages. This means that the old one-byte assumption is completely thrown out. But when programs use the network, they need to know how long a piece of data is in terms of bytes. That has to be figured out unambiguously at some point in time. The way Python does this is by making us encode strings into bytes objects when we want to send them over a binary channel (such as an HTTP connection).

This Japanese word for cat is two characters long. But when it's encoded in binary, it's six bytes long:
```
>>> len('ねこ')
2
>>> len('ねこ'.encode())
6
```
The most common encoding these days is called UTF-8. It is supported by all major and minor browsers and operating systems, and it supports characters for almost all the world's languages. In UTF-8, a single character may be represented as anywhere from one to four bytes, depending on language.

English text with no accent marks still takes up one byte per character:
```
>>> len('cat')
3
>>> len('cat'.encode())
3
```
UTF-8 is the default encoding in Python. When you call the encode method on a string without passing it another encoding, it assumes you mean UTF-8. This is the right thing to do, so that's what the code in this course does.

For even more detail ...
The [Python Unicode HOWTO](https://docs.python.org/3.6/howto/unicode.html) is a definitive guide to the history of string encodings in Python.

Okay, now let's get back to writing web servers!

- - -
Next up: [The echo server](ND024_Part4_Lesson07_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
