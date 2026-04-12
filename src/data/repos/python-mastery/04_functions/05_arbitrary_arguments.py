
# Arbitrary positional arguments = It allows functions to accept any number of positional, non-keyword arguments

# def averages(*args):
#   Function code remains the same
# Conventional naming = *args    , but any argument name will work.
# Allows a variety of uses while producing expected results!





def average(*args):
    """Find the mean in a sequence of values and round to two decimal places."""

    average_value = sum(args) / len(args)
    rounded_average = round(average_value, 2)
    return rounded_average

print(average(15, 29, 4, 13, 11, 8))


# Args creates a single iterable
# * = means combining all positional arguments, so it places them all inside a tuple.

# If we have lots of data across different structures, such as lists, and we want to find the average without needing to
# combine them into a single variable , we can place an asterisk in front of each argument.

# Calculating across multiple lists
print(average(*[15,29],*[4, 13], *[11, 8]))

print("--------------------------------")

# Arbitrary keyword arguments : **kwargs           
# the term generally used is kwargs, but word any will work.
# General syntax :  keyword = value     , This is equivalent to the key-value pairs in dictionary.

def average(**kwargs):
    """Find the mean in a sequence of values and round to two decimal places."""

    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average

print(average(a=15, b=29, c=4, d=13, e=11, f=8))

# The function combines the keyword argument names and values into a single dictionary and calculates the average of the values.

# We can also call average with a single keyword argument as a dictionary by using two asterisks in front
print(average(**{"a":15, "b":29, "c":4, "d":13, "e":11, "f":8}))

# Each key-value pair in the dictionary is mapped to a keyword argument and value!

# Calling average with three kwargs
print(average(**{"a":15, "b": 29}, **{"c":4, "d":13}, **{"e":11, "f":8}))