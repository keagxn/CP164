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
from List_array import List
from utilities import array_to_list, list_to_array

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)

# --------Output-------- #
print("Printing LList: ")

for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("Printing List: ")

for value in source:
    print(value)
