'''
Python 3
'''
from __future__ import print_function
import operator

# List and Tupple Stuff

# Reverse a List
a = [1, 2, 3]
print(a[::-1])
# [3, 2, 1]

# Remove Duplicates List
a = [1, 2, 3, 3, 2, 2, 2]
a = list(set(a))
print(a)
# [1, 2, 3]

# Swap Numbers
a = 1
b = 2
a, b = b, a
print(a, b)
# 2 1

# Unpacking
first, *mid, end = [1, 2, 3, 4]
print(mid)
# [2, 3]

# zip
a = [1, 2, 3]
b = [4, 5, 5]
ab = [z for z in zip(a, b)]
print(ab)
# [(1, 4), (2, 5), (3, 5)]











