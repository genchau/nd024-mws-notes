# Lesson 11.9 Managing Focus

General rule: Don't add tab index to site content.

Exception: Page manipulation with a user action. Such as navigation links that changes the content of the page.

In these cases, we want to add a tab index to the appropriate header with a -1. We'll call its focus with javascript after the user has clicked on it.

The described process is call managing focus.

Imagine not managing focus. A user clicks on a navigation link which jumps to the middle of the page. But the focus stays where it is at in the navigation menu. Using tab we would have to tab over all the nav links and then any content links. But if we did use focus management, when a user clicks the same nav link, the focus then jumps to that section's header. This method makes more sense when navigating with the keyboard or other accessible devices.

Styling focus will be covered in later section.

- - -
Next up: [Quiz: Manage Focus Yourself](ND024_Part2_Lesson11_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
