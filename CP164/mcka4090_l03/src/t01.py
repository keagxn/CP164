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
from Queue_array import Queue

# --------Constants-------- #
queue = Queue()

# --------Input-------- #


# --------Calculations-------- #
value = input("Enter a value: ")

queue.insert(value)

# --------Output-------- #
print(len(queue))
