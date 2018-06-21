# Lesson 8.5 HTTPS for security

### What HTTPS does for you
When a browser and a server speak HTTPS, they're just speaking HTTP, but over an encrypted connection. The encryption follows a standard protocol called Transport Layer Security, or TLS for short. TLS provides some important guarantees for web security:

- It keeps the connection private by encrypting everything sent over it. Only the server and browser should be able to read what's being sent.
- It lets the browser authenticate the server. For instance, when a user accesses https://www.udacity.com/, they can be sure that the response they're seeing is really from Udacity's servers and not from an impostor.
- It helps protect the integrity of the data sent over that connection — checking that it has not been (accidentally or deliberately) modified or replaced.

Note: TLS is also very often referred to by the older name SSL (Secure Sockets Layer). Technically, SSL is an older version of the encryption protocol. This course will talk about TLS because that's the current standard.

#### QUESTION 1 OF 4
Here are a few different malicious things that an attacker could do to normal HTTP traffic. Each of the three guarantees (privacy, authenticity, and integrity) helps defend against one of them. Match them up!

Privacy - You're reading your email in a coffee shop, and the shop owner can read your email off of their Wi-Fi network you're using.
Authenticity - You think you're logging into Facebook, but actually you're sending your Facebook password to a server in the coffee shop's back room.
Integrity - The coffee shop owner doesn't like cat pictures, so they replace all the cat pictures on the web pages you're looking at with pictures of celery.

### Inspecting TLS on your service
If you deployed a web service on Heroku earlier in this lesson, then HTTPS should already be set up. The URI that Heroku assigned to your app was something like https://yourappname.herokuapp.com/.

From there, you can use your browser to see more information about the HTTPS setup for this site. However, the specifics of where to find this information will depend on your browser. You can experiment to find it, or you can check the documentation: Chrome, Firefox, Safari.

Note: In some browser documentation you'll see references to SSL certificates. These are the same as TLS certificates. Remember, SSL is just the older version of the encryption standard.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/585471ca_screen-shot-2016-12-16-at-14.58.51/screen-shot-2016-12-16-at-14.58.51.png">

Most browsers have a lock icon next to the URI when you're viewing an HTTPS web site.
Clicking on the lock is how you start exploring the details of the HTTPS connection.
Here, I've clicked on the lock on my bookmark server deployed on Heroku.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/5854715d_screen-shot-2016-12-16-at-14.56.54/screen-shot-2016-12-16-at-14.56.54.png">

Viewing TLS certificate details for the *.herokuapp.com certificate in Google Chrome.

### What does it mean?
Well, there are a lot of locks in these pictures. Those are how the browser indicates to the user that their connection is being protected by TLS. However, these dialogs also show a little about the server's TLS setup.

### Keys and certificates
The server-side configuration for TLS includes two important pieces of data: a private key and a public certificate. The private key is secret; it's held on the server and never leaves there. The certificate is sent to every browser that connects to that server via TLS. These two pieces of data are mathematically related to each other in a way that makes the encryption of TLS possible.

The server's certificate is issued by an organization called a certificate authority (CA). The certificate authority's job is to make sure that the server really is who it says it is — for instance, that a certificate issued in the name of Heroku is actually being used by the Heroku organization and not by someone else.

The role of a certificate authority is kind of like getting a document notarized. A notary public checks your ID and witnesses you sign a document, and puts their stamp on it to indicate that they did so.

#### QUESTION 2 OF 4
Take a look at the TLS certificate presented for your deployed app, or the screenshots above from my version of it. What organization was this server certificate issued to? Who issued it?

It was issued to Heroku, and the issuer is DigiCert.

### How does TLS assure privacy?
The data in the TLS certificate and the server's private key are mathematically related to each other through a system called public-key cryptography. The details of how this works are way beyond the scope of this course. The important part is that the two endpoints (the browser and server) can securely agree on a shared secret which allows them to scramble the data sent between them so that only the other endpoint — and not any eavesdropper — can unscramble it.

### How does TLS assure authentication?
A server certificate indicates that an encryption key belongs to a particular organization responsible for that service. It's the job of a certificate authority to make sure that they don't issue a cert for (say) udacity.com to someone other than the company who actually runs that domain.

But the cert also contains metadata that says what DNS domain the certificate is good for. The cert in the picture above is only good for sites in the .herokuapp.com domain. When the browser connects to a particular server, if the TLS domain metadata doesn't match the DNS domain, the browser will reject the certificate and put up a big scary warning to tell the user that something fishy is going on.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/December/5854788f_screen-shot-2016-12-16-at-15.27.45/screen-shot-2016-12-16-at-15.27.45.png">

The big scary warning that Chrome displays if a TLS certificate is not valid.

### How does TLS assure integrity?
Every request and response sent over a TLS connection is sent with a message authentication code (MAC) that the other end of the connection can verify to make sure that the message hasn't been altered or damaged in transit.

#### QUESTION 3 OF 4
Suppose that an attacker were able to trick your browser into sending your udacity.com requests to the attacker's server instead of Udacity's real servers. What could the attacker do with that evil ability?

If your browser believes the attacker's server is udacity.com, it will send your udacity.com authentication cookies to the attacker's server. They can then put those cookies in their own web client and masquerade as you when talking to the real site. Also, if your browser is fetching content from the attacker's server, the attacker can put whatever they want in that content. They could even forward most of the content from the real server.

However, compromising Udacity's site would not allow an attacker to break into your Gmail or Facebook accounts, and fortunately it wouldn't let the attacker blow up your computer either.

#### QUESTION 4 OF 4
When your browser talks to your deployed service over HTTPS, there are still some ways that an attacker could spy on the communication. Mark the cases that HTTPS does not protect against:

HTTPS only protects your data in transit. It doesn't protect it from an attacker who has taken over your computer, or the computer that's running your service. So items 1, 4, and 5 are not things that HTTPS can help with.

- - -
Next up: [Beyond GET and POST](ND024_Part4_Lesson08_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
