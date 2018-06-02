import itertools
from copy import deepcopy

# Some pattern to note

'''

12345 = 12354
12340 = 12403
154320 = 201345

'''

# Algorithm : Derived after observing pattern
'''

1. Find from right the first index that can be swaped.
Ie index having value less that right neighbor

2. Find from right the first value that is bigger than the number to be swap

3. Perform the swap and then reverse. Don't sort :-P

'''

# For previous perm just reverse the signs,directions remain same :-)


# Making this inplace is blunder
# Unfortunately it was made :-(
def nextperm(numlist):
    swapdex = -1  # Idx to be swapped
    for i in range(len(numlist) - 2, -1, -1):
        if numlist[i] < numlist[i + 1]:
            swapdex = i
            break

    if swapdex == -1:
        # Return reversed list
        return part_rev(numlist, 0, len(numlist) - 1)

    otherdex = -1  # Other number to be swaped

    for i in range(len(numlist) - 1, swapdex, -1):
        if numlist[i] > numlist[swapdex]:
            otherdex = i
            break

    assert(otherdex != -1), "Error in Otherdex"

    numlist[swapdex], numlist[otherdex] = numlist[otherdex], numlist[swapdex]
    return part_rev(numlist, swapdex + 1, len(numlist) - 1)


# Partial Rev : Inplace
# Li : List whose part is to be reversed
# start,end : Inclusive indexes
def part_rev(li, start, end):
    assert(end >= start), "Error in Indices"

    i = start
    j = end
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1

    return li


if __name__ == "__main__":
    testlist1 = [1, 2, 3, 4, 5]
    testlist2 = [1, 1, 3, 4, 4, 5]
    testlist3 = [1, 3, 5, 5, 7, 7]
    testlist4 = [1, 1, 1, 1]
    testlists = [testlist2]

    for testlist in testlists:
        ctestlist = deepcopy(testlist)
        iterlist = list(itertools.permutations(ctestlist, len(ctestlist)))
        iterlist = sorted(set(iterlist))
        ans = [testlist]
        temp = deepcopy(testlist)
        for i in range(len(iterlist) - 1):
            temp = nextperm(temp)
            ans.append(deepcopy(temp))

        for i in range(len(iterlist)):
            print iterlist[i], ans[i]
