# Lesson 5.12 Class Preview

### Class Preview
Here's a quick peek of what a JavaScript class look like:
```
class Dessert {
  constructor(calories = 250) {
    this.calories = calories;
  }
}

class IceCream extends Dessert {
  constructor(flavor, calories, toppings = []) {
    super(calories);
    this.flavor = flavor;
    this.toppings = toppings;
  }
  addTopping(topping) {
    this.toppings.push(topping);
  }
}
```
Notice the new class keyword right in front of Dessert and IceCream, or the new extends keyword in class IceCream extends Dessert? What about the call to super() inside the IceCream's constructor() method.

There are a bunch of new keywords and syntax to play with when creating JavaScript classes. But, before we jump into the specifics of how to write JavaScript classes, we want to point out a rather confusing part about JavaScript compared with class-based languages.

- - -
Next up: [JavaScript's Illusion of Classes](ND024_Part3_Lesson05_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
