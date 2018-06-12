# Longest Common Sequence
# Dynamic Programming

# Space Complexity can be improved to 2*[n+1]
# If number is the only concern. However the table then loses
# The ability to print the actual subsequence
# The idea is that the outerloop depends only on the results of the
# previous answer


def lcs(st1, st2):

    l1 = len(st1)
    l2 = len(st2)

    table = [[0 for x in range(l2 + 1)] for y in range(l1 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0 or j == 0:
                table[i][j] = 0

            elif st1[i - 1] == st2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    sequence = [''] * table[l1][l2]
    index = table[l1][l2] - 1
    i = l1
    j = l2

    while i > 0 and j > 0:
        if st1[i - 1] == st2[j - 1]:
            sequence[index] = st1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return sequence


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print lcs(X, Y)
