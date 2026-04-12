# default arguments = A default value for certain parameters
#                     default is used when the argument is omitted when you invoke a function
#                     make your function more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# if we are passing in an argument for our discount and tax we'll use whatever is passed in
# rather than the default

print(net_price(500))

# the net_price function would also accept up to two additional arguments
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))


