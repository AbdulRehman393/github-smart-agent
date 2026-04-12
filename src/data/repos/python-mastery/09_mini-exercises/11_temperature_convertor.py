
unit = input("What is the unit of the temperature? press 'F' for Fahrenheit or 'C' for Celsius: ").upper()
temperature = float(input("Enter a temperature: "))

if unit == 'F':
    temperature = (temperature - 32) * 5/9
    unit = 'C'
    print(f"Temperature is {round(temperature,1)}° {unit}")    #Shortcut for degree symbol in Windows : Alt + 0176
elif unit == 'C':                                             #                           in Mac : Shift + Option + 7
    temperature = temperature * 9/5 + 32
    unit = 'F'
    print(f"Temperature is {round(temperature,1)}° {unit}")
else:
    print(f"{unit} is an invalid unit for temperature.")

