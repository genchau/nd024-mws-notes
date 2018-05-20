# Lesson 1.12 Project Final Walkthrough

Here's my implementation of the XHR for the AJAX project.

```
(function () {
    const form = document.querySelector('#search-form'); //GC comment: Finds the form, so we can add event listener for the submit button.
    const searchField = document.querySelector('#search-keyword'); //GC comment: Finds the location of the input text field.
    let searchedForText; //GC comment: Will be used to store the string value from the search form. Then be used as the API parameter and request data from unsplash and ny times on the search word.
    const responseContainer = document.querySelector('#response-container'); //GC comment: The response-container is pretty much the body of index.html.

    form.addEventListener('submit', function (e) { //GC comment: Looking for the submit event on form.
        e.preventDefault(); //GC comment: I see this everywhere, this is to prevent default behavior from the browswer and to run our code instead.
        responseContainer.innerHTML = ''; //GC comment: We want to first clear the response container. So when we start a new search it will present a new page.
        searchedForText = searchField.value; //GC comment: After submit button we are able to retrieve the search terms in form field.



		function addImage(){ //GC comment: Our onload function, when response is received from unsplash.
			let htmlContent = ''; //GC comment: Starting with a blank string.
			const data = JSON.parse(this.responseText); //GC comment: this.responseText is the response from unsplash. We'll parse the JSON data and store it into data const.

			if (data && data.results && data.results[0]) { //GC comment: this if statement checks whether images do exist in this search query.
				const firstImage = data.results[0]; //GC comment: data.results returns a couple of results up to 10, we are only interested in displaying the first picture.
				htmlContent = `<figure> 
					<img src="${firstImage.urls.regular}" alt="${searchedForText}">
					<figcaption>${searchedForText} by ${firstImage.user.name}, ${firstImage.likes} likes</figcaption>
				</figure>`; //GC comment: This writes the html code using figure element for the first picture from unsplash. The caption will show example, "Bears by Thomas Edison, 33 likes."
			} else {
				htmlContent == '<div class="error-no-image">No images available</div>'; //GC comment: If no image received, we'll default to this message. There's a class in CSS for this, which will insert a default error image.
			}

			responseContainer.insertAdjacentHTML('afterbegin', htmlContent); //GC comment: I like this code. So the method insertAdjacentHTML gives us the ability to inject HTML at 4 possible options. We have beforebegin, afterbegin, beforeend, afterend. We're choosing to add this on top so we are using afterbegin.
		}

		
		function addArticles () { //GC comment: Our onload function, when response is received from NY times.
			let htmlContent = ''; //GC comment: Starting with a blank string.
			const data = JSON.parse(this.responseText); //GC comment: this.responseText is the response from NY Times. We'll parse the JSON data and store it into data const.

			if (data.response && data.response.docs && data.response.docs.length > 1) { //GC comment: checks make sure we have content
				htmlContent = '<ul><li class="article">GenChau was here.</li>'+ 
					data.response.docs.map(artNYTimes => `<li class="article">
						<h2><a href="${artNYTimes.web_url}" target="_blank">${artNYTimes.headline.main}</a></h2>
						<p>${artNYTimes.snippet}</p>
					</li>`
				).join('') + '<li class="article"><h2><a>GenChau was here.</a></h2><p>Yup still here.</p></li></ul>';
					//GC comment: a couple of things going on here. 
					//The .map() function applies an operation to each element of an array. And create a new array with those values stored.
					//The .join() function joins all the elements in the array and creates one long string. The parameter determines how they are separated. It defaults to (,).
					//So this creates an unordered list. With each article being a list item. I added 2 li elements for my own experiment with the label GenChau was here.
					//data.response.docs provide a couple of things. We are using web_url, headline.main, snippet. The class article determines the looks of the list element.
				console.log("GC start", htmlContent);
			} else {
				htmlContent = '<div class="error-no-articles">No articles available</div>'; //GC comment: If no articles this will display.
			}

			responseContainer.insertAdjacentHTML('beforeend', htmlContent); //GC comment: We're adding the articles after the picture, so beforeend works perfect.
		}

        // Searches UNSPLASH.com for the image and adds it to the web page.
	    const imgRequest = new XMLHttpRequest(); //GC comment: creating the XHR.
		imgRequest.onload = addImage; //GC comment: defining onload for XHR.
		imgRequest.onerror = function (err) { //GC comment: defining onerror for XHR.
			requestError(err,'image'); //GC comment: not sure what this does.
		};
		imgRequest.open('GET', `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`); //GC comment: This is how we setup the XHR.
		imgRequest.setRequestHeader('Authorization', 'Client-ID 49fafd545b4229485140ae2c2a20916dae8a6def2684760c7010044e24104cbe'); //GC comment: Unsplash requires a header for the API key.
		imgRequest.send(); //GC comment: This is the last step to XHR request, sending.

		// Searches NYTIMES.com for an article and adds it to the web page.
		const articleRequest = new XMLHttpRequest(); //GC comment: creating the XHR object.
		articleRequest.onload = addArticles; //GC comment: defining onload, but didn't define onerror.
		articleRequest.open('GET', `http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=e35e661abcd54895b4b2842465fb67a0`); //GC comment: setting up the XHR.
		articleRequest.send(); //GC comment: Sending the XHR.

    });
})();

```

- - -
Next up: [XHR Recap](ND024_Part3_Lesson01_13.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
