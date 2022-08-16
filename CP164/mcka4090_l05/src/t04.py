"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from functions import to_power

base = float(input("Enter the base value: "))

power = int(input("Enter the power: "))

ans = to_power(base, power)

print(ans)
