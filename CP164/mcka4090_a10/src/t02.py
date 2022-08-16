"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-04-01"
-------------------------------------------------------
"""

from List_linked import List
from Sorts_List_linked import Sorts


arr = [
    84, 66, 20, 27, 8, 12, 14, 35, 67, 29,
    6, 10, 87, 2, 93, 39, 37, 69, 49
]

a = List()

for value in arr:
    a.append(value)

Sorts.radix_sort(a)

for value in a:
    print(value, end=", ")
