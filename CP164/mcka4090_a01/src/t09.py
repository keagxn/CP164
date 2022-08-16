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
from functions import pig_latin

# --------Constants-------- #

# --------Inputs-------- #
word = str(input("Word: "))

# --------Calculations-------- #
pl = pig_latin(word)

# --------Output-------- #
print(f'Piglatin: {pl}')
