"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from List_linked import List


file_variable = open("food.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.find(foods[1]))

print(new_list.index(foods[1]))

print(foods[1] in new_list)
