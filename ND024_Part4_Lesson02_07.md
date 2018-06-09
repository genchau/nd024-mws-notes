# Lesson 2.7 Quiz: Request Headers Quiz

Send an HTTP Request

- Download [this](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/June/575716a0_ud897-l2-request-headers-binary/ud897-l2-request-headers-binary.zip)
- launch the provided server
- send a request
    - use UDACITY method
    - include HOST header
    - set header X-Udacity-Exercise-Header to some text
    - set the Date header to Wed, 11 Jan 1995 23:00:00 GMT


Solution:
- I downloaded netcat from [here](https://eternallybored.org/misc/netcat/netcat-win32-1.12.zip)
- `nc netcat.127.0.0.1.xip io 8080`
- `UDACITY / HTTP/1.1`
- `Host: www.udacity.com`
- `X-Udacity-Exercise-Header: level-up`
- `Date: Wed, 11 Jan 1995 23:00:00 GMT`

ba16d

- - -
Next up: [REST](ND024_Part4_Lesson02_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
