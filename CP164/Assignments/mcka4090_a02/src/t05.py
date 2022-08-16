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
from Food_utilities import read_foods, food_table, food_search

# --------Constants-------- #


# -------Inputs-------- #
file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

# --------Calculations-------- #
result = food_search(foods, 9, 0, True)

# --------Output-------- #
food_table(result)
