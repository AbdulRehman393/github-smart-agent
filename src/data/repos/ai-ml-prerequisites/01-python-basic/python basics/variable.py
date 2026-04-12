#variable = A reusable container for a value (string, integer, float, boolean)
#           The variable behaves as if it was the value that it contains

full_name = "Abdul Rehman"              #String is a series of characters
age = 22                                #Integers are whole numbers
gpa = 3.2                               #Floats are numbers but they contain a decimal
is_student = True                       #Booleans are either true or false, true and false need to be capitalized

print(f"Hello {full_name}")
print(f"You are {age} years old.")
print(f"Your gpa is {gpa}")
print(f"Are you a student?: {is_student}")

# We usually use Boolean in If Statement
if is_student:
    print("You are a student")
else:
    print("You are not a student")