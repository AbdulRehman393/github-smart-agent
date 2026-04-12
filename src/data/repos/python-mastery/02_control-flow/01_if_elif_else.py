# if = Do some code only IF some condition is True
#      Else do something else
#      The order of if and elif matter


age = int(input("Enter you age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign up!")
