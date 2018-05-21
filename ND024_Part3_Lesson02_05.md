# Lesson 2.5 Code Walkthrough

Link to my github repo:
https://github.com/genchau/course-ajax/blob/master/lesson-2-async-w-jQuery/app.js

Link to github preview:
https://htmlpreview.github.io/?https://github.com/genchau/course-ajax/blob/master/lesson-2-async-w-jQuery/index.html

```
/* eslint-env jquery */

(function () {
    const form = document.querySelector('#search-form');
    const searchField = document.querySelector('#search-keyword');
    let searchedForText;
    const responseContainer = document.querySelector('#response-container');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        responseContainer.innerHTML = '';
        searchedForText = searchField.value;

        function addImage(images) {
        	console.log(images);// TODO_REMOVE
        	const firstImage = images.results[0];

        	if (images.results.length>0){
		    	responseContainer.insertAdjacentHTML('afterbegin', 
		    		`<figure>
		    		<img src="${firstImage.urls.small}" alt="${searchedForText}">
		    		<figcaption>${searchedForText} by ${firstImage.user.name}, ${firstImage.likes} likes</figcaption>
		    		</figure>`
		    	);
        	} else {
        		responseContainer.insertAdjacentHTML('afterbegin', 
        			'<div class="error-no-image">No images available</div>'
        		)
        	}
        }

        function addArticles(articles) {
        	let htmlContent = '';

        	if (articles.response.docs.length > 0) {
        		htmlContent = 
        		'<ul>\n' +
        			articles.response.docs.map(articlesNYTimes => 
        				`<li class="article">
        					<h2><a href="${articlesNYTimes.web_url}" target="_blank">${articlesNYTimes.headline.main}</a></h2>
        					<p>${articlesNYTimes.snippet}</p>
        				</li>`)
        			.join('\n') +
        		'\n</ul>';
        	} else {
        		htmlContent = '<div class="error-no-articles">No articles available</div>';
        	}

        	responseContainer.insertAdjacentHTML('beforeend', htmlContent);
        }

        function requestError(e, part) {
        	console.log(e);
        	responseContainer.insertAdjacentHTML('afterbegin', `<p class="network-warning error-no-${part}">Oh no! There was an error making a request for the ${part}.</p>`);
        }

    	$.ajax({
    		url: `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`,
    		headers: {
    			Authorization: 'Client-ID 611dc2767c8fcc33f0013f0c03634373b5c864669a77f37b7133f9377bf52f8e'
    		}
    	}).done(addImage)
    	.fail(function(err) {
    		console.log("GC Error getting data from unsplash");
    		requestError(err, 'image');
    		console.log("GC requestError image activated");
    	});

    	$.ajax({
    		url: `http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=e35e661abcd54895b4b2842465fb67a0`,
    	}).done(addArticles)
    	.fail(function(err) {
    		console.log("GC Error getting data from NY Times");
    		requestError(err, 'articles');
    		console.log("GC requestError articles activated");
    	});

    });
})();
```
With my own annotations:
```
/* eslint-env jquery */

(function () {
    const form = document.querySelector('#search-form'); //GC comment: queries HTML for the form.
    const searchField = document.querySelector('#search-keyword'); //GC comment: queries HTML for the search field box
    let searchedForText; //GC comment: this will be used to store the string of the search
    const responseContainer = document.querySelector('#response-container'); //GC comment: The response container is where we'll be adding the html to display the images and articles.

    form.addEventListener('submit', function (e) { //GC comment: First thing we are doing here is listen for the submit button to get clicked.
        e.preventDefault(); //GC comment: prevents browser's default behavior, so we can handle the submit request.
        responseContainer.innerHTML = ''; //GC comment: We are going to clear the webpage of previous search results.
        searchedForText = searchField.value; //GC comment: We are storing the string value of the search terms.

        function addImage(images) { //GC comment: our addImage function called after a successful ajax response.
        	console.log(images);// TODO_REMOVE, this is for me to understand how images looked like.
        	const firstImage = images.results[0]; //GC comment: We are only interested in the first image result. So we are storing the firstImage.

        	if (images.results.length>0){ //GC comment: Here we are checking if unsplash returned any images.
		    	responseContainer.insertAdjacentHTML('afterbegin', 
		    		`<figure>
		    		<img src="${firstImage.urls.small}" alt="${searchedForText}">
		    		<figcaption>${searchedForText} by ${firstImage.user.name}, ${firstImage.likes} likes</figcaption>
		    		</figure>`
		    	); //GC comment: We are writing to the html using figure element, with a figcaption of example: bears by Dr. Seuss, 2344 likes.
        	} else { //GC comment: We'll use the default error-no-image css when it fails to receive any images.
        		responseContainer.insertAdjacentHTML('afterbegin', 
        			'<div class="error-no-image">No images available</div>'
        		) //GC comment: afterbegin is the param for insertAdjacentHTML. It tells it to insert the html right after the first element.
        	}
        }

        function addArticles(articles) { //GC comment: our addArticles function called after a successful ajax response from ny times.
        	let htmlContent = ''; //GC comment: starts with an empty string. It's different from addImage, because addImage runs first it's able to directly modify responseContainer.

        	if (articles.response.docs.length > 0) { //GC comment: checks to see if we received at least 1 article.
        		htmlContent = //GC comment: We're using map method, and join method to iterate through the articles and write the list elements for the html.
        		'<ul>\n' +
        			articles.response.docs.map(articlesNYTimes => 
        				`<li class="article">
        					<h2><a href="${articlesNYTimes.web_url}" target="_blank">${articlesNYTimes.headline.main}</a></h2>
        					<p>${articlesNYTimes.snippet}</p>
        				</li>`)
        			.join('\n') +
        		'\n</ul>';
        	} else { //GC comment: if it fails we'll use the error-no-articles css.
        		htmlContent = '<div class="error-no-articles">No articles available</div>';
        	}

        	responseContainer.insertAdjacentHTML('beforeend', htmlContent); //GC comment: We insert the html into responsecontainer.
        }

        function requestError(e, part) { //GC comment: error function called by either ajax to unsplash or ny times.
        	console.log(e);
        	responseContainer.insertAdjacentHTML('afterbegin', `<p class="network-warning error-no-${part}">Oh no! There was an error making a request for the ${part}.</p>`);
        }

    	$.ajax({ //GC comment: ajax to unsplash with api key header.
    		url: `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`,
    		headers: {
    			Authorization: 'Client-ID 611dc2767c8fcc33f0013f0c03634373b5c864669a77f37b7133f9377bf52f8e'
    		}
    	}).done(addImage) //GC comment: runs addImage if successful.
    	.fail(function(err) {
    		console.log("GC Error getting data from unsplash");
    		requestError(err, 'image');
    		console.log("GC requestError image activated");
    	});

    	$.ajax({ //GC comment: ajax to ny times.
    		url: `http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=e35e661abcd54895b4b2842465fb67a0`,
    	}).done(addArticles) //GC comment: runs addArticles if successful
    	.fail(function(err) {
    		console.log("GC Error getting data from NY Times");
    		requestError(err, 'articles');
    		console.log("GC requestError articles activated");
    	});

    });
})();
```

- - -
Next up: [Peek inside $.ajax()](ND024_Part3_Lesson02_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
