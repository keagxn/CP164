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

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
list1 = List()

# --------Output-------- #
list1.append(100)

print(len(list1))

list1.insert(0, 200)

print(len(list1))

remove = list1.remove(200)

print(remove)
