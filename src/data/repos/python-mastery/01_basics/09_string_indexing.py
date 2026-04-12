# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
# step     = if you need to skip over the characters

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])                    # Python will assume it the starting position will be the beginning of the string
print(credit_number[5:9])                   # the ending index is exclusive
print(credit_number[5:])                    # everything besides  4 digits to the end of the string
print(credit_number[-3])                    # if you need character in a string
print(credit_number[::2])                   # this will print every second character with in our string
print(credit_number[2:-1:3])                # now it will count every third character


# if you want to display reverse string
text = "Hello"
print(text[::-1])