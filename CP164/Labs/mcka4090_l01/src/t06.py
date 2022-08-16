"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-16"
-------------------------------------------------------
"""

# --------Imports-------- #

from Food_utilities import read_food, write_foods

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #

keagan_mckay = read_food('Keagan McKay|4|True|420')

shortbread = read_food('Shortbread |9|True|502')

file = open("new_foods.txt", "wt")

write_foods(file, [keagan_mckay, shortbread])

file.close()

# --------Output-------- #
