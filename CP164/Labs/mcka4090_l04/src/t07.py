"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""

# --------Imports-------- #
from Food_utilities import read_foods
from utilities import list_test

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)

# --------Output-------- #
