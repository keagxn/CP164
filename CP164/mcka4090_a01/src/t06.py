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
from functions import max_diff

# --------Constants-------- #

# --------Inputs-------- #
a = list(map(int, input("\nEnter the numbers : ").strip().split()))

# --------Calculations-------- #
md = max_diff(a)

# --------Output-------- #
print(f'Maxdif: {md}')
