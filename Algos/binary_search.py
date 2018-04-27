from __future__ import print_function


def binary_search(list, key, first, last):
    mid = (first + last) / 2
    if list[mid] > key:
        return binary_search(list, key, first, mid - 1)
    if list[mid] < key:
        return binary_search(list, key, mid + 1, last)
    else:
        return mid


items = [1, 2, 3, 4, 5, 8, 10, 11, 13, 17, 18, 19]

for i in items:
    print(binary_search(items, i, 0, len(items) - 1))
