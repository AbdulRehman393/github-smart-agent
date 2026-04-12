import requests

# Headers with requests

# Adding headers to a request
response = requests.get(
    'https://api.datacamp.com',
     headers = {'accept':'application/json'}
)

# Reading response headers
print(response.headers['content-type'])

print("-----------------")

print(response.headers.get('content-type'))