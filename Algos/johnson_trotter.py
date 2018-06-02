from copy import deepcopy


# Might be a better idea to convert list to a list of tupples
# Number along with direction if the number aint a sequence
# Else just use this for generation of index values
# Then use the index values to give the result. Like itertools.permutations
def jt(li):
    # Init stuff
    li.sort()
    lt = len(li)
    dirs = [-1] * lt
    result = list()
    result.append(deepcopy(li))

    while True:
        # Find mobile
        mobile = -1
        for i in range(lt):
            neigh = i + dirs[li[i]]
            if neigh < 0 or neigh >= lt:
                continue
            if li[i] > li[neigh] and (mobile == -1 or li[mobile] < li[i]):
                mobile = i

        # If Mobile not found. Sequence is done
        if mobile == -1:
            break

        mobinum = li[mobile]
        neigh = mobile + dirs[li[mobile]]
        # swap
        li[mobile], li[neigh] = li[neigh], li[mobile]

        # update

        for i in range(lt):
            if li[i] > mobinum:
                dirs[li[i]] *= -1

        print li
        raw_input()
        result.append(deepcopy(li))

    return result


if __name__ == "__main__":
    print(jt([0, 1, 2, 3]))
