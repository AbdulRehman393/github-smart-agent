#Typecasting = the process of converting a variable from one date type to another
#              str(), int(), float(), bool()
# Typecasting is very useful when handling with user input because user input is always a string

name = "Abdul Rehman"
age = 25
gpa = 3.2
is_student = True


name = bool(name)   #If somebody enters his name , it will give us true , if somebody does not enter his name, it will give us false
print(name)

# You could get tge datatype of variable or value by using the type function
print(type(name))


gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

# age +=1 here we will get type error We can only concatenate strings, not integers to a string
# if we will do like following , We will be using concatenation
age += "1"  # Since , We are working with strings, the result will be 221
print(age)


