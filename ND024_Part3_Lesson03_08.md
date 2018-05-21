# Lesson 3.8 Project Wrap-up

Link to my github repo: [course-ajax/app.js at master · genchau/course-ajax · GitHub](https://github.com/genchau/course-ajax/blob/master/lesson-3-async-w-fetch/app.js)

Link to my github preview: [GitHub & BitBucket HTML Preview](https://htmlpreview.github.io/?https://github.com/genchau/course-ajax/blob/master/lesson-3-async-w-fetch/index.html)

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


		function addImage(data) {
		    let htmlContent = '';
		    const firstImage = data.results[0];

		    if (firstImage) {
		        htmlContent = 
		        `<figure>
		    		<img src="${firstImage.urls.small}" alt="${searchedForText}">
		    		<figcaption>${searchedForText} by ${firstImage.user.name}, ${firstImage.likes} likes</figcaption>
		    	</figure>`;
		    } else {
		        htmlContent = '<div class="error-no-image">No images available</div>'
		    }

		    responseContainer.insertAdjacentHTML('afterbegin', htmlContent);
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

        fetch(`https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`, {
        	headers: {
        		'Authorization': 'Client-ID 611dc2767c8fcc33f0013f0c03634373b5c864669a77f37b7133f9377bf52f8e'
        	}
        }).then(response => response.json())
        .then(addImage)
        .catch(e => requestError(e, 'image'));

        fetch(`http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=e35e661abcd54895b4b2842465fb67a0`)
        .then(response => response.json())
        .then(addArticles)
        .catch(e => requestError(e, 'articles'));    

    });
})();
```
With my annotations:
```
/* eslint-env jquery */

(function () {
    const form = document.querySelector('#search-form'); //GC comment: queries HTML for the form
    const searchField = document.querySelector('#search-keyword'); //GC comment: queries for the search field
    let searchedForText; //GC comment: used to store the search term
    const responseContainer = document.querySelector('#response-container'); //GC comment: queries the response container, which is the main section of the html.

    form.addEventListener('submit', function (e) { //GC comment: waits for the submit click event
        e.preventDefault(); //GC comment: tells browser to prevent default actions.
        responseContainer.innerHTML = ''; //GC comment: clears the page on every submit click.
        searchedForText = searchField.value; //GC comment: stores the search term.


		function addImage(data) { //GC comment: Our addImage function after fetch is successful from unsplash.
		    let htmlContent = ''; //GC comment: starting with empty string.
		    const firstImage = data.results[0]; //GC comment: we're only showing the first returned result image.

		    if (firstImage) {  //GC comment: checks if we have a first image.
		        htmlContent =  //GC comment: We'll be using the figure element to display the image. The caption is example: joker by Will Smith, 1839423 likes.
		        `<figure>
		    		<img src="${firstImage.urls.small}" alt="${searchedForText}">
		    		<figcaption>${searchedForText} by ${firstImage.user.name}, ${firstImage.likes} likes</figcaption>
		    	</figure>`;
		    } else { //GC comment: Will default to the error-no-image css.
		        htmlContent = '<div class="error-no-image">No images available</div>'
		    }

		    responseContainer.insertAdjacentHTML('afterbegin', htmlContent); //GC comment: Using insertAdjacentHTML, after begin param to modify the HTML.
		}

        function addArticles(articles) { //GC comment: Our addArticles function after fetch is successful from ny times.
        	let htmlContent = ''; //GC comment: starting with blank string.

        	if (articles.response.docs.length > 0) { //GC comment: check if we have at least one document.
        		htmlContent =  //GC comment: All articles will be in a list element, using array methods of map and join.
        		'<ul>\n' +
        			articles.response.docs.map(articlesNYTimes => 
        				`<li class="article">
        					<h2><a href="${articlesNYTimes.web_url}" target="_blank">${articlesNYTimes.headline.main}</a></h2>
        					<p>${articlesNYTimes.snippet}</p>
        				</li>`)
        			.join('\n') +
        		'\n</ul>';
        	} else { //GC comment: Will default to this css class error-no-articles if things fail.
        		htmlContent = '<div class="error-no-articles">No articles available</div>';
        	}

        	responseContainer.insertAdjacentHTML('beforeend', htmlContent); //GC comment: using insert adjacent html with param before end to modify the html.
        }

        function requestError(e, part) { //GC comment: Here's the error handler. It simply modifies the html to show users there was a problem with either the article or image.
        	console.log(e);
        	responseContainer.insertAdjacentHTML('afterbegin', `<p class="network-warning error-no-${part}">Oh no! There was an error making a request for the ${part}.</p>`);
        }

        fetch(`https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`, { //GC comment: This is how we fetch data from unsplash with the header for API key.
        	headers: {
        		'Authorization': 'Client-ID 611dc2767c8fcc33f0013f0c03634373b5c864669a77f37b7133f9377bf52f8e'
        	}
        }).then(response => response.json()) //GC comment: response.json() is used to retrieve the JSON data
        .then(addImage) //GC comment: if successful run addImage function
        .catch(e => requestError(e, 'image')); //GC comment: if fail here's the failure handler. image string is simply passed in.

        fetch(`http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=e35e661abcd54895b4b2842465fb67a0`) //GC comment: This is how we fetch data from ny times.
        .then(response => response.json()) //GC comment: need to retrieve the JSON data
        .then(addArticles) //GC comment: if successful runs the addArticle function.
        .catch(e => requestError(e, 'articles')); //GC comment: if fail here's the failure handler. We're passing in a string for articles.

    });
})();
```

- - -
Next up: [Fetch Outro](ND024_Part3_Lesson03_09.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
