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
from utilities import array_to_queue, queue_to_array, queue_test

# --------Constants-------- #
queue = Queue()

# --------Input-------- #


# --------Calculations-------- #
source = [1, 2, 3]

array_to_queue(queue, source)

for _ in range(len(queue)):
    value = queue.remove()
    print(value)
    source.append(value)

array_to_queue(queue, source)

queue_to_array(queue, source)

# --------Output-------- #
print(source)

queue_test(source)
