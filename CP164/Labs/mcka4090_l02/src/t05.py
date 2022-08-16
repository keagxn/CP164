"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""

# --------Imports-------- #
from Food_utilities import read_foods
from utilities import stack_test

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)

# --------Output-------- #
