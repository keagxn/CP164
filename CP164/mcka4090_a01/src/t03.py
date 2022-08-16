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
from functions import file_analyze

# --------Constants-------- #
fv = open("fv.txt", "r")

# --------Inputs-------- #

# --------Calculations-------- #
u, l, d, w, r = file_analyze(fv)

# --------Output-------- #
print(f'# of Uppercase: {u}')
print(f'# of lowercase: {l}')
print(f'# of digits: {d}')
print(f'# of whitespace: {w}')
print(f'# of remaining: {r}')