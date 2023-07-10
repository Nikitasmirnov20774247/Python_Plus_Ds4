def trans_matrix(matrix):
    return [[row[ind] for row in matrix] for ind in range(len(matrix[0]))]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(f'Оригинальная матрица:\n{matrix}')
result_matrix = trans_matrix(matrix)
print(f'Транспонированная матрица:')
print(*result_matrix, sep="\n")