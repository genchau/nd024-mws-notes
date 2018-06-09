# Lesson 1.11 Quiz: Fetch Quiz

Download [this](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/June/5755fd25_l1-fetch-binary/l1-fetch-binary.zip)

```
fetch('password.txt', {
  'method': 'PUT',
  'headers': {
    'X-Udacity-Exercise': 'fetch rocks!'
  }
}).then(function(response) {
  return response.text();
}).then(function(data) {
  console.log(data);
});
```
piquizahhai5aeh2fah9Uk

[That's so fetch! - JakeArchibald.com](https://jakearchibald.com/2015/thats-so-fetch/)

- - -
Next up: [Outro](ND024_Part4_Lesson01_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
