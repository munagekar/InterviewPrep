# These are unoptimized ways for longest palindrome search
from itertools import combinations_with_replacement


# Complexity Cubic
def brutus(st):
    ans = 0
    for i, j in combinations_with_replacement(list(range(len(st))), 2):

        if checkpali(st[i:j + 1]):
            ans = max(ans, j - i + 1)

    return ans


# Complexity Linear
def checkpali(st):
    i = 0
    j = len(st) - 1
    while i < j:
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1

    return True


# Build single element table
# Build a adjacent element table
# Finally use this table and go bottom up
# Complexity : Quadratic
def dp(st):
    maxi = 1
    lt = len(st)
    table = [[0] * lt] * lt
    for x in range(lt):
        table[x][x] = True
    for x in range(lt - 1):
        if st[x] == st[x + 1]:
            table[x][x + 1] = True
            maxi = 2
    for k in range(3, lt + 1):
        for start in range(0, lt - k + 1):
            end = start + k - 1
            if table[start + 1][end - 1] is True and st[start] == st[end]:
                maxi = k
                table[start][end] = True

    return maxi


print brutus("abc"), dp("abc")
print brutus("dabcd"), dp("dabcd")
print brutus("abccba"), dp("abccba")
print brutus("daaab"), dp("daaab")
