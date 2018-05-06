# Lesson 14.2 Why ARIA

Native elements are always preferred. They provide the following built-in support for free:
- focus
- keyboard support
- built in semantics

WAI-ARIA or just ARIA: Web Accessibility Initiatives - Accessible Rich Internet Applications.
- This spec is good for bridging areas where there are accessibility issues that can't ben managed with native HTML.

ARIA works by allowing us to specify attributes on elements which will get translated to the accessibility tree.

For example we want to implement a simple checkbox. We need:
- be focusable.
- handle the same keyboard interactions
- be intuitive for screen readers

Before ARIA:
```
    <div class="demo">

      <h2>Custom checkboxes</h2>

      <div tabindex="0" class="checkbox" checked>
        Tim-Tams
      </div>
      <div tabindex="0" class="checkbox">
        Mint slices
      </div>

      <h2>Native checkboxes</h2>

      <div>
        <label>
          <input type="checkbox" checked>
          Tim-Tams
        </label>
      </div>
      <div>
        <label>
          <input type="checkbox">
          Mint slices
        </label>
      </div>

    </div>
```
Problem with screen reader:
- The native checkbox will announce "checkbox checked" the custom checkbox does not.

Here's the ARIA fix by:
- adding role attribute `role=`
- adding ARIA attribute `aria-checked=`
```
    <div class="demo">

      <h2>Custom checkboxes</h2>

      <div tabindex="0" class="checkbox" checked role="checkbox" aria-checked="true">
        Tim-Tams
      </div>
      <div tabindex="0" class="checkbox" role="checkbox" aria-checked="false">
        Mint slices
      </div>

    </div>
```

You can think of ARIA as tree surgery on the accessibility tree. We add in ARIA branches.

BUT, that's the only thing ARIA does is modify the accessibility tree. We still need to make the element:
- focusable
- add keyboard event listeners.

[Custom checkboxes](http://udacity.github.io/ud891/lesson5-semantics-aria/02-why-aria/index.html)

[Accessible Rich Internet Applications (WAI-ARIA) 1.1](https://www.w3.org/TR/wai-aria-1.1/)


- - -
Next up: [Quiz: First Steps with ARIA](ND024_Part2_Lesson14_03.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
