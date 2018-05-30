# Generate all permutations of a string
# repeatation allowed


# Non recursive version Non Unique
# ---------------------------------------------------------------
def basic_perm(st):
    bag = ['']
    for i in range(len(st)):
        newbag = []
        for seq in bag:
            newbag.extend(insert(seq, st[i]))
        bag = newbag

    return bag


# o(len(st)2)
def insert(st, ch):
    li = []
    for i in range(len(st) + 1):  # O(len(st))
        li.append(st[:i] + ch + st[i:])  # 0(len(st))

    return li  # number of words returned o(len(st))


# Recursive Non Unique : Backtracking
# _________________________________________________________________
def bt(chars, bag, idx=0):
    if idx == len(chars) - 1:
        bag.append(''.join(chars))
    for i in range(idx, len(chars)):
        chars[idx], chars[i] = chars[i], chars[idx]  # swap
        bt(chars, bag, idx + 1)
        chars[idx], chars[i] = chars[i], chars[idx]  # undo/backtrack


#  _________________________________________________________________


if __name__ == "__main__":
    print basic_perm("abc")
    bag = []
    bt(list("abc"), bag)
    print bag
