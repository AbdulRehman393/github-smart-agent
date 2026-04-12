# -------------------------------- Shopping cart  --------------------------------------

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = int(input(f"Enter the price of a {food} : Rs "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end = " ")

print()

for price in prices:
    total += price

print(f"You total price is: Rs. {total}")