import numpy as np


# simple python multidimensional list
# my_list = [[2,4,5,5],[3,5,2,5]]
# print(my_list[0][0])
# print(my_list[0][2])
#
# for x in my_list:
#     for y in x:
#         print(y, end = " ")
#     print()


#array = np.array('A')
#array = np.array(['A', 'B', 'C'])    # this is now a one dimensional array like a single row.
# array = np.array([['A', 'B', 'C'],    # this would form sort of two dimensional matrix. It's a 2D matrix. Sometimes people
#                  ['D', 'E', 'F'],     # refer it as a matrix. there is rows and columns
#                  ['G', 'H', 'I']])


# now we are going to higher dimension , three dimensions
# array = np.array([[['A', 'B', 'C'],['D','E', 'F'],['G','H','I']],   # they need to be consistent number of elements
#                   [['J', 'K', 'L'],['M','N','O'],['P','Q','R']],    # within each list this program will give us
#                   [['S', 'T', 'U'],['V','W', 'X'],['Y','Z']]])      # value error

array = np.array([[['A', 'B', 'C'],['D','E', 'F'],['G','H','I']],   # what you could so is add some sort of placeholder
                  [['J', 'K', 'L'],['M','N','O'],['P','Q','R']],
                  [['S', 'T', 'U'],['V','W', 'X'],['Y','Z',' ']]])

# you could go beyond three dimensions, too. You can go to four dimensions, five dimensions etc


print(array.ndim)   # meaning number of attributes

# you can also access the shape
print(array.shape)    # this will return a tuple of integers, it shows you the depth of number of rows, and the number of
                      # columns    (depth, rows, columns)
                      # think of it as a cake , it has three layers, top layer , middle layer, and the bottom layer.
                      # Each layer has three rows, each row has three columns.

# with python list , if we have to access any element . you use chain indexing
print(array[0][0][0])   # this is called chain indexing.

# with numpy we have access to something called multidimensional indexing.
# multidimensional indexing is faster than chain indexing
print(array[0, 0, 0])
print(array[0, 0, 1])
print(array[0, 0, 2])
print(array[0, 1, 0])
print(array[1,1,1])

# Exercise: We are going to perform three letter word using string concatenation
word = array[2, 0, 0] + array[0, 0, 0] + array[0, 0, 0] + array[2, 0, 0]
print(word)

