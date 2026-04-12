# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional  2. default  3. KEYWORD  4. arbitrary

# identifier = the name you give something in a program
# A general term
# Any valid name in Python
# Used for:  variables  functions  classes  modules  constants

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("hello", first="Bilal", last="Raza", title="Mr.")  # with these keyword arguments the order really doesn't matter
# if you are mixing and matching positional arguments and keyword arguments , you need to be sure that positional arguments are first




for x in range(1, 11):
    print(x, end=" ")  # end is a keyword argument found within the built-in print statement

print()

print("1","2","3","4","5", sep="-")    # sep is a keyword argument