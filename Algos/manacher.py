# Longest Palindromic Substring
# O(n)

'''
In manacher algorithm the whole idea is to avoid doing work
by using work already done in the mirror part of the palindrome
'''
from __future__ import division
import operator


def manacher(st):
    # Preprocess
    # Add additional nonmatching chars at end to avoid bound checking
    # simply awesome :-)
    st2 = "^" + st.replace("", "#") + "$"

    i = 1
    C = 0
    R = 0
    P = [0] * len(st2)
    while i < len(st2) - 1:
        # Mirror Position Based on Center
        i_mir = 2 * C - i
        # Is it within last palindrome else it is set to 0
        # and will be explored
        if R > i:
            P[i] = min(R - i, P[i_mir])

        while st2[i + 1 + P[i]] == st2[i - 1 - P[i]]:
            P[i] += 1

        # Update Right if necessary
        if R < i + P[i]:
            C = i       # New center for palindrome
            R = i + P[i]

        i += 1

    c, maxlen = max(enumerate(P), key=operator.itemgetter(1))
    # This center is shifted by extra char so c-1
    start = (c - 1 - maxlen) // 2
    end = start + maxlen
    # end not included
    return st[start:end]


if __name__ == "__main__":
    print manacher("babcbabcbaccba")
    print manacher("abaaba")
    print manacher("abababa")
    print manacher("abcbabcbabcba")
    print manacher("forgeeksskeegfor")
    print manacher("caba")
    print manacher("abacdfgdcaba")
    print manacher("abacdfgdcabba")
    print manacher("abacdedcaba")
