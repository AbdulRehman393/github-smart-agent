# --------------------------- Arithmetic Calculator ---------------------------------------

operator = input("Select any operator + - * / % ** % //: ")
num1 = float(input("Enter first number: "))
num2= float(input("Enter second numbr: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "%":
    result = num1 % num2
    print(round(result, 3))
elif operator == "**":
    result = num1 ** num2
    print(round(result, 3))
elif operator == "//":
    result = num1 // num2
    print(round(result, 3))

else:
    print(f"{operator} not a valid operator")