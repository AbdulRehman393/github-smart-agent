# object = A "bundle" of related attributes(variables) and methods(functions)   # a method is a function that belongs within that object
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car


# Object
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)


print(car1.model)                           # car1.   this .(dot) is known as attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car1.stop()
car1.describe()