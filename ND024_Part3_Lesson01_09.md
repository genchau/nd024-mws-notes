# Lesson 1.9 A Full Request

This will console.log the response, which is pretty useless.
```
function handleSuccess () { 
  console.log( this.responseText ); 
}
function handleError () { 
  console.log( 'An error occurred \uD83D\uDE1E' );
}
const asyncRequestObject = new XMLHttpRequest();
asyncRequestObject.open('GET', 'https://unsplash.com');
asyncRequestObject.onload = handleSuccess;
asyncRequestObject.onerror = handleError;
asyncRequestObject.send();
```

onload function to handle a JSON response:
```
function handleSuccess () {
const data = JSON.parse( this.responseText ); // convert data from JSON to a JavaScript object
console.log( data );
}

asyncRequestObject.onload = handleSuccess;
```

- - -
Next up: [Project Initial Walkthrough](ND024_Part3_Lesson01_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
