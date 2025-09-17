def matrix_multiplier(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    # Check compatibility
    if cols_a != rows_b:
        print("The number of columns of A ({}) is not equal to rows of B ({})".format(cols_a, rows_b))
        return None

    # Create an empty resultant matrix
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


# Example
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(matrix_multiplier(a, a), end=" ")
