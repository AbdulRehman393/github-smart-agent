# validate user input exercise
# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must  not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 character")
elif  username.find(" ") != -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your user name cannot contain number")
else:
    print(f"Welcome {username}")



