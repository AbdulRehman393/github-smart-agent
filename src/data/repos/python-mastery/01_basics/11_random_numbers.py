import random

# random module gives us access to a lot of useful methods involving random numbers
# for a comprehensive list, we can use the help function
print(help(random))

# for a random whole integer
# number = random.randint(1, 20)     # it will generate number between 1 and 20, 1 and 20 both are included

low = 1
high = 100

number = random.randint(low, high)

print(number)

# if you need a random floating point number
value = random.random()     # this will return a floating point number between 0 and 1

# you can pick a random choice from a sequence
options = ("rock","paper","scissors")
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

# using a shuffle method, I can shuffle a sequence
random.shuffle(cards)

print(cards)