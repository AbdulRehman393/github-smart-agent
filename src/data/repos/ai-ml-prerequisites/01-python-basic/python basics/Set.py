#Set {}          = mutable (add/remove) but we cannot replace any of the element with in it, unordered, We cannot
#                  access them by index
#                  No duplicates, best for membership testing


fruits = {"apple","mango","banana"}

# Let's add element
fruits.add("pineapple")

# Let's remove element
fruits.remove("banana")

# We cannot pop , We cannot work with indexes

# I am going to print the elements of my set,the sets are unordered the order is going to change each time
# during its first run we will have different order , during 2nd and other time we print , it will have
# different order

for fruit in fruits:
    print(fruit, end = " ")

print()

#Let's clear our set
fruits.clear()

print(fruits)

# Sets don't allow duplicate e.g:
cars = {"Ferrari","BMW","Mercedes","BMW"}
print(cars)

# Sets are good for membership testing, checking to see if there is a given value within your set

if "Ferrari" in cars:
    print("Ferrari was found")
else:
    print("Ferrari was not found")


# We even could accept user input
items = {'bat','guitar','vacuum-cleaner'}

item = input("Enter an item to search for: ")

if item in items:
    print(f"{item} was found")
else:
    print(f"{item} was not found")

