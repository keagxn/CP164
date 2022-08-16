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
from functions import stack_combine
from utilities import array_to_stack

# --------Constants-------- #
source1 = Stack()

source2 = Stack()

# -------Inputs-------- #


# --------Calculations-------- #
array_to_stack(source1, [6, 9, 4, 20])

array_to_stack(source2, [7, 1, 8, 7, 6, 9])

target = stack_combine(source1, source2)

# --------Output-------- #
while not target.is_empty():
    value = target.pop()
    print(value)
