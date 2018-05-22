# Lesson 5.19 Working with JavaScript Subclasses

### Working with subclasses
Like most of the new additions, there's a lot less setup code and it's a lot cleaner syntax to create a subclass using class, super, and extends.

Just remember that, under the hood, the same connections are made between functions and prototypes.

### super must be called before this
In a subclass constructor function, before this can be used, a call to the super class must be made.
```
class Apple {}
class GrannySmith extends Apple {
  constructor(tartnessLevel, energy) {
    this.tartnessLevel = tartnessLevel; // `this` before `super` will throw an error!
    super(energy); 
  }
}
```

QUESTION 1 OF 2
Take a look at the following code:
```
class Toy {}
class Dragon extends Toy {}
const dragon1 = new Dragon();
```
Given the code above, is the following statement true or false?
```
dragon1 instanceof Toy;
```
    true


QUESTION 2 OF 2
Let's say that a Toy class exists and that a Dragon class extends the Toy class.

What is the correct way to create a Toy object from inside the Dragon class's constructor method?

    super();


- - -
Next up: [Quiz: Building Classes and Subclasses (2-3)](ND024_Part3_Lesson05_20.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
