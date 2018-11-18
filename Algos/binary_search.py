from __future__ import print_function, division


def binary_search(arr, key, first, last):
    mid = (first + last) // 2
    if arr[mid] > key:
        return binary_search(arr, key, first, mid - 1)
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, last)
    else:
        return mid


def bs_non_recursive(arr, key):
    first = 0
    last = len(arr)
    while last - first > 0:
        mid = (last + first) // 2
        if arr[mid] > key:
            last = mid - 1
        elif arr[mid] < key:
            first = mid + 1
        else:
            return mid
    return first


items = [1, 2, 3, 4, 5, 8, 10, 11, 13, 17, 18, 19]

for i in items:
    print(binary_search(items, i, 0, len(items) - 1))
    print(bs_non_recursive(items, i))
