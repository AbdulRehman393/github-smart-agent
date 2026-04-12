import requests

# Exercise No. 01

response = requests.get('http://localhost:3000/lyrics')



#Check if the server responded successfully with the 200 status code.
# Check the response status code
if (response.status_code == 200):
  print('The server responded succesfully!')

# Find out what content-types the server can respond with by printing out 
# the response accept header.
response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers['accept'])


# Add an accept header to the request so the server returns JSON formatted data, 
# then print the response text attribute.

# Set the content type to application/json
headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)


# Exercise No. 02
# Add an accept header to request a response in the application/xml content-type from the server.
# Check if the server did not accept the request using the relevant status code.
# Print out a list of accepted content types from the server response.
# Add a header to use in the request

headers = {'accept':'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)
