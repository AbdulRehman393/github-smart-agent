
# A 2-Dimensional list is just a list made up of lists . 2dlist = [list1, list2, list3]
# It's very useful if you ever need a grid or Matrix of data kind of like an Excel spreadsheet
# 2-d collection is not limited to lists, it can be tuples, sets, and dictionaries.
# 2-d tuple, tuple just made up of tuples.


fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]


# It kind of represents a grid or Matrix with rows and columns. each individual list
# resemble a row, each element resembles a column

print(groceries[0])   # It will return the entire first row
print(groceries[1])   # It will return the entire second row
print(groceries[2])   # It will return the entire third row
#print(groceries[3])   # list index out of range, because we only have three rows



# So, one of the element found within one of the rows , you would need two indexes
print(groceries[0][0])     # apple   # It's kind of like coordinates
print(groceries[0][1])
print(groceries[0][2])
print(groceries[0][3])
#print(groceries[0][4])    # error: index out of range,  because we only have three elements in this row
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])

print("---------------------")
# We can also make 2_d list this
Groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# Using a single for loop would iterate over the rows but to also iterate over the
# elements found within each row , we would use a nested loop
for collection in Groceries:
    print(collection)

# if you ever need to iterate over the elements within each row  of a 2d list, you can use
# nested loops

for collection in Groceries:
    for food in collection:
        print(food, end = " ")
    print()

print("---------------")

# list of tuples
items = [("apple", "orange", "banana", "coconut"),
         ("celery", "carrots", "potatoes"),
         ("chicken", "fish", "turkey")]

# 2-d Tuples
foods = (("apple", "orange", "banana", "coconut"),
         ("celery", "carrots", "potatoes"),
         ("chicken", "fish", "turkey"))

# You could make a tuple made up of Sets
products = ({"apple", "orange", "banana", "coconut"},
         {"celery", "carrots", "potatoes"},
         {"chicken", "fish", "turkey"})

