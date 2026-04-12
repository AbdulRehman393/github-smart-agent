import requests

# Append the query params to the URL string
response = requests.get("http://350.5th-ave.com/unit/243?floor=77&elevator=True")
print(response.url)


# Use the params argument to add query parameters

# Create dictionary
query_params = {'floor': 77, 'elevator': True}
# Pass the dictionary using the 'params' argument
response = requests.get('https//350.5th-ave.com/unit/243', params=query_params)
print(response.url)




