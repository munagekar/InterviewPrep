# TODO : Solve this problem with suffix tree


def lcs(st1, st2):
    l1 = len(st1)
    l2 = len(st2)

    table = [[0 for x in range(l2 + 1)] for y in range(l1 + 1)]
    result = 0
    end = 0

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0 or j == 0:
                continue
            if st1[i - 1] == st2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
                if table[i][j] > result:
                    end = i
                    result = table[i][j]

    # Note : End is already one excess
    return st1[end - result:end]


print lcs("xyzabcd", "abcdxyz")
