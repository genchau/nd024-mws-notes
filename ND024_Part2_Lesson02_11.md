# Lesson 2.11 Quiz: Relative Sizes

##### Quiz and solution:
Which of the following snippets of code are responsive? Check all that apply.

- [X] Upper-Left. This is responsive because of the *relative* max width.
```
<img id="owl">
#owl {
  width: 640px;
  max-width: 100%;
}
```
- [ ] Bottom-Left. This is not responsive because of absolute width. 
```
<div class="box"></div>
.box {
  width: 350px;
}
```
- [X] Upper-Right. Although this is an absolute width of 125px, it's considered responsive because 125px will be smaller than almost all screens that users will use which is usually considered 360px on the smallest phone width.
```
<img class="logo">
.logo {
  width: 125px;
}
```
- [X] Bottom-Right. This is responsive because of the relative width size.
```
<div class="city"></div>
.city {
  width: 100%;
}
```

- - -
Next up: [Tap Target Sizes](ND024_Part2_Lesson02_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
