# Define a function called concat
def concat(*args):
  """Concatenates multiple string arguments with spaces between them."""

  result = ""

  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))