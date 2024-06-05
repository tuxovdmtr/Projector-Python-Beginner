import numpy as np
import pandas as pd
import math

# a. Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11

zero_array = np.zeros((4, 3))
ones_array = np.ones((4, 3))
full_array = np.arange(12)
print(zero_array)
print(ones_array)
print(full_array.reshape(4, 3))

# b. Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.

def function(x):
    return 2 * (x ** 2) + 5

value_range = np.arange(1, 101, 1)
pd_1 = pd.DataFrame(function(value_range), columns=['Tabular form'])
print(pd_1)

# c. Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

def function_2(x):
    return math.e ** -x

value_range = np.arange(-10, 11, 1)
pd_2 = pd.DataFrame(function_2(value_range), columns=['Tabular form'])
print(pd_2)