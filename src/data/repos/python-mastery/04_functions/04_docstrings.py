# Docstrings = It is a string(block of text) used to describe what a function does.
# Docstrings are displayed along with the additional information, when we use the help function.

# Accessing information,including the docstring
print(help(round))

print("---------------------------")
# Access only the docstring
print(round.__doc__)

# .__doc__ = "dunder-doc" attribute
print("---------------------------")


# One-line docstring
# Creating a docstring
def average(values):
    # One-line docstring
    """Find the mean in a sequence of values and round to two decimal places."""
    average_value = sum(values) /  len(values)
    rounded_average = round(average_value,2)
    return rounded_average

# Access our docstring
print(average.__doc__)

# Update a functions's docstring
average.__doc__ = "Calculate the mean of values in a data structure, rounding the result to 2 digits."

print(average.__doc__)

print("----------------------------------")

# Multi-line docstring = we use it to provide more information, which is useful if the function
# is more complex or has lots of arguments. 

def average(values):
    """
    Find the mean in a sequence of values and round to two decimal places.

    Args:
        values (list): A list of numeric values.
    
    Returns:
        rounded_average (float): The mean of values, rounded to two decimal places.
    """
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

# Calling help shows our full docstring, including the blank line formatting.
print(help(average))
