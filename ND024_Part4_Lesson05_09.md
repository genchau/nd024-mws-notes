# Lesson 5.9 Security Exploit - CSRF

As we just learned, requests had looked just like they came from a form will not be pre-flighted. You can't read the response if CORS doesn't allow it. But sometimes you might not need to see the response to wreak havoc. Imagine a bank that has a form to transfer money. If you are not a good person, all you want to do is wire the money to your own account, you don't care about what the server answers. So you set up a website that forges a request of the same URL the form uses and set the parameters so that the money is wired to you and the user won't even notice. That's why this kind of attack is called cross-sites request forgery or CSRF.

<img src="https://d3eaqdewfg2crq.cloudfront.net/wp-content/uploads/2013/04/csrf.png">

Of course, banks have sophisticated protection mechanisms but for most purposes, a CSRF token is protection enough. If CSRF token is additional field appended to a form that has been put there by a server and it starts server side as well. If someone is submitting a request, the seller checks that token against the one that has stored and only execute the requests if these token match.

- - -
Next up: [Quiz: CSRF Quiz](ND024_Part4_Lesson05_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
