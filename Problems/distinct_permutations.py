# Generate Distinct Permutations recursively
# complexity : 0(n2 * n!)


def dperm(st):
    if len(st) == 1:
        return [st]
    bag = list()
    unique_char = set(st)  # Can be optimized to O(n)
    # To order these permutations in lexi order
    # Simply sort the unique characters
    # ie unique_char = sorted(set(st))
    for ch in unique_char:
        remaining = charsub(st, ch)  # cost O(n)
        r_perms = dperm(remaining)
        bag.extend([ch + perm for perm in r_perms])

    return bag


def charsub(st, ch):
    return st.replace(ch, '', 1)


if __name__ == "__main__":
    print dperm('a')
    print dperm('ab')
    print dperm('abc')
    print dperm('baba')
    print dperm('bbaa')
