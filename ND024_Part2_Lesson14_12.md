# Lesson 14.12 Quiz: Combo Box

#### Quiz:
folder: `lesson5-semantics-aria/13-combobox` -> `combobox.js`

Problems:
- ChromeVox reports wrong list size and position after filtering the searchbox.
- ChromeVox does not read to us the active item, a job for `aria-activedescendant`.

[WAI-ARIA Authoring Practices 1.1](https://www.w3.org/TR/2016/WD-wai-aria-practices-1.1-20160317/#combobox)

#### Solution:

`filter: function(str)`
```
filter: function(str) {
    this.visibleItems = [];
    var foundItems = 0;
    for (var item of this.items) {
        if (item.textContent.toLowerCase().startsWith(str.toLowerCase())) {
            foundItems++;
            item.hidden = false;
            this.visibleItems.push(item);
        } else {
            item.hidden = true;
            item.classList.remove('active');
        }
    }
    if (foundItems === 0) {
        this.hide();
    } else {
        for (var i = 0; i < this.visibleItems.length; i++) {
            var item = this.visibleItems[i];
            item.setAttribute('aria-posinset', i + 1);
            item.setAttribute('aria-setsize', this.visibleItems.length);
        }
    }
},
```

`item.setAttribute('aria-posinset', i + 1);` this sets up the position in set using the iterator `i`. `+ 1` was needed due to `posinset` being a 1 based index vs 0 based index used for i.

`item.setAttribute('aria-setsize', this.visibleItems.length);` We just simply give the array length to `aria-setsize`.

`changeActiveListitem()` in addition to setting active, we need to setActiveDescendant for ARIA:
```
changeActiveListitem: function(newIdx) {
    var active = this.activeItem;
    var newActive = this.visibleItems[newIdx];
    if (active)
        active.classList.remove('active');
    newActive.classList.add('active');

    this.textbox.setActiveDescendant(newActive);
}
```
`this.textbox.setActiveDescendant(newActive);` the function works off a `textbox`. It takes a list element as a parameter.

- - -
Next up: [Hidden in Plain Sight](ND024_Part2_Lesson14_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
