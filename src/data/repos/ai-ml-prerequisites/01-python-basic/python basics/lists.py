# List []        = mutable, most flexible


fruits = ["apple","orange","coconut"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits)

fruits[0] = "pineapple"
fruits[2] = "mango"

#So, this line of code effectively adds "honda" to the beginning of your cars list,
# shifting all existing elements one position to the right.
fruits.insert(1,"grapes")
print(fruits)

# We can append elements using append method
fruits.append("strawberry")

# We can remove elements
fruits.remove("orange")

# We can pop meaning we can remove an element at a given index.
fruits.pop(1)

# We could use for loop to iterate each element in a list
for fruit in fruits:
    print(fruit, end =" ")    # So, here we are ending each character with a space rather than a new line

print()

# In order to clear you list
fruits.clear()

print(fruits)