# Algorithm for Largest Contigous Sum of Array
# O(N)


def kadane(li):
    # current max, total max
    c_max = li[0]
    t_max = li[0]

    for num in li[1:]:
        c_max = max(num, c_max + num)
        t_max = max(c_max, t_max)
    return t_max


def kadane_with_indices(li):
    cfirst = 0
    clast = 0
    tfirst = 0
    tlast = 0
    c = li[0]
    t = li[0]
    for i in range(1, len(li)):
        num = li[i]
        if num < num + c:
            c = num + c
            clast = i

        else:
            c = num
            cfirst = i
            clast = i

        if c > t:
            t = c
            tfirst, tlast = cfirst, clast

    return t, tfirst, tlast


if __name__ == "__main__":
    li = [-2, -3, 4, -1, -2, 1, 5, -3]
    print kadane(li)
    print kadane_with_indices(li)
