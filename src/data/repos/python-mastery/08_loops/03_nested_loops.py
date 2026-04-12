# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
# We can have any for loop inside another for loop, while loop insider another while loop,
# for loop inside while loop , while loop inside for loop

for x in range(3):
    for y in range(1, 10):
        print(y, end = "")   # If I want all of these numbers on the same line,or you could add a different symbol
    print()