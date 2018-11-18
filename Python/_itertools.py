# itertools
from __future__ import print_function
import itertools
import operator

# Combinations
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5),
# (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

# Permutations
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Accumulate
print(list(itertools.accumulate([1, 2, 3], operator.add)))
[1, 3, 6]


# Cartesian Product
print(list(itertools.product([1, 2, 3, 4], [5, 6])))
# [(1, 5), (1, 6), (2, 5), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6)]