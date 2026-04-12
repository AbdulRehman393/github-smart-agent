#---------------------- Weight Convertor   ---------------------------------

weight = float(input("Enter your Weight: "))
unit = input("Enter the weight unit Press 'L' for pounds, press 'K' for kilograms: ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "L"
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "L":
    weight  = weight / 2.205
    unit = "K"
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print(f"{unit} is not a valid unit")


