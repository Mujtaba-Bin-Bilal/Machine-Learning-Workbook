def transpose(a):
    rows_a=len(a)
    cols_a=len(a[0])
    solution=[[0 for _ in range(rows_a)] for _ in range(cols_a)]
    for i in range(rows_a):
        for j in range(cols_a):
            solution[j][i]=a[i][j]
    return solution
a=[[1,2,3],[4,5,6]]
print(transpose(a))
