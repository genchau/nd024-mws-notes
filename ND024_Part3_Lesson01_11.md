# Lesson 1.11 Setting a Request Header

unsplash:
```
function addImage() {
  let htmlContent = '';
  const data = JSON.parse(this.responseText);
  
  if (data && data.results && data.results[0]) {
    const firstImage = data.results[0];
    htmlContent = `<figure>
      <img src="${firstImage.urls.regular}" alt="${searchedForText}">
      <figcaption>${searchedForText} by ${firstImage.user.name}</figcaption>
    </figure>`;
  } else {
    htmlContent = '<div class="error-no-image">No images available</div>';
  }
  
  responseContainer.insertAdjacentHTML('afterbegin', htmlContent);
}

const searchedForText = 'hippos';
const unsplashRequest = new XMLHttpRequest();

unsplashRequest.open('GET', `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`);
unsplashRequest.onload = addImage;
unsplashRequest.setRequestHeader('Authorization', 'Client-ID <your-client-id>');
unsplashRequest.send();

function addImage(){
}
```

Use `debugger` in our JavaScript to pause the script during execution.

new york times:
```
function addArticles () {
  let htmlContent = '';
  const data = JSON.parse(this.responseText);
  
  if (data.response && data.response.docs && data.response.docs.length > 1) {
    htmlContent = '<ul>' + data.response.docs.map(article => `<li class="article">
      <h2><a href="${article.web_url}">${article.headline.main}</a></h2>
      <p>${article.snippet}</p>
      </li>`;
    ).join('') + '</ul>';
  } else {
    htmlContent = '<div class="error-no-articles">No articles available</div>'
  }
  
  responseContainer.insertAdjacentHTML('beforehand'), htmlContent);
}

const articleRequest = new XMLHttpRequest();
articleRequest.onload = addArticles;
articleRequest.open('GET', `http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=<your-API-key-goes-here>`);
articleRequest.send();
```

- - -
Next up: [Project Final Walkthrough](ND024_Part3_Lesson01_12.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
