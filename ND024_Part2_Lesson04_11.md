# Lesson 4.11 Quiz: Project Update Part 2

Download RWDF_L4_start.zip

Objective:
- Pick a set of breakpoints
- Use a responsive pattern to style the page
- Test on phones, tablets, and browser windows different sizes.

##### My Solution:
index.html modifications:
```
<head>
...
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
...
</head>
<body>

  <header class="navbar header">
    <div class="navbar-header header__inner">
  <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>                        
  </button>
  ...
  <nav id="myNavbar" class="nav collapse navbar-collapse">
      <ul class="nav__list nav navbar-nav navbar-right">
  ...
</body>
```

main.css modifications:
```
header, nav, footer, section, article, div {
  ...
  width:100%;
}
 .content {
	 display: flex;
	 flex-wrap: wrap;
 }
 img, embed, object, video {
  max-width: 100%;
}

.header__inner, .nav, .nav__list, main, .hero, .top-news, .scores, .weather {
	width: 100%;
	max-width: 960px;
	margin-left: auto;
	margin-right: auto;
}

body a, button {
  min-width: 48px;
  min-height: 48px;
  padding: 1.5em;
}

@media screen and (max-width: 550px) {
	.header__title {
		font-size: 2em;
		margin: 1.2em 0.5em;
	}
}

@media screen and (min-width: 700px) {
	.hero, .top-news {
		width: 50%;
	}
	.scores {
		width: 40%;
		height: 400px;
		margin-top: 80px;
	}
	.recent-news {
		width: 60%;
		height: 200px;
	}
	.weather {
		order: 1;
	}
}

.navbar-toggle {
	background-color: white;
	border: 1px solid gray;
}

.icon-bar {
	background-color: gray;
}
```
Links to files:
- [ND024_Part2_Lesson04_11_index.html](ND024_Part2_Lesson04_11_index.html)
- [ND024_Part2_Lesson04_11_main.css](ND024_Part2_Lesson04_11_main.css)

- - -
Next up: [Lesson Summary](ND024_Part2_Lesson04_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
