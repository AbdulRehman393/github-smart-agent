# Tuple ()       = immutable, faster

# They are similar to list but instead of closing all of our elements with a set of straight brackets
# We will enclose them with a set of parentheses, where it differs is that tuples are immutable
# meaning we cannot change the  elements once the tuple is created , but this makes them faster
# it's faster to access the elements of a tuple rather than a list, We cannot even append and remove elements

fruits = ("Apple","Mango","Banana")

for fruit in fruits:
    print(fruit)