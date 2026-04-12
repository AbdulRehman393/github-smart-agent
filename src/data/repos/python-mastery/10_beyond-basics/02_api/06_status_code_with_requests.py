import requests

# Accessing the status code
response = requests.get('https://api.datacamp.com/users/12')
print(response.status_code == 200)

# Looking up status code with requests.codes
response = requests.get('https://api.datacamp.com/this/is/the/wrong/path')
print(response.status_code == requests.codes.not_found)