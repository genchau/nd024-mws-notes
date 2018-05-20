# Lesson 1.10 Project Initial Walkthrough

Download the starter code:
[GitHub - udacity/course-ajax](https://github.com/udacity/course-ajax)

3 separate folders:
1. lesson-1-async-w-xhr
2. lesson-2-async-w-jQuery
3. lesson-3-async-w-fetch

We'll need to setup an account for the APIs.

This is missing a request header:
```
function addImage(){}
const searchedForText = 'hippos';
const unsplashRequest = new XMLHttpRequest();

unsplashRequest.open('GET', `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`);
unsplashRequest.onload = addImage;

unsplashRequest.send()
```


- - -
Next up: [Setting a Request Header](ND024_Part3_Lesson01_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
