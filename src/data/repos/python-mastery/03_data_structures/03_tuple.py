# Tuple = ()  ordered and immutable , Duplicated Ok, generally faster than list because python knows it
# cannot change so memory access is optimized.
# Immutable means you cannot change , add or remove element once it's created.


fruits = ("apple", "orange", "banana", "coconut","coconut")

# To display all the attributes and methods of a set
print(dir(fruits))

# for in-depth description of these methods
print(help(fruits))

# To define the length of our set , we can use the length function
print(len(fruits))

# We can use the in operator to find if a value is find within the set
print("orange" in fruits)

# There are not many methods for tuples as lists
# So We have only methods to access to i.e., index and count

# to find the index of that element
print(fruits.index("apple"))

# to count how many times the elements exist in our collection
fruits.count("coconut")

print(fruits)

for fruit in fruits:
    print(fruit, end = " ")
