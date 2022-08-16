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
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
source = Priority_Queue()

source.insert(1)

source.insert(2)

source.insert(3)

key = 2

target1, target2 = pq_split_key(source, key)

# --------Output-------- #
print("Printing Target 1...")

while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")

while len(target2) > 0:
    print(target2.remove())
