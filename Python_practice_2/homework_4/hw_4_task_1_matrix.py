# Напишите функцию для транспонирования матрицы

def matrix_transposition(matrix: list[[]]):
    ready_for_transposition: bool = True
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            ready_for_transposition = False
            print('This matrix can not be transposed')
            return None
    res_matrix = list([0 for j in range(len(matrix))] for i in range(len(matrix[0])))
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            res_matrix[j][i] = matrix[i][j]
    return res_matrix



# matrix: list = [[0, 1, 2, 3, 4], ['а', 'б', 'в', 'г', 'д'], [6, 7, 8, 9, 10], ['ж', 'з', 'и', 'к', 'л'],
#                 ['н', 'о', 'п', 'р', 'с']]
matrix = [[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4]]
for i in matrix:
    print(i)
matrix_2 = matrix_transposition(matrix)
print()
for i in matrix_2:
    print(i)

