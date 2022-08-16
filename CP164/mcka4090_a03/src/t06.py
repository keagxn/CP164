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
from functions import reroute

# --------Constants-------- #


# -------Inputs-------- #
opstring = input("Enter opstring: ")

# --------Calculations-------- #
values_in = [1, 2, 3, 4, 5, 6]

values_out = reroute(opstring, values_in)

# --------Output-------- #
print(values_out)
