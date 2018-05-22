# Lesson 6.6 Modifying Sets

### Modifying Sets
After you’ve created a Set, you’ll probably want to add and delete items from the Set. So how do you that? You use the appropriately named, .add() and .delete() methods:
```
const games = new Set(['Super Mario Bros.', 'Banjo-Kazooie', 'Mario Kart', 'Super Mario Bros.']);

games.add('Banjo-Tooie');
games.add('Age of Empires');
games.delete('Super Mario Bros.');

console.log(games);
```
    Set {'Banjo-Kazooie', 'Mario Kart', 'Banjo-Tooie', 'Age of Empires'}

On the other hand, if you want to delete all the items from a Set, you can use the .clear() method.
```
games.clear()
console.log(games);
```
    Set {}

TIP: If you attempt to .add() a duplicate item to a Set, you won’t receive an error, but the item will not be added to the Set. Also, if you try to .delete() an item that is not in a Set, you won’t receive an error, and the Set will remain unchanged.

.add() returns the Set if an item is successfully added. On the other hand, .delete() returns a Boolean (true or false) depending on successful deletion.

- - -
Next up: [Working with Sets](ND024_Part3_Lesson06_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
