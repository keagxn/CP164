"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""

# --------Imports-------- #
from Stack_array import Stack
from utilities import array_to_stack

# --------Constants-------- #
source1 = Stack()

# -------Inputs-------- #


# --------Calculations-------- #
array_to_stack(source1, [6, 9, 4, 20])
source1.reverse()

# --------Output-------- #
while not source1.is_empty():
    value = source1.pop()
    print(value)
