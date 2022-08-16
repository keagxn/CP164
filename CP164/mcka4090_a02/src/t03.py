"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-21"
-------------------------------------------------------
"""

# --------Imports-------- #
from Food_utilities import read_food, calories_by_origin

# --------Constants-------- #


# -------Inputs-------- #
keagan_mckay = read_food('Keagan McKay|4|True|420')

shortbread = read_food('Shortbread |9|True|502')

# --------Calculations-------- #
a = calories_by_origin([keagan_mckay, shortbread], 9)

# --------Output-------- #
print(f"Average Calories: {a}")
