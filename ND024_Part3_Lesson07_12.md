# Lesson 7.12 Transpiling Walkthrough

The projects package.json file lists all of the NPM packages that this project depends on. This project depends on the babel-cli and the ES2015 preset that is a collection of all ES6 plugins. So these are the plugins that will be downloaded and installed. Once they're installed, we need to tell the babel-cli which plugins it should use to do the transpiling. The cli will check the .babelrc file for which plugins and presets to use. So the package.json file lists what should be installed and the babel rc file tells babel which plugins to use when it does it's transpiling. Now that babel knows to use this preset, we need to tell it to actually transpile the code. To do that we've added a build script that will tell babel to take the files in the ES6 directory, transpile them using that ES2015 preset and then put the transformed code in the ES5 directory.

package.json:
```
{
  "name": "es6",
  "version": "1.0.0",
  "description": "Simple app that demos transpiling ES6 code to ES5 code with Babel.",
  "main": "",
  "scripts": {
    "build": "babel ES6 -d ES5"
  },
  "author": "Richard Kalehoff",
  "license": "MIT",
  "devDependencies": {
    "babel-cli": "^6.16.0",
    "babel-preset-es2015": "^6.16.0"
  }
}
```
.babelrc:
```
{
    "presets": ["es2015"]
}
```

- - -
Next up: [Transpiling Recap](ND024_Part3_Lesson07_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
