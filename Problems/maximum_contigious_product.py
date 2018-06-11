# Similar to Kadane
# The problem here is negative itegers and magnitude less than 1


def mcp(li):
    negacur = li[0]
    posimax = li[0]
    posicur = li[0]

    for i in range(1, len(li)):
        if li[i] >= 0:
            posicur = max(posicur * li[i], li[i])
            negacur *= li[i]

        else:
            negacur, posicur = posicur, negacur  # swap sign change
            posicur *= li[i]
            negacur *= li[i]

        posimax = max(posimax, posicur)

    return posimax


arr = [1, -2, -3, 0, 7, -8, -2]
print mcp(arr)
arr = [-2]
print mcp(arr)
arr = [-2, 0]
print mcp(arr)
arr = [-2, 0, 4]
print mcp(arr)
arr = [-4, 2, -2]
print mcp(arr)
