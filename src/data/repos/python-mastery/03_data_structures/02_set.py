# Set = {} unordered and mutable
# Elements cannot be accessed or modified by index
# Add / Remove allowed
# No duplicates
# Sets may work well if you are working with constants maybe colours for example
# you need to find if a color is within a set

fruits = {"apple","orange","banana","coconut","apple"}    # no duplicates are allowed
                                                          # output elements : apple, orange, banana, coconut
                                                          # it could be in any order

# To display all the attributes and methods of a set
print(dir(fruits))

# for in-depth description of these methods
print(help(fruits))

# To define the length of our set , we can use the length function
print(len(fruits))

# We can use the in operator to find if a value is find within the set
print("orange" in fruits)

# if I use the index operator of my set
# print(fruits[0])  # it will give me an error, we are not able to use indexing on a set and
                    # sets are unordered

# We cannot change the value of a set ,but we can add and remove elements
fruits.add("pineapple")

fruits.remove("apple")

fruits.pop()

#fruits.clear()

print(fruits) # As set is unordered if I will print it again, they will likely
              # be in a different order.

