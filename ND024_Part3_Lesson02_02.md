# Lesson 2.2 jQuery's 'ajax()' Method

The `.ajax()` method is at the heart of all asynchronous requests for the entire jQuery library. There are a couple of ways you can call the `.ajax()` method:

```
$.ajax(<url-to-fetch>, <a-configuration-object>);

// or 

$.ajax(<just a configuration object>);
```

2 ways to use configuration object:
```
var settings = {
   frosting: 'buttercream',
   colors: ['orange', 'blue'],
   layers: 2,
   isRound: true
};

const myDeliciousCake = MakeCake( settings );
```
```
const myDeliciousCake = MakeCake({
   frosting: 'buttercream',
   colors: ['orange', 'blue'],
   layers: 2,
   isRound: true
});
```

Making an Ajax call:
```
$.ajax({
    url: 'https://swapi.co/api/people/1/'
});
```

- - -
Next up: [Handling The Returned Data](ND024_Part3_Lesson02_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
