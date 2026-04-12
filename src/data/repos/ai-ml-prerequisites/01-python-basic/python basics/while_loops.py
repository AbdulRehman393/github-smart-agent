# While Loop = used to repeat a block of code as long as a condition remains 'True'
#              we re-check the condition at the end of the loop

name = input("What is you name? ")

while name == "":
    print("Enter your name:  ")

age = int(input("Enter you age: "))

while age < 0:
    print("Age can't be less than 0")
    print("Enter you age")

print(f"Hello {name}!")
print(f"You are {age} years old!")