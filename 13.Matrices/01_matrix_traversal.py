def traverse_row_major(matrix):
    for row in matrix:
        for x in row:
            print(x, end=" ")
    print()


def traverse_col_major(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=" ")
    print()


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    traverse_row_major(m)
    traverse_col_major(m)
