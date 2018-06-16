# Lesson 5.2 Origins

As a general rule of thumb, JavaScript is not allowed to access the data of any other origin than its own. An origin is made up of three parts: the data scheme, the host name, and the port. For the page you're on right now, the scheme is HTTPS, the Host name is www.udacity.com, and the port is 443. If you change any of these parts, you are on a different origin and different rules will apply. Apart from the mixed content problems we talked about, earlier this is another reason to not mix HTTP and HTTPS URLs. But what are these rules that apply once you are working across multiple origins? First of all, you can't make fetch requests to other origins. Actually, under certain criteria, you can, but then you can't read the answer. Secondly, you cannot inspect iframes or windows with JavaScript if they are from another origin. These rules make a lot of sense if you think about it. Let's assume I was allowed to make fetch requests to other origins. I could just set up a website that makes fetch requests to Facebook.com and steal all your Facebook messages, or even worse, I could make fetch request to udacity.com and make you drop out of all of your Udacity classes. No, we don't want that. This restriction or rule is called the same origin policy.

[Same Origin Policy - Web Security](https://www.w3.org/Security/wiki/Same_Origin_Policy)

- - -
Next up: [Origins 2](ND024_Part4_Lesson05_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
