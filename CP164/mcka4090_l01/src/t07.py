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

from Food_utilities import read_foods, get_vegetarian

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")

# --------Output-------- #
