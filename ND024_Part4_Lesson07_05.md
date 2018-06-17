# Lesson 7.5 HTML and forms

### Exercise: HTML and forms
Most of the time, query parameters don't get into a URL by the user typing them out into the browser. Query parameters often come from a user submitting an HTML form. So dust off your HTML knowledge and let's take a look at a form that gets submitted to a server.

If you need a refresher on HTML forms, take a look at the [MDN introduction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms) (gentle) or the [W3C standard reference](https://www.w3.org/TR/2011/WD-html5-20110525/forms.html) (more advanced).

Here's a piece of HTML that contains a form:
```
<!DOCTYPE html>
<title>Login Page</title>
<form action="http://localhost:8000/" method="GET">
<label>Username:
  <input type="text" name="username">
</label>
<br>
<label>Password:
  <input type="password" name="pw">
</label>
<br>
<button type=submit>Log in!</button>
```

This HTML is also in the exercises directory, under Lesson-2/2_HTMLForms/LoginPage.html. Open it up in your browser.

Before pressing the submit button, start up the echo server again on port 8000 so you can see the results of submitting the form.

The second one should happen. The form inputs, with the names username and pw, become query parameters to the echo server.

### Exercise: Form up for action
Let's do another example! This HTML form has a pull-down menu with four options.
```
<!DOCTYPE html>
<title>Search wizardry!</title>
<form action="http://www.google.com/search" method=GET>
  <label>Search term:
    <input type="text" name="q">
  </label>
  <br>
  <label>Corpus:
    <select name="tbm">
      <option selected value="">Regular</option>
      <option value="isch">Images</option>
      <option value="bks">Books</option>
      <option value="nws">News</option>
    </select>
  </label>
  <br>
  <button type="submit">Go go!</button>
</form>
```
This form is in the HTML file SearchPage.html in the same directory. Open it up in your browser.

This form tells your browser to submit it to Google Search. The inputs in the form supply the q and tbm query parameters. (And if Google ever changes the way their search query parameters work, this example is going to be totally broken.)

Yes. The form action is the URI to which the form fields will be submitted.

- - -
Next up: [GET and POST](ND024_Part4_Lesson07_06.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
