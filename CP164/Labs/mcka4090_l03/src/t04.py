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
from Priority_Queue_array import Priority_Queue

# --------Constants-------- #
pq = Priority_Queue()

# --------Input-------- #


# --------Calculations-------- #
value = int(input("Enter a number: "))

pq.insert(value)

# --------Output-------- #
print(pq.peek())
