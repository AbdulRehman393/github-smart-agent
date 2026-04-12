# Define the generate_email function
def generate_email(full_name):
    name_parts = full_name.split()
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'

    # Return the email address
    return email


# Call the function on the full_name string
print(generate_email("Abdul Rehman"))