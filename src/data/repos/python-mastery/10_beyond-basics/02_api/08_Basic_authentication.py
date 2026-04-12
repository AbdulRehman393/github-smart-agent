import requests


# Basic authentication with the requests package
# This will automatically add a Basic Authentication header before sending the request
requests.get('http://api.music-catalog.com', auth=('username','password'))