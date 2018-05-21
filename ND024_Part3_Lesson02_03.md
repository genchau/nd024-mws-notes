# Lesson 2.3 Handling The Returned Data

Similar to XHR, we need a function to handle the response. We can chain on to `.ajax()` with a `.done()` method.
```
function handleResponse(data) {
    console.log('the ajax request has finished!');
    console.log(data);
}

$.ajax({
    url: 'https://swapi.co/api/people/1/'
}).done(handleResponse);
```

unsplash:
```
$.ajax({
    url: `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`
}).done(addImage);
```

Notice:
- We did not need to create an XHR object
- instead of specifying that the request is a GET request, it defaults to that and we just provide the URL of the resource we're requesting.
- Instead of setting `onload`, we use the `.done()` method.

```
$.ajax({
    url: `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`
}).done(addImage);
```

- - -
Next up: [Cleaning up the Success Callback](ND024_Part3_Lesson02_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
