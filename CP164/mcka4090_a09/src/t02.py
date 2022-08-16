"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-03-25"
-------------------------------------------------------
"""

from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total

hs = Hash_Set(20)

file = open('otoos610.txt', 'rt')

insert_words(file, hs)

file.close()

total, max_value = comparison_total(hs)

print("Using array-based Sorted List Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_value.word}': {max_value.comparisons:,}")
