# Lesson 13.5 Setting Up ESLint

To make the linter most effective, we want to have it run at the earliest possible time. And th earliest possible time is, in our case, after we press the key on our keyboard, making a change in Sublime. In order for this to work, we'll need to install ESlint first via npm. 

```
npm install -g eslint
```
Now we need 2 different Sublime plugins. SublimeLinter is a framework around linting, but doesn't come with specific language linters. And sublimeLinter-contrib-eslint is the wrapper code that connects ESLint to SublimeLinter.

In sublime, command palette, ctrl+shift+p,
Install SublimeLinter
Install SublimeLinter-contrib-eslint
Restart editor.

Now we need to configure ESLint.
```
eslint --init
```
We can use: Tabs, Single, Unix, Yes, No, Browser, No, JSON setting.

This generates a .eslintrc.js file. The key is the extends block at the bottom. This tells eslint to run with its recommended set, and anything we add on top will overwrite or add to it.
- - -
The instructions from the video did not work, I used instructions from here: [GitHub - roadhump/SublimeLinter-contrib-eslint_d: This linter plugin for SublimeLinter provides an interface to eslint_d](https://github.com/roadhump/SublimeLinter-contrib-eslint_d)

1. Install Node.js and npm
2. Install `npm install -g eslint_d`
3. Run `npm init -f npm install eslint_d`
4. Install sublime plugins from package control in command palette:
    - SublimeLinter-contrib-eslint_d
5. Run `eslint --init`
Here's my .eslintrc.js
```
module.exports = {
    "env": {
        "browser": true,
        "es6": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "sourceType": "module"
    },
    "rules": {
        "indent": [
            "error",
            "tab"
        ],
        "linebreak-style": [
            "error",
            "unix"
        ],
        "quotes": [
            "error",
            "single"
        ],
        "semi": [
            "error",
            "always"
        ]
    }
};
```
- - -
Here's ESLint in action. Open \ud892\Lesson 3\js\main.js. The red dot indicates an error. To see what the error is click on the foo, then look at status bar at the bottom of Sublime. 2 errors in this program. Foo not defined. And foo not used. To fix, add "var". Then return foo.

In gulpfile.js, we'll find a lot of errors. ESLint thinks this file runs in the browser. Browser has no require function. We can turn off ESLint by typing the following:
```
/*eslint-env node */
```

- - -
Next up: [Setting up ESLint in Gulp](ND024_Part3_Lesson13_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
