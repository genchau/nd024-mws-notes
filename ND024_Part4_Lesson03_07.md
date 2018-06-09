# Lesson 3.7 TLS: Hashing

So we have a look at encryption but remember that TLS is made up of two parts, encryption and hashing. Hashing is the process of transforming data into a short representation of the original data. The smallest change in the original data will have enormous changes in the hash. If two documents yield the same hash value, they are very very likely to be the same documents. There are a couple of things we care about with hashing functions. One, it should be impossible to revert the conversion process, meaning once data has been converted into a hash, it can't be unconverted back into the original data. And 2, it should be just as impossible to find a different document yielding an identical hash value. One of the most common hashing functions is SHA which exists in multiple flavors like SHA-256 or SHA-512 where the number says how big the output of the hash is in bits. No matter how big the document is that we pass in, we will always get 25 bits as output when we're using SHA-256.

- - -
Next up: [Quiz: Hashing Quiz](ND024_Part4_Lesson03_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
