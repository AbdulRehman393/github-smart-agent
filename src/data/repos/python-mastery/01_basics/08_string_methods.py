# --------------------------------- String Methods -----------------------------------------
name = input("Enter your full name: ")

# length
length = len(name)

print(length)

# first occurence
result =name.find("A")    # the find method will return the first occurence of a given character , the position
print(result)

# last occcurence
result = name.rfind("o")     # If python is not able to locate a given character it will return negative one (-1)
print(result)

# Capitalize first character of a String
result = name.capitalize()
print(result)

# upper method will take all characters in a string and make it upper case
result = name.upper()
print(result)

# lower method will take all characters in a string and make it lower case
result = name.lower()
print(result)

# isdigit method will return either true or false if , true if there are only digits in that string else false
result = name.isdigit()
print(result)

# isalpha method will return either true or false if , true if there are only alphabetical character in that string else false
result = name.isalpha()                       # remember space is not an alphabetical character
print(result)

phone_number = input("Enter you phone number #:")

# let's check how many characters (here we are checking dashes) in our string
result = phone_number.count("0")
print(result)

# replace method replace any occurence with one character with another, it's most useful method of string
result = phone_number.replace("-"," ")    # We can also eliminate dashes or another character by replacing it with
print(result)                                          # empty string  like this  phone_number.replace("-","")

# If you want to comprehensive list to all the string methods available to you
print(help(str))