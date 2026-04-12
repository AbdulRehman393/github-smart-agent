# collection = single "variable" used to store multiple values e.g., List, Set , Tuple and Dictionaries
# You can use index operator with collections much like you can use with string
# List = [] ordered and changeable. Duplicates OK

fruits= ["apple", "orange", "banana", "coconut","banana"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])  # if I want my fruits backward

# methods that we can use with collections
print(dir(fruits))   # if We scroll this to the end, We have a bunch of different methods that
                     # this list can perform
# if you want description of all these methods there is a help function
print(help(fruits))

# if you need the length of how many elements are within a collection
print(len(fruits))

# using in operator we can find a value is within a collection
print("apple" in fruits) # It will return true if that value is in collection else false.

# We can change one of the these values, once we create our list.
fruits[1] = "pineapple"

# We can append an element to our list, to add an element to the end of the list
fruits.append("watermelon")

# To remove an element
print(fruits.remove("apple"))

# using the insert method we can insert a value t a given index
fruits.insert(0, "guava")

# the sort method will sort a list, these will be in alphabetical order
fruits.sort()
print(fruits)

# to reverse a list , we will use reverse method, these are reversed placed on the order in which we
# placed them
fruits.reverse()
print(fruits)
# if you would like reverse alphabetical order , you can first sort and then reverse

# to clear a list , you can use a clear method
# fruits.clear()
# print(fruits)

# we can return the index of a value
print(fruits.index("banana"))
# if we don't find a value , it will give us error that this value is not in list

# You could count the amount of times that a value is found within a list
# because duplicates are okay
print(fruits.count("banana"))

# We can also remove the last element by using the pop method
fruits.pop()


# You can iterate over them through the for loop

for fruit in fruits:
    print(fruit)

