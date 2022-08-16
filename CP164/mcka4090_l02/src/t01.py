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

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")

stack.push("top")

print(stack.peek())

# --------Output-------- #
