import requests

# Each verb has it's own method in the requests package
# Use the data argument to pass data to a POST or PUT request.


# GET = Retrieve a resource
reponse = requests.get("http://350.5th-ave.com/unit/243")

# POST = Create a resource
response = requests.post("http://350.5th-ave.com/unit/243", data={"key": "value"})

# PUT = Update an existing resource
response = requests.put("http://350.5th-ave.com/unit/243", data={"key": "value"})

# DELETE = Remove a resource
response = requests.delete("http://350.5th-ave.com/unit/243")




