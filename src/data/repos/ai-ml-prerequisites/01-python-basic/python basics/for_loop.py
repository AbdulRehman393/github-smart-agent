# for loops = used to iterate over a sequence (string, list, tuple, set)
#             repeat a block of code an exact amount of times

for i in range(10):
    print(i)


for i in range(91, 101):   # The first number is inclusive , the second number is exclusive
    print(i)


for i in range(1,11,2):    #Here, We are incrementing our index by 2 during each index ,that is the third value
    print(i)


name = "Abdul Rehman"

for letter in name:
    print(letter, end=" ")           # At the end of each print statement, we print a new line character rather than a new line character
                                     # let's make one following change, let's set the ending character to be something else like a space, We can
                                     # also use other characters like comma or something else.

