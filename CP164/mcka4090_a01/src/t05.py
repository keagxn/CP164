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
from functions import is_palindrome

# --------Constants-------- #


# --------Inputs-------- #
s = str(input("Palindrome: "))

# --------Calculations-------- #
palindrome = is_palindrome(s)

# --------Output-------- #
print(f'Palindrome? {palindrome}')