# function = A block of reusable code
#            place () after the function name to invoke it
# return = statement used to end a function
#          and send a result back to a caller
# A function must be defined before it is called.

# Positional arguments are arguments where:
#
# Order matters
#
# Values are assigned based on position


# Example 1

def happy_birthday(name, age):      # You need matching set of parameters as arguments, the order does matter
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Bilal", 20)   # Any data you send a function are known as arguments
happy_birthday("Jawad", 30)

# Example 2

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Sajad", 42.50, "01/01")

# Example 3

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z


print(add(1,2))
print(subtract(4,2))
print(multiply(2,3))
print(divide(9,3))

# Example 4

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("jawad", "raza")
print(full_name)


