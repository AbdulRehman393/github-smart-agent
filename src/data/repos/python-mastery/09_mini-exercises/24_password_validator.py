import string


user_password = input("Enter a password, it must be at least 8 characters long and must at least a single character: ")

def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password(user_password)
print("Is the password valid? ", is_valid)