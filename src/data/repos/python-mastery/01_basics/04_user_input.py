

name = input("Enter your name: ")
age = input("Enter your age: ")

# When we accept user input, it always of string data type
# age = age + 1      Here , we will get type error , We can only concatenate Strings, not integers

# I need to type cast it to int or float to do any sort of arithmetic operations on it
age = int(age)
age = age + 1

gpa = float(input("What is your gpa?"))

print(f"Hello {name}")
print(f"You are {age} years old")
print(f"Your gpa is {gpa}")