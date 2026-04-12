# Lambda functions

# lambda keyword
# Represents an anonymous functions which doesn't require a name or need to be saved as a variable


# Syntax = lambda arguments: expression
# Convention is to use x for a single argument
# The expression is the equivalent of the function body
# No return statement is required

# Can be stored as a variable

# Get the average
(lambda x: sum(x) / len(x))([3, 6, 9])

# Print the average 
print((lambda x: sum(x) / len(x))([3, 6, 9]))

# Store lambda function as a variable
average = lambda x: sum(x)/len(x)

# Call the average function
print(average([3, 6, 9]))

# Multiple parameters

# Lambda function with two arguments
power = lambda x, y: x**y

# Raise 2 to the power of 3
print(power(2,3))