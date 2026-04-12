# Getting last four digits of a credit card number

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# let's reverse the string of our credit card number
print(credit_number[::-1] )       # We don't need starting index and the ending index , for the step it will be -1
                                  # -1 will reverse the string
