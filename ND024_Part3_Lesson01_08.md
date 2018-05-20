# Lesson 1.8 XHR's.send() method

This will send a request to unsplash for the home page. In dev tools type the following command in console. Click on network tab to see the unsplash.com XHR request. So we just requested something but did nothing with it.
```
const asyncRequestObject = new XMLHttpRequest();
asyncRequestObject.open('GET', 'https://unsplash.com');
asyncRequestObject.send();
```

Handling success:
```
function handleSuccess () {
    // in the function, the `this` value is the XHR object
    // this.responseText holds the response from the server

    console.log( this.responseText ); // the HTML of https://unsplash.com/
}

asyncRequestObject.onload = handleSuccess;
```

Handling errors:
```
function handleError () {
    // in the function, the `this` value is the XHR object
    console.log( 'An error occurred 😞' );
}

asyncRequestObject.onerror = handleError;
```

- - -
Next up: [A Full Request](ND024_Part3_Lesson01_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
