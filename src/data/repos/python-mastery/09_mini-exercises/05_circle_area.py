import math
# Calculating Area of a circle
# pi*r*2
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)

print(f"The Area of a Circle : {round(area,2)} cm^2")