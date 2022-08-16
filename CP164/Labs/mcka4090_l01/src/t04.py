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

from Food_utilities import read_food

# --------Constants-------- #


# -------Inputs-------- #

to_read = input("Enter food details: ")


# --------Calculations-------- #
food = read_food(to_read)

# --------Output-------- #
print(food)
