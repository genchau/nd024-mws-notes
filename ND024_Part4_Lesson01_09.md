# Lesson 1.9 Sending data with a POST Request

So far, we have only been requesting the server to send data to us using the GET method. However, sometimes we might want the user to type in some data or upload a picture and send that to the server. This is where the POST method comes into play that we mentioned earlier. With a POST request, the request itself can also have a payload or body something we have already seen in responses, but not in requests. What exactly happens to the data once it has been sent to the server is up to the backend developer and is not in the scope of this course. It is, however, important to know that POST requests are potentially handled differently by proxies and the browser than GET requests. 


<img src="https://img.scoop.it/wma1fbyxPFqmw1kXjWW9zTl72eJkfbmt4t8yenImKBVvK0kTmF0xjctABnaLJIm9">

Have you ever seen one of these? This is what happens when the page we're currently looking at was the result of a POST request. If we try to reload such a website, the browser will prompt us to confirm this reload action as POST requests are allowed to be destructive operations and repeating it might be more destructive than we originally intended. That's why it is usually recommended for the backend developer to not respond to a POST request with a website but with a redirect to avoid this rather jarring behavior. For the user, the redirect is practically invisible but avoids the prompt on reload.

- - -
Next up: [From XHR to Fetch](ND024_Part4_Lesson01_10.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
