# Modules are python scripts that are
# -> Files ending with py
# -> contains functions and attributes
# -> Can contain other modules
# -> Help us avoid rewriting code that already exist!

# There are around 200 built-in modules

# os module
# Used for interacting with our operating system
# Check the current directory
# List available files
# Access environmental variables and many more

# string module
# provides predefined character sets that simplify common text processing tasks.

import os

# Checking the type confirming that 'os' is a module.
print(type(os))

# once the module is imported , to check what's inside
# the easiest approach is to check the documentation
# we can also use the built-in help() function,output can be quite lengthy

# print(help(os))

# Using an os function
print(os.getcwd())             # retrieves the current working directory.


# Assign to a variable, useful if we need to reference the directory later such as when reading multiple files
# from the same location.

work_dir = os.getcwd()

# Changing directory
os.chdir(r"C:\Users\rehman.saeed\Desktop\Courses\Intermediate Python for Developers\notes")

print(os.getcwd())

os.chdir("C:/Users/rehman.saeed/Desktop/Courses/Intermediate Python for Developers/code")

print(os.getcwd())

# Module attributes
# -> attributes return values
# -> Functions perform tasks
# -> Don't use parentheses with attributes

# Get the local environment
print(os.environ)


# String module

import string

print(string.ascii_lowercase)            # returns all lowercase letters
print(string.digits)                     # returns numbers from 0 to 9
print(string.punctuation)                # returns all special characters

# These attributes are especially handy for validating user input.