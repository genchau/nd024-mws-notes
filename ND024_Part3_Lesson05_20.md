# Lesson 5.20 Quiz: Building Classes and Subclasses (2-3)

### Directions:
Create a Bicycle subclass that extends the Vehicle class. The Bicycle subclass should override Vehicle's constructor function by changing the default values for wheels from 4 to 2 and horn from 'beep beep' to 'honk honk'.

### Your Code:
```
/*
 * Programming Quiz: Building Classes and Subclasses (2-3)
 */

class Vehicle {
	constructor(color = 'blue', wheels = 4, horn = 'beep beep') {
		this.color = color;
		this.wheels = wheels;
		this.horn = horn;
	}

	honkHorn() {
		console.log(this.horn);
	}
}

// your code goes here
class Bicycle extends Vehicle {
    constructor(color = 'blue', wheels = 2, horn = 'honk honk') {
        super(color, wheels, horn);
    }
}

const myVehicle = new Vehicle();
myVehicle.honkHorn(); // beep beep
const myBike = new Bicycle();
myBike.honkHorn(); // honk honk
```

- - -
Next up: [Lesson 2 Summary](ND024_Part3_Lesson05_21.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
