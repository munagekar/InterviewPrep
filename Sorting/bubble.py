# Inplace 0(n2)
import unittest
from random import randint
import time


def buble(arr):
    for step in range(len(arr) - 1, 0, -1):
        for j in range(0, step):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Reduces the number of steps usualy
def optim(arr):
    steps = len(arr) - 1
    while steps > 0:
        swap_idx = 0
        for j in range(0, steps):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_idx = j
        steps = swap_idx

    return arr


class Tester(unittest.TestCase):

    def test_buble(self):
        start = time.time()
        for l in range(1000, 2001):
            test = []
            for i in range(l):
                test.append(randint(0, 1023))
            self.assertEqual(sorted(test), buble(test))
        end = time.time()
        print "Buble Sort Time", end - start

    def test_optim(self):
        start = time.time()
        for l in range(1000, 2001):
            test = []
            for i in range(l):
                test.append(randint(0, 1023))
            self.assertEqual(sorted(test), optim(test))
        end = time.time()
        print "Opt Buble Sort Time", end - start


if __name__ == "__main__":
    unittest.main()

'''
Buble Sort Time 97.4582951069
.Opt Buble Sort Time 102.402309895
.
----------------------------------------------------------------------
Ran 2 tests in 199.861s

OK
'''
