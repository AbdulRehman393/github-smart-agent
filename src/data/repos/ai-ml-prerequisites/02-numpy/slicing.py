import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                [9, 10, 11, 12],
               [13, 14, 15, 16]])

# for array slicing we will be using subscript operator, here is our slicing expression, array[start:end:step]
# start , end , step all parts are optional
# string slicing works the same way as array slicing in Python, including the start:end:step pattern.

# accessing  row
print(array[0])     # first row
print(array[1])     # second row
print(array[2])     # third row
print(array[3])     # fourth row
#print(array[4])    # Error , out of bound
# We can also use negative indexing
print(array[-1])    # last row
print(array[-2])    # second last row

print()

# starting index at which element you would like to start

# We can also select a range, we need both a start and an ending index
print(array[0:3])     # ending index is exclusive    # it will print first three rows
print()
print(array[1:4])     # It will print the rows from index 1 to index 3 means rows from second to fourth
print()
print(array[1:])                     # If you would like to select everything till the end you could omit the second number
print()
print(array[0:4:2])    # let's select every second row starting with the first row, give me every second row, we will be
                       # counting by 2
print()
# if we are selecting all rows, you can omit the start and the end but here we will still need two columns
print(array[::2])

print(array[::-1])   # this will return all the rows reversed.
print()

print(array[::-2])   # now, we are selecting every second row in reversed order

# So , this was row selection, now we will get into column selection
print()
# while accessing our 2D array, we'll need two indexes,
print(array[0,0])  # first index is for our row and the second index is for our column


print(array[:,0])      # if we would like to select all rows and access column 0
print(array[:,1])
print(array[:,2])
print(array[:,3])
print()
print(array[:,-1])    # this will return the last column
print(array[:,-2])    # this will return the second last column

#
print(array)