import unittest
from random import randint
import time


# Simple Insertion Sort
# Stable, inplace
# Complexity O(n2)
# 2x faster than buble sort
def insort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp
    return arr


class Tester(unittest.TestCase):

    def test_insort(self):
        start = time.time()
        for l in range(1000, 2001):
            test = []
            for i in range(l):
                test.append(randint(0, 1023))
            self.assertEqual(sorted(test), insort(test))
        end = time.time()
        print "Insertion Sort Time", end - start


if __name__ == "__main__":
    unittest.main()
