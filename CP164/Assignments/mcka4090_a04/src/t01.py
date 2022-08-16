"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-02-04"
-------------------------------------------------------
"""

# --------Imports-------- #
from Queue_circular import Queue

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #


# --------Output-------- #
q = Queue(3)

print(len(q))

print(q.is_empty())

q.insert(100)

print(len(q))

value = q.peek()

print(value)

removed = q.remove()

print(removed)

q.insert(100)
q.insert(200)
q.insert(300)
print(q.is_full())
