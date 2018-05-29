# Check whether all items are unique are not
# Eg : In string
# All methods accept strings
import itertools
import unittest


# Complexity : O(n2)
# Iterate over all combinations to check if equal
def naive(s):
    return all(i != j for i, j in itertools.combinations(list(s), 2))


# Complexity : O(nlogn)
# Sort and ensure adjacent elements are not equal
def sort_n_chk(s):
    ss = sorted(s)
    return all(i != j for i, j in zip(ss[:-1], ss[1:]))


# Complexity : O(n)
# Standard Hash n Check
def flag_chk(s):
    sl = list(s)
    flag = [0] * 26
    for char in sl:
        idx = ord(char) - ord('a')
        flag[idx] += 1
        if flag[idx] > 1:
            return False
    return True


# Complexity: 0(nlogn)
def pytricks(s):
    return len(s) == len(set(list(s)))


# Complexity : 0(n)
# Hash inside single number
def bit_chk(s):
    bits = 0
    for char in list(s):
        test = 1 << (ord(char) - ord('a'))
        if bits & test:
            return False
        else:
            bits &= test
    return True


class Tester(unittest.TestCase):

    def test_all(self):
        t1 = "abcdef"
        t2 = "abc"
        t3 = "a"
        f1 = "aa"
        f2 = "abcdea"
        f3 = 'defghijklmnopqrsdtuvz'

        funcs = [bit_chk, pytricks, sort_n_chk, naive, flag_chk]
        f = [f1, f2, f3]
        t = [t1, t2, t3]
        for func, s in itertools.product(funcs, t):
            self.assertTrue(func(s))
        for f, s in itertools.product(funcs, f):
            self.assertFalse(func(s))


if __name__ == "__main__":
    unittest.main()
