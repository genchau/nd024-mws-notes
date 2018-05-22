# Lesson 5.18 Extending Classes from ES5 to ES6

Let's hide the inner workings of these classes to compare how they are constructed.
Remember that there's a new special method called the
constructor that's run whenever the class is called.
It's doing the same thing as this tree constructor over here.
Also remember, that a method name inside of
a class definition is the same thing as adding that method to the prototype.
That takes care of this base class which looks pretty similar.
The bigger difference comes when extending the base class with a subclass.
With the older ES5 code,
we'd have to create another constructor function.
Then we'd have to set the function's prototype to the base classes prototype.
And since we've overridden the original prototype object,
we need to remake the connection between
the constructor property and the original constructor function.
Then we're back to the normal routine of adding methods to the prototype object.
Now compare all of the code it took to get these two functions
connected and prototype linked to this code over here.
It's just another class definition but it uses
the extends keyword to connect this maple class to the base class tree.
Significantly nicer, right?
It's also a lot easier to call the base class from the subclass.
The ES6 code uses the new super keyword.
Well, you have to use.call in the ES5 code and pass this and is the first argument.
And calling a prototype method also takes a lot less code in the new class format too.


- - -
Next up: [Working with JavaScript Subclasses](ND024_Part3_Lesson05_19.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
