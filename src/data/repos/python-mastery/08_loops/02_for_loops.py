# for loop = execute a block a code a fixed number of times.
#            You can iterate over a range, string, sequence, etc. anything
#            that is considered iterable.
# Iterable = something you can go through, item by item, one at a time.

for x in range(5):
    print("Hello World!")


# Iterate forward
for x  in range(1, 11):  # second number is exclusive # it will begin at 1 and will stop at 11
    print(x)             # 1 is inclusive and 11 is exclusive , It'll print from 1 to 10


for x in range(1,11):
    print("Hello, How are you?")


# Iterate Backward

# for y in range(10,1):   # It will not work as range(start, stop) → counts up by 1 by default.
# print(y)

for x in reversed(range(1,11)):
    print(x)
print("Have a Nice Day!")

# Another way to do it
for x in range(10, 0, -1):
    print(x)
print("What's up!")


# there is additional parameter you could add i.e., step
# if you would like to cound by two you will add step as 2

for x in range(1, 11, 2):
    print(x)
print("Have a Nice Day!")


# Iterate over a string

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x, end = " ")

# break and continue keywords

# continue = it will skip that iteration

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

print()

# break = We will break out of the loop entirely

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

