# Lesson 4.13 Quiz: Writing a For...of Loop (1-4)

### Directions:
Write a for...of loop that:

loops through each day in the days array
capitalizes the first letter of the day
and prints the day out to the console
Your code should log the following to the console:

      Sunday
      Monday
      Tuesday
      Wednesday
      Thursday
      Friday
      Saturday

### Your Code:
```
/*
 * Programming Quiz: Writing a For...of Loop (1-4)
 */

const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];

// your code goes here
for (const day of days) {
    console.log( day.charAt(0).toUpperCase() + day.substr(1) );
}
```

- - -
Next up: [Spread... Operator](ND024_Part3_Lesson04_14.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
