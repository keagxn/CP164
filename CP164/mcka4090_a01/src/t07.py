"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""

# --------Imports-------- #
from functions import matrix_transpose

# --------Constants-------- #


# --------Inputs-------- #
a = [[0, 1], [2, 3], [6, 3], [5, 9], [9, 2]]
print(f'Input: {a}')

# --------Calculations-------- #
b = matrix_transpose(a)

# --------Output-------- #
print(f'Output: {b}')
