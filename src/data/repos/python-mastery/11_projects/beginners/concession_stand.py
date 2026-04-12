# Concession stand

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []  # to keep track of user, selected items
total = 0  # to keep track of a total

print("------------ MENU ------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) :
        cart.append(food)
        total += menu.get(food)
    else:
        print("That Item is not in our Menu or type it correctly")

print("----------- YOUR ORDER ------------")

for food in cart:
    print(food,end = " ")

print()
print(f"Total is: ${total:.2f}")