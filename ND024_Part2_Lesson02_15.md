# Lesson 2.15 Quiz: Project Part 1

Download the RWDF_L2_Start.zip.

##### Quiz Objective: 
- Make it responsive
- add a meta view port to the page
- make any adjustments to the CSS in markup
- make everything display in a single column
- use relative widths
- check your touch targets
- test your site across different viewports

##### My solution to the quiz:
insertions to index.html:
```
<head>
......
<meta name="viewport" content="width=device-width, initial-scale=1">
......
```
insertions to main.css :
```
header, nav, footer, section, article, div {
  ......
  min-width:100%;
}

/* These were placed towards the bottom of the page. */

img, embed, object, video {
  max-width: 100%;
}

.header__inner, .nav, main, .hero, .top-news, .scores, .weather {
	width: 100% !important;
	max-width: 960px;
}

body a, button {
  min-width: 48px;
  min-height: 48px;
  padding: 1.5em; /* I could had done a better job of fine-tuning here */
}

```

- - -
Next up: [Project Solution - Long](ND024_Part2_Lesson02_16.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
