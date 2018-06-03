# Rle


def rle(st):
    prevchar = st[0]
    count = 1
    result = ''
    for char in st[1:]:
        if char != prevchar:
            result += (prevchar + str(count))
            prevchar = char
            count = 1
        else:
            count += 1

    result += (prevchar + str(count))
    return result


print rle("abc")
print rle("abbbbcd")
print rle("aaaa")
print rle("a")
print rle("aaaddd")
print rle("aaabbbccc")
