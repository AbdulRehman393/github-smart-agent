# Arithmetic  = + addition
#             = - subraction
#             = * multiplication
#             = / division (returns a float)
#             = // integer division (returns an integer)
#             = % remainder
#             = ** power
friends = 5

friends += 1                                 #augmented assignment operator    friends += 1 means friends = friends + 1

# unlike other languages python doesn't have an increment operator such as friends++ this is syntax error
# so to increment by 1, we would have to say friends += 1

friends -= 2

friends *= 2

friends /= 2        # Here, it will give us floating point number
friends //= 3       # Here, it will give us integer

remaining_friends = friends % 3


print(friends)

a = 3
b = 2
print(a**b)