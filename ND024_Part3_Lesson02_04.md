# Lesson 2.4 Cleaning up the Success Callback

unsplash:
```
function addImage(images) {
    const firstImage = images.results[0];

    responseContainer.insertAdjacentHTML('afterbegin', `<figure>
            <img src="${firstImage.urls.small}" alt="${searchedForText}">
            <figcaption>${searchedForText} by ${firstImage.user.name}</figcaption>
        </figure>`
    );
}
```

It's better than XHR:
- The function now has one parameter `images`
- This parameter has already been converted from JSON to a JavaScript object, so * the line that had JSON.parse() is no longer needed.
- The `firstImage` variable is set to the images.results first item.

- - -
Next up: [Code Walkthrough](ND024_Part3_Lesson02_05.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
