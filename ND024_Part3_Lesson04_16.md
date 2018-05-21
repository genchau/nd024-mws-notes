# Lesson 4.16 Quiz: Using the Rest Parameter (1-5)

### Directions:
Use the rest parameter to create an average() function that calculates the average of an unlimited amount of numbers.

TIP: Make sure to test your code with different values. For example,

average(2, 6) should return 4
average(2, 3, 3, 5, 7, 10) should return 5
average(7, 1432, 12, 13, 100) should return 312.8
average() should return 0

### Your Code:
```
/*
 * Programming Quiz: Using the Rest Parameter (1-5)
 */

// your code goes here

function average(...nums) {
    let sum = 0;
    let addends = 0;
    for (const num of nums) {
        sum += num;
        addends += 1;
    }
    if (!addends) return 0;
    return sum/addends;
}

console.log(average(2, 6));
console.log(average(2, 3, 3, 5, 7, 10));
console.log(average(7, 1432, 12, 13, 100));
console.log(average());

```

- - -
Next up: [Lesson 1 Summary](ND024_Part3_Lesson04_17.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
