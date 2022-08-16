"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID:      210924090
Email:   mcka4090@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""

from BST_linked import BST
from morse import DATA1, fill_code_bst, decode_morse

bst = BST()

fill_code_bst(bst, DATA1)

text = "... --- ..."

print(decode_morse(bst, text))
