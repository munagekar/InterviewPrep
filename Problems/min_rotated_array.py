# To find minimum value in rotated sorted array
# Use binary search,there is a single reset point
# If mid is less than right than array has been increasing
# Ie doesn't have reset point explore left side instead
from __future__ import division
from random import randint
import unittest
import operator


# Generate rotated list
def rotagen():
    li = [randint(0, 9) for r in range(10)]
    sortli = sorted(list(set(li)))
    split = randint(0, len(sortli) - 1)
    return sortli[split:] + sortli[:split]


def find(left, right, li):
    if left == right:
        return left, li[left]

    mid = (left + right) // 2

    if li[mid] < li[right]:
        return find(left, mid, li)
    else:
        return find(mid + 1, right, li)


class Tester(unittest.TestCase):

    def test_find(self):
        for i in range(1000):
            li = rotagen()
            print "List:", li
            idx, val = find(0, len(li) - 1, li)
            min_idx, min_val = min(enumerate(li), key=operator.itemgetter(1))
            self.assertEquals(idx, min_idx)
            self.assertEquals(val, min_val)


if __name__ == "__main__":
    unittest.main()
