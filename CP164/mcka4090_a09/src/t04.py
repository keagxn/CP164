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

from BST_linked import BST

bst = BST()

arr = [11, 7, 15, 6, 9, 12, 18, 8]

for value in arr:
    bst.insert(value)

zero, one, two = bst.node_counts()

print("Number of nodes with no children: ")
print(zero)

print()
print("Number of nodes with one child: ")
print(one)

print()
print("Number of nodes with two children: ")
print(two)

print()
print("BST contains 15?: ")
print(15 in bst)

print()
print("Parent Node for 15: ")
print(bst.parent(15))

print()
print("Parent Node for 8 (found recursively): ")
print(bst.parent_r(8))
