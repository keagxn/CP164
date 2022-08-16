"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""

# --------Imports-------- #
from Food import Food
from Food_utilities import read_foods, by_origin

# --------Constants-------- #


# -------Inputs-------- #
origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

# --------Calculations-------- #

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

origins = by_origin(foods, origin)

# --------Output-------- #
for food in origins:
    print(food, end="\n\n")
