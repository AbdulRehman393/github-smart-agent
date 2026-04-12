# Lambda functions with iterables
# map() applies a function to all elements in an iterable


names  = ["ali","ahmad","bilal"]
# Apply a lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)

# Convert to a List
print(list(capitalize))