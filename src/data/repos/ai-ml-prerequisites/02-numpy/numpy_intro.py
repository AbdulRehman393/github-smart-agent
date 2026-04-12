#NumPy = Numerical Python
# It's a Python Library used for numerical computing, It's widely used in fields that involve heavy data processing,
# such as data science, engineering, artificial intelligence,  and machine learning.
# Python is currently a most popular language for AI and ML due to few reasons:
# Easy to read & write
# offers many libraries
# Integrates well with: API, database, web apps.
# This makes Python a top choice  for building and deploying real world AI solutions
# However, Python is really slow , that's why NumPy comes in.
# Under the hood, it's written in C, which is magnitudes faster than regular Python code
# With AI and Machine Learning, you are often working with massive data sets, and you need to do a lot of
# number crunching. Plain Python lists not going to cut it. Numpy gives us access to numpy arrays which are
# faster than native Python lists. With NumPy arrays we can perform vectorized operations. For example, multiply
# the elements by 2. np.array([1,2,3]*2 = [2,4,6]
# With a python list, multiplying list by two would  repeat all element twice
# e.g., [1,2,3] *2 = [1,2,3,1,2,3]

# Numpy gives you a speed and specialized tools need to handle largescale numerical operations efficiently.

import numpy as np                  # For some convenience, we can give numpy a quick name or alias.

# print(np.__version__)


# In python
# my_list = [1, 2, 3, 4]
# my_list = my_list * 2        # Output:  [1,2,3,4,1,2,3,4]
#
# print(my_list)

# A numpy array is superior to a Python list. It's faster and gives us more operation

array = np.array([1, 2, 3, 4])
array = array * 2

print(array)

# Just to verify that it is a numpy array
print(type(array))   # <class 'numpy.ndarray'>  nd meaning and dimensional array