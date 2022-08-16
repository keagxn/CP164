"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""

# --------Imports-------- #
from functions import is_palindrome_stack

# --------Constants-------- #


# -------Inputs-------- #
string = input("Enter a string: ")

# --------Calculations-------- #
palindrome = is_palindrome_stack(string)

# --------Output-------- #
print(palindrome)
