# Lesson 11.15 Offscreen Content

What do we do with offscreen content with links? For example a responsive drawer panel. When you tab through a page like this the focus actually disappears and tabs through the hidden nav drawer. 

We can use console.log to figure out where the focus is by typing in `document.activeElement`

We can use an extension to help us identify which links will be hidden. In Chrome Web Store install "Accessibility Developer Tools." >> Then go into Audits section. >> Uncheck everything except Accessibility.

To fix the drawer we can either:
`display: none;` or ` visibility: hidden` whenever it is off screen. This will prevent focus from being able to move into that element.

Then when the nav drawer comes back on-screen, we set `display: block` or `visibility: visible`. 

- - -
Next up: [Quiz: Implement Offscreen Content](ND024_Part2_Lesson11_16.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
