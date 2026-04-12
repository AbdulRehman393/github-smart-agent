# requests library = Many powerful buil-in features
#          = Easier to use

import requests
api = "http://api.music-catalog.com/"

response = requests.get(api)
print(response.text)