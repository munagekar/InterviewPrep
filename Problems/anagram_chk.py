# If large number multiplication is cheap,not really :-P
# Generate first 26 primes corresponding to each letter
# Now multiply and generate hash. Compare hash


# Naive O(nlogn)
def ana_chk(st1, st2):
    if sorted(st1) == sorted(st2):
        return True
    return False


# OPtim O(n)
def optim(st1, st2):
    if len(st1) != len(st2):
        return False
    _hash = [0] * 26
    for i in range(len(st1)):
        _hash[ord(st1[i]) - ord('a')] += 1
        _hash[ord(st2[i]) - ord('a')] -= 1
    for val in _hash:
        if val != 0:
            return False
    return True


st = "abcdefg"
cst = "abdefgc"
print ana_chk(cst, st)
print optim(st, cst)
st = "abcdefg"
cst = "abcdeeg"
print ana_chk(cst, st)
print optim(st, cst)
