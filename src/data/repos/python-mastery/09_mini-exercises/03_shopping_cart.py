item = input("What item would you like to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like: "))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${round(total,2)}")   # We can truncate everything upto number of decimal places as we want by using round function

