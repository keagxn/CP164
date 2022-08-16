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
from Food_utilities import read_food, average_calories

# --------Constants-------- #


# -------Inputs-------- #
keagan_mckay = read_food('Keagan McKay|4|True|420')

shortbread = read_food('Shortbread |9|True|502')

# --------Calculations-------- #
avg = average_calories([keagan_mckay, shortbread])

# --------Output-------- #
print(f"Average Calories: {avg}")
