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
from functions import dsmvwl

# --------Constants-------- #


# --------Inputs-------- #
s = str(input("Sentence: "))

# --------Calculations-------- #
out = dsmvwl(s)

# --------Output-------- #
print(f'Disemvowelled: {out}')