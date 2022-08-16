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
from functions import queue_split_alt

# --------Constants-------- #


# -------Inputs-------- #


# --------Calculations-------- #
source = Queue(3)

source.insert(1)

source.insert(2)

source.insert(3)

target1, target2 = queue_split_alt(source)

# --------Output-------- #
print("Printing Target 1...")

while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")

while len(target2) > 0:
    print(target2.remove())
