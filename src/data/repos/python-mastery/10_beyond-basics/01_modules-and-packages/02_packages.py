# Packages = A collection of modules , also called libraries       (module = python file)
# Publicly available and free
# Download it from Python Package Index, known as PyPI, which is essentially a directory of packages.
# Then can be imported and used like modules

# Installing a package

# Terminal / Command Prompt
# python3 -m pip install <package_name>
# python3 executes Python code from the terminal
# pip = stands for preferred installer program, tool used to install Python packages.

# Installing pandas
# python3 -m pip install pandas

# Import pandas
# use an alis to shorten the code
import pandas as pd

# Creating a DataFrame

sales = {"user_id": ["KM37", 'PR19', "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

# Convert to a pandas DataFrame
sales_df = pd.DataFrame(sales)

print(sales_df)

# Reading in a CSV file in our current directory
screen_time_df = pd.read_csv("screen_time.csv")

# Checking the type confirms it is a pandas DataFrame.
print((type(screen_time_df)))

# DataFrame method to preview the first five rows
print(screen_time_df.head())

# Checking the file info
print(screen_time_df.info())