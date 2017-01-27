===================
Facebook Token
===================

# Install
pip install facebooktoken

# Prepare your necessary varibles
1. Visit https://developers.facebook.com/tools/explorer/ and retrieve your short lived access token
2. Visit https://developers.facebook.com/apps/ and retreive your **APP ID** and **APP SECRET**

# Use your retrieved variables
```python
from facebooktoken import FacebookTokenRefresher

ftr = FacebookTokenRefresher(
	app_id=700797440051611,
	app_secret="485c92c8220b87badbe8f6bb5cd02be7",
	short_access_token="EAAJ9Xx55SZA0BAHmtrLHE3mvthKHW5mbBDXpkW6haI62UBevj8bZB1DWdoGKKtYhevbZBvtyOBHVdC7i3cFmxbO7PaUpjS2yovRO4BWPsNcmRqLzUCcAcU70dkl3WrdrqZAvG1jPWrdcnVJZANKiZCJmqf44vXfNU9kAzA9uqRM0FTzYZBk6P6QYlpQJ2LJiNQZD"
)

results = ftr.refresh()
```

### Results with status code 200
```json
{
	'access_token': 'EAAJ9Xx55SZA0BAKt4QswTRq7CFx0V4a9Ria1DrOlP36rtyJDUZAOmIdMaO7LZBTInDUaN7jnIgckxwy5FYApzqrpYYhbM5rsBSzx9TLZAdKrFk9BRDCw6foj07dEYkQhbPq8TYYeRYqDeLutgwB4hbVyYSes43AZD',
	'expires': u'5179894'
}
```

## On failure
By default on failure FacebookTokenRefresherException will get raised with the response data. You could if needed pass raise_exception=False when using the *refresh()* method.

### Results on failure with execption raised (Exception)
```python
facebooktoken.base.FacebookTokenRefresherException: {
    "error": {
        "message": "Invalid Client ID",
        "code": 101,
        "type": "OAuthException",
        "fbtrace_id": "EYsYDFbxVAm"
    }
}
```

### Results on failure without execption raised (Dictionary)
```json
{
    "error": {
        "message": "Invalid Client ID",
        "code": 101,
        "type": "OAuthException",
        "fbtrace_id": "DFbQ8aA94t5"
    }
}
```