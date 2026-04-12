# while loop = execute some code WHILE some condition remains true
# while loop tends to be better if you need to execute something possibly infinite
# amount of times such as when you are accepting user input for example.

name = input("Enter your name: ")
while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")



age =  int(input("Enter you age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")



food = input("Enter a food you like (q to quit): ").lower()

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ").lower()

print("bye")


num = int(input("Enter a number between 1 and 10: "))

while num <  1 or num  > 10:
    print("You entered a number out of range")
    num = int(input("Enter a number between 1 and 10: "))

print(f"You entered {num}")