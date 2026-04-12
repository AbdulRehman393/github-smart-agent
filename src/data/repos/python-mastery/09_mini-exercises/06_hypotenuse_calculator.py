import math

# Calculating the hypotenuse of a right triangle

a = float(input("Enter the altitude of a triangle: "))
b = float(input("Enter the base of a triangle: "))

#c = math.sqrt(pow(a,2) + pow(b,2))
c = math.hypot(a,b)

print(f"Hypotenuse of a triangle is {round(c,2)}")

