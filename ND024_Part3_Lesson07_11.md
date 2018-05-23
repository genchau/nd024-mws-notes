# Lesson 7.11 Using Babel

The most popular JavaScript transpiler is called Babel.

Babel's original name was slightly more descriptive - 6to5. This was because, originally, Babel converted ES6 code to ES5 code. Now, Babel does a lot more. It'll convert ES6 to ES5, JSX to JavaScript, and Flow to JavaScript.

Before we look at transpiling code on our computer, let's do a quick test by transpiling some ES6 code into ES5 code directly on the Babel website. Check out Babel's REPL and paste the following code into the section on the left:
```
class Student {
  constructor (name, major) {
    this.name = name;
    this.major = major;
  }

  displayInfo() {
    console.log(`${this.name} is a ${this.major} student.`);
  }
}

const richard = new Student('Richard', 'Music');
const james = new Student('James', 'Electrical Engineering');
```

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/5888fc24_babel-es6-to-es5/babel-es6-to-es5.png">
ES6 code on the left that's being transpiled to ES5 code on the right.

### Transpiling project in repo
If you check in the [repo for this project](https://github.com/udacity/course-es6/tree/master/lesson-4/walk-through-transpiling), inside the Lesson 4 directory is a little project that's all set up for transpiling ES6 code to ES5 code. There's an "ES6" directory that contains the ES6 code we'll be transpiling (using Babel) to ES5 code that will be able to run in every browser.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/5888fd20_es6-code-in-project/es6-code-in-project.png">
Code editor with ES6 code that will be transpiled.

The way Babel transforms code from one language to another is through plugins. There are plugins that transform ES6 arrow functions to regular ES5 functions (the ES2015 arrow function plugin). There are plugins that transform ES6 template literals to regular string concatenation (the ES2015 template literals transform). For a full list, check out all of Babel's plugins.

Now, you're busy and you don't want to have to sift through a big long list of plugins to see which ones you need to convert your code from ES6 to ES5. So instead of having to use a bunch of individual plugins, Babel has presets which are groups of plugins bundled together. So instead of worrying about which plugins you need to install, we'll just use the ES2015 preset that is a collection of all the plugins we'll need to convert all of our ES6 code to ES5.

You can see that the project has a .babelrc file. This is where you'd put all of the plugins and/or presets that the project will use. Since we want to convert all ES6 code, we've set it up so that it has the ES2015 preset.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2017/January/5888fdb4_es6-preset-in-project/es6-preset-in-project.png">
Code editor with .babelrc file that has ES2015 preset listed.

WARNING: Babel uses both Node and NPM to distribute its plugins. So before you can install anything, make sure you have both of these tools installed:

install Node (which will automatically install NPM)

- - -
Next up: [Transpiling Walkthrough](ND024_Part3_Lesson07_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
