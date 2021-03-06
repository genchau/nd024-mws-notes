# Lesson 5.5 CORS

CORS has been adopted by API providers as the primary way to share resources. CORS headers permit cross origin requests without relying on JavaScript, though they do need some server side code. CORS sort us allow service to specify a set of origins that are allowed to access its resources. If the request refer header is on that list, it will be able to inspect the answer and use the data. Problem solved. However, if you take a closer look you will realize that by the time the server sends back the headers the request will already have executed. This can become problematic with destructive operations because it is already too late to ignore the request. This is where preflight requests come into play. A preflight request uses the options method and allows the browser to signal that it only wants to check what is allowed and what is not. A server should not execute any kind of business logic but only returned the headers similar to a head request. However not all requests will be preflighted, requests are made because of image text or forms will not be preflighted. So any kind of get request will be sent straight away, you just won't be able to read the answer, CORS doesn't allow it. The details about when preflight requests are actually sent with CORS are intricate and extensive, so I'll even link with details in instructor notes. Now we have a couple of ways to get around the single origin restriction. If you're ever involved in publishing an API yourself, I'd encourage you to think about CORS from the very beginning and to enable it on your server.

Request:
```
GET /courses?status=enrolled
Host: api.udacity.com
Referer: yourcourselist.com
```
Response:
```
HTTP/1.1 200 OK
Date: Mon, 30 May 2016 00:23:53 GMT
Access-Control-Allow-Origin: yourcourselist.com
Connection: Keep-Alive
Content-Type: application/xml
```

### Preflight Requests
Request:
```
OPTIONS /
Referer: yourcourselist.com
```
Response:
```
200 OK
Access-Control-Allow-Origin: yourcourselist.com
```

[Cross-Origin Resource Sharing (CORS) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests)

- - -
Next up: [Quiz: Preflight Request with CORS Quiz 1](ND024_Part4_Lesson05_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
