# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of the two values based on a condition
#                          X if condition else Y
from time import monotonic_ns

num = 5

print("Positive" if num > 0 else "Negative")

value = 5
result = "Even" if value % 2 == 0 else "Odd"

print(f"The value is: {result}")

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(f"Maximum Number is {max_num}")
print(f"Minimum Number is {min_num}")

age =  16
age = "Adult" if age >= 18 else "Child"

print(f"You are {age}")

temperature = 18
weather = "Hot" if temperature > 20 else "Cold"

print(f"It's {weather} today.")

user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)

online_status = False
print("Online" if online_status else "Offline")