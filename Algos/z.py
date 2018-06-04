import unittest


def z(text):
    L = 0
    R = 0
    Z = [0]
    for i in range(1, len(text)):
        # char i not in window use regular checking method
        if i > R:
            L = i
            R = i
            while R < len(text) and text[R - L] == text[R]:
                R += 1
            Z.append(R - L)
            R -= 1
        # In window so reuse
        else:
            # distance within window
            d = i - L
            # Check if match not touching window
            if i + Z[d] - 1 < R:
                Z.append(Z[d])
            else:
                L = i
                while R < len(text) and text[R - L] == text[R]:
                    R += 1
                Z.append(R - L)
                R -= 1
    return Z


# Returns list of matching indices
def match(text, pat):
    Z = z(pat + '$' + text)
    return [idx - len(pat) - 1 for idx, val in enumerate(Z) if val == len(pat)]


class Tester(unittest.TestCase):

    def test_z(self):
        self.assertEqual(z('aabcaabxaaaz'),
                         [0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0])
        self.assertEqual(z("aaaaaa"), [0, 5, 4, 3, 2, 1])
        self.assertEqual(z("aabaacd"), [0, 1, 0, 2, 1, 0, 0])
        self.assertEqual(z("abababab"), [0, 0, 6, 0, 4, 0, 2, 0])


if __name__ == "__main__":
    pat = "aab"
    text = "aabcaabxaaaz"
    print match(text, pat)
    unittest.main()
