# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates allowed
# few examples of key value pairs could be an ID and a name, an item and a price etc.

capitals = {"Pakistan": "Islamabad",
            "India": "Delhi",
            "China": "Beijing",
            "USA": "Washington D.C.",
            "Russia":"Moscow"}

# If you would like to see all the different attributes and methods of a dictionary, we can use the dir function
print(dir(capitals))

# If you would like an in-depth description of all these attributes and methods you can use the help function
print(help(capitals))

# few methods of dictionary

# checking how many key-value pairs in our dictionary
print(len(capitals))

# to get one of the values from a dictionary
print(capitals.get("USA"))
print(capitals.get("Japan"))  # if python doesn't find a key, it will return us None.

# you can check if a key is in our dictionary or not
if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# Let's update our dictionary
capitals.update({"Germany": "Berlin"})
capitals.update({"India": "New Delhi"})

# To remove a key value pair, you can use a pop method
capitals.pop("China")

# You can remove the latest key-value pair within a dictionary by using the following method
capitals.popitem()

# to clear the dictionary
#capitals.clear()

# to get all the keys within our dictionary , but not the values there is keys method
keys = capitals.keys()    # technically, keys is a dict_keys object.
                          # It behaves like a list in loops, but it is not a list.
                          # keys = capitals.keys()  # keys is a dict_keys object
                          # for key in keys:
                          # print(key)
print(keys)

for key in capitals.keys():
    print(key)


# To get all the values within our dictionary, there is a value method
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

# items() method returns a dictionary object which resembles a 2d list of tuples
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")



