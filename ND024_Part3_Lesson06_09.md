# Lesson 6.9 Quiz: Using Sets

### Directions:
Create a variable with the name myFavoriteFlavors and give it the value of an empty Set object. Then use the .add() method to add the following strings to it:

"chocolate chip"
"cookies and cream"
"strawberry"
"vanilla"
Then use the .delete() method to remove "strawberry" from the set.

### Your Code:
```
/*
 * Programming Quiz: Using Sets (3-1)
 *
 * Create a Set object and store it in a variable named `myFavoriteFlavors`. Add the following strings to the set:
 *     - chocolate chip
 *     - cookies and cream
 *     - strawberry
 *     - vanilla
 *
 * Then use the `.delete()` method to remove "strawberry" from the set.
 */

const myFavoriteFlavors = new Set([]);
console.log(myFavoriteFlavors);
myFavoriteFlavors.add('chocolate chip');
console.log(myFavoriteFlavors);
myFavoriteFlavors.add('cookies and cream');
console.log(myFavoriteFlavors);
myFavoriteFlavors.add('strawberry');
console.log(myFavoriteFlavors);
myFavoriteFlavors.add('vanilla');
console.log(myFavoriteFlavors);
myFavoriteFlavors.delete('strawberry');
console.log(myFavoriteFlavors);
```

- - -
Next up: [WeakSets](ND024_Part3_Lesson06_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
