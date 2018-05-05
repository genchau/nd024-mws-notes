# Lesson 12.14 Quiz: Labeling Input Elements

#### Quiz:

folder: `lesson3-semantics-built-in/16-labelling-input-elements/`

Objective: 
- One form element doesn't have a label.
- Find that element.
- FIx the code.

Problem:
```
<div class="inline-control sign-up col-1">
    <input type="checkbox" checked name="jLetter" id="jLetter"> Receive promotional offers?
</div>
```

Solution:
```
<style>
  label[for=jLetter] {
    display: inline;
  }

  div.promotional {
    margin-bottom: 8px;
  }
</style>
...
<div class="inline-control sign-up col-1">
  <div class="promotional">
    <input type="checkbox" checked name="jLetter" id="jLetter">
    <label for="jLetter">Receive promotional offers?</label>
  </div>
</div>
```

- - -
Next up: [Text Alternatives](ND024_Part2_Lesson12_15.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
