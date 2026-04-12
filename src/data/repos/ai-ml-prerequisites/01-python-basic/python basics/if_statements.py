#if statements = execute some code if a condition is True
#                they allow for basic decision-making
#                (if, elif, else)

#The order of you if and elif statements matter, because the condition at the top if true will execute   and will leave
#rest of the conditions to check , it will not check rest of the statements

age = int(input("What is your age"))
has_ticket = True
price = 10.00

if age >= 65:
    print(f"You are a senior citizen")
    print(f"The ticket price for a senior citizen is ${price*0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"The ticket price for an adult is ${price}")
else:
    print("You are a child")
    print("The price ticket for a child is ${price*0.5}")


if has_ticket:
    print("You have a ticket, you may enter")
else:
    print("You are not having ticket, You may not enter")