def search_matrix(matrix, target):
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    m = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(search_matrix(m, 5))
