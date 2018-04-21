'''
Python 3
'''

import itertools
import operator

# List and Tupple Stuff

# Reverse a List
a = [1, 2, 3]
print(a[::-1])

# Remove Duplicates List
a = [1, 2, 3, 3, 2, 2, 2]
a = list(set(a))
print(a)

# Swap Numbers
a = 1
b = 2
a, b = b, a
print(a, b)

# Unpacking
first, *mid, end = [1, 2, 3, 4]
print(mid)

# zip
a = [1, 2, 3]
b = [4, 5, 5]
ab = [z for z in zip(a, b)]
print(ab)


# itertools

# Combinations
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))
# Permutations
print(list(itertools.permutations([1, 2, 3], 2)))
# Accumulate
print(list(itertools.accumulate([1, 2, 3], operator.add)))
# Cartesian Product
print(list(itertools.product([1, 2, 3, 4], [5, 6])))
