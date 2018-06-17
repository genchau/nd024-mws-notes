# Lesson 7.6 GET and POST

### Form methods: GET and POST
In the last lesson, I mentioned that GET is only one of many HTTP verbs, or methods.

When a browser submits a form via GET, it puts all of the form fields into the URI that it sends to the server. These are sent as a query, in the request path — just like search engines do. They're all jammed together into a single line. Since they're in the URI, the user can bookmark the resulting page, reload it, and so forth.

This is fine for search engine queries, but it's not quite what we would want for (say) a form that adds an item to your shopping cart on an e-commerce site, or posts a new message on a comments board. GET methods are good for search forms and other actions that are intended to look something up or ask the server for a copy of some resource. But GET is not recommended for actions that are intended to alter or create a resource. For this sort of action, HTTP has a different verb, POST.

### Idempotence
Vocabulary word of the day: idempotent. An action is idempotent if doing it twice (or more) produces the same result as doing it once. "Show me the search results for 'polar bear'" is an idempotent action, because doing it a second time just shows you the same results. "Add a polar bear to my shopping cart" is not, because if you do it twice, you end up with two polar bears.

POST requests are not idempotent. If you've ever seen a warning from your browser asking you if you really mean to resubmit a form, what it's really asking is if you want to do a non-idempotent action a second time.

<img src="https://d17h27t6h515a5.cloudfront.net/topher/2016/October/580f75a6_cow/cow.png">

When I tell my browser to reload a page that came from a POST request, it displays a "Confirm Form Resubmission" dialog to make sure I'm not accidentally resubmitting a form.

(Important note if you're ever asked about this in a job interview: idempotent is pronounced like "eye-dem-poe-tent", or rhyming with "Hide 'em, Joe Tent" — not like "id impotent".)

Adding zero to a number is idempotent, since you can add zero as many times as you want and the original number is unchanged. Adding five to a number is not idempotent, because if you do it twice you'll have added ten. Setting a variable to the value 5 is idempotent: doing it twice is the same as doing it once. Looking up an entry in a dictionary doesn't alter anything, so it's idempotent.

### Exercise: Be a server and receive a POST request
Here's a piece of HTML with a form in it that is submitted via POST:
```
<!DOCTYPE html>
<title>Testing POST requests</title>
<form action="http://localhost:9999/" method="POST">
  <label>Magic input:
    <input type="text" name="magic" value="mystery">
  </label>
  <br>
  <label>Secret input:
     <input type="text" name="secret" value="spooky">
  </label>
  <br>
  <button type="submit">Do a thing!</button>
</form>
```
This form is in your exercises directory as Lesson-2/2_HTMLForms/PostForm.html. Open it up in your browser. You should see a form. Don't submit that form just yet. First, open up a terminal and use ncat -l 9999 to listen on port 9999. Then type some words into the form fields in your browser, and submit the form. You should see an HTTP request in your terminal. Take a careful look at this request!

The first three are true! Try changing POST to GET in the form and restarting ncat, and see how this affects the request you see when you submit the form.

When a browser submits a form as a POST request, it doesn't encode the form data in the URI path, the way it does with a GET request. Instead, it sends the form data in the request body, underneath the headers. The request also includes Content-Type and Content-Length headers, which we've previously only seen on HTTP responses.

By the way, the names of HTTP headers are case-insensitive. So there's no difference between writing Content-Length or content-length or even ConTent-LeNgTh … except, of course, that humans will read your code and be confused by that last one.

- - -
Next up: [A server for POST](ND024_Part4_Lesson07_07.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
