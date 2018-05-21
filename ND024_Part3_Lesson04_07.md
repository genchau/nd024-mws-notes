# Lesson 4.7 Quiz: Destructuring Arrays (1-3)

### Directions:
Use array destructuring to pull out the three colors from the array of things and store them into the variables one, two, and three.

### Your Code:
```
/*
 * Programming Quiz: Destructuring Arrays (1-3)
 *
 * Use destructuring to initialize the variables `one`, `two`, and `three`
 * with the colors from the `things` array.
 */

const things = ['red', 'basketball', 'paperclip', 'green', 'computer', 'earth', 'udacity', 'blue', 'dogs'];

const [one,,, two,,,, three] = things;

const colors = `List of Colors
1. ${one}
2. ${two}
3. ${three}`;

console.log(colors);
```

- - -
Next up: [Object Literal Shorthand](ND024_Part3_Lesson04_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
