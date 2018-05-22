# Lesson 6.14 Working with Maps

### Working with Maps
After you’ve built your Map, you can use the .has() method to check if a key-value pair exists in your Map by passing it a key.
```
const members = new Map();

members.set('Evelyn', 75.68);
members.set('Liam', 20.16);
members.set('Sophia', 0);
members.set('Marcus', 10.25);

console.log(members.has('Xavier'));
console.log(members.has('Marcus'));
```
    false
    true

And you can also retrieve values from a Map, by passing a key to the .get() method.
```
console.log(members.get('Evelyn'));
```
    75.68

- - -
Next up: [Looping Through Maps](ND024_Part3_Lesson06_15.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
