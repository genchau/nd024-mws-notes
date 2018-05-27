# Lesson 12.3 Different Approaches for Live Editing

1. Live-editing within our browser. Some editors, like Brackets, come with live editing built in. In Brackets, we press a button that will launch a new instance of our browser with our updates already live. Sublime Text doesn't have it built in, but the Takana plugin gets pretty close. However, it supports CSS and SCSS live editing, but not HTML. 
2. Chrome DevTools has a relatively little known feature called Workspaces that allows you to ditch the editor altogether and work directly in the browser. We can make changes to our CSS right in the Styles panel, and have them persist. 
3. BrowserSync allows us to have live editing that is assisted by our build tool, improving upon the 2 methods we showed you before. For this to work, we can reuse something we've already learned about, and that's the watch task that currently watches our SASS for changes and compiles them into CSS. Browsersync works by creating or proxying a local web server which serves and tracks our files for changes. Best of all, it's free, open source, and is compatible with most Node.JS-based build tools including Gulp. 

[Takana](https://packagecontrol.io/packages/Takana) plugin on PackageControl

[Chrome Dev Workspaces](https://developer.chrome.com/devtools/docs/workspaces)

[Browser Sync](http://www.browsersync.io/)

- - -
Next up: [Using Browser-Sync](ND024_Part3_Lesson12_04.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
