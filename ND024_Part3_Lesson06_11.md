# Lesson 6.11 Quiz: Working With WeakSets

### Directions:
Create the following variables:

uniqueFlavors and give it the value of an empty WeakSet object
flavor1, and set it to the object { flavor: 'chocolate' }
flavor2, and set it to an object with a property of flavor and a value of your choice
Use the .add() method to add the objects flavor1 and flavor2 to uniqueFlavors.

Use the .add() method to add the flavor1 object to the uniqueFlavors set, again.

### Your Code:
```
/*
 * Programming Quiz: Using Sets (3-2)
 *
 * Create the following variables:
 *     - uniqueFlavors and set it to a new WeakSet object
 *     - flavor1 and set it equal to `{ flavor: 'chocolate' }`
 *     - flavor2 and set it equal to an object with property 'flavor' and value of your choice!
 *
 * Use the `.add()` method to add the objects `flavor1` and `flavor2` to `uniqueFlavors`
 * Use the `.add()` method to add the `flavor1` object (again!) to the `uniqueFlavors` set
 */
 
const uniqueFlavors = new WeakSet([]);
const flavor1 = { flavor: 'chocolate' };
const flavor2 = { flavor: 'blueberry pomengranate' };
uniqueFlavors.add(flavor1);
uniqueFlavors.add(flavor2);
uniqueFlavors.add(flavor1);
console.log(uniqueFlavors);
```

- - -
Next up: [Maps](ND024_Part3_Lesson06_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
