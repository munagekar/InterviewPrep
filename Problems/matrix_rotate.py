
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
'''
mat = [[7, 4, 1],
       [8, 5, 2],
       [9, 6, 3]]
'''


# clockwise 90
def rotate(mat):
    rows = len(mat)
    cols = len(mat[0])
    target = list()
    for j in range(cols):
        temprow = []
        for i in range(rows - 1, -1, -1):
            temprow.append(mat[i][j])
        target.append(temprow)

    return target


# The following can also be used for inplace rotation
def pytricks(mat):
    # transpose a row reversed matrix
    return zip(*mat[::-1])

# Another idea is to treat the matrix as independent rings
# And then perform the rotation, might be slightly tricky to implement


if __name__ == "__main__":
    print rotate(mat)
    print rotate(mat2)
    print pytricks(mat)
    print pytricks(mat2)
