# typecasting =  The process of converting a value of one data type to another
#                (string, integer, float, boolean)
#                Explicit vs Implicit

# The user input is always a string , so we need to convert it to a type according to our need.

# ------------------ Explicit typecasting -----------------------------
# When manually converting a value or variable into a different datatype

name = "Abdul"
age = 21
gpa = 3.2
student = False

print(type(name))     # type() function tells us the datatype of the variable
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(type(age))
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(type(student))

# num ---> bool
age = bool(age)
print(age)       # when converting a number to boolean if that number is anything but zero it will be true

# Casting something to boolean will be useful in this way, if We ask a user to enter a name, I need to check to see
# if they enter in something, if it's true , it means they have entered something, if false it means, they have not
# entered anything

name = bool(name)
print(name)     # This is true , but if this was an empty string it would be false like this name = ""
                # even the space like this name = " "   registers as true


#  ------------------------ Implicit typecasting -------------------------------
# When a value or variable is converted into a different data type automatically

x = 2
y = 2.0

x = x / y   # x is implicitly converted to a float during type casting

print(x)

#isinstance(x, int): This checks if x is an integer or a subtype of an integer
# You can even check against multiple types

price = "hello"
if isinstance(price, (int, float)):
    print("Valid numeric value for price.")
else:

    print("Invalid numeric type for price.")
