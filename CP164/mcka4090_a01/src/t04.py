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
from functions import is_leap_year

# --------Constants-------- #


# --------Inputs-------- #
year = int(input("Year: "))

# --------Calculations-------- #
leap_year = is_leap_year(year)

# --------Output-------- #
print(f'Leap Year? {leap_year}')
