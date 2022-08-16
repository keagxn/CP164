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
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)

# --------Output-------- #
