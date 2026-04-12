# How to connect to an API using Python
from http.client import responses

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)      # the .get method is going to return response object

    if response.status_code == 200:
       pokemon_data = response.json()     #using this method will convert to a python dictionary, will consist of key-value pairs much like a json
       return pokemon_data                # returning our dictionary
    else:
        print(f"Failed to retrieve data {response.status_code}")



pokemon_name = input("Enter pokemon:")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}.capitalize()")
    print(f"Id:{pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")