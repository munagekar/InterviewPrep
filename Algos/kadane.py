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


if __name__ == "__main__":
    li = [-2, -3, 4, -1, -2, 1, 5, -3]
    print kadane(li)
