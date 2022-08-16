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
from functions import matrix_stats

# --------Constants-------- #

# --------Inputs-------- #
a = [[0, 1], [2, 3], [6, 3], [5, 9], [9, 2]]
print(f'Input: {a}')

# --------Calculations-------- #
small, large, total, average = matrix_stats(a)

# --------Output-------- #
print(f'Smallest number: {small}')
print(f'Largest number: {large}')
print(f'Total of all numbers: {total}')
print(f'Average of all numbers: {average}')