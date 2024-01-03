import numpy

C = numpy.array([[0.2, 0, 0.2, 0, 0],
                 [0, 0.2, 0, 0.2, 0],
                 [0.2, 0, 0.2, 0, 0.2],
                 [0, 0.2, 0, 0.2, 0],
                 [0, 0, 0.2, 0, 0.2]])
D = numpy.array([[2.33, 0.81, 0.67, 0.92, -0.53],
                 [-0.53, 2.33, 0.81, 0.67, 0.92],
                 [0.92, -0.53, 2.33, 0.81, 0.67],
                 [0.67, 0.92, -0.53, 2.33, 0.81],
                 [0.81, 0.67, 0.92, -0.53, 2.33]])
b = numpy.array([4.2, 4.2, 4.2, 4.2, 4.2])
A = numpy.array(3 * C + D)
#A = numpy.random.rand(5, 5) * 5
#b = numpy.random.rand(5) * 7
A_save = A.copy()
b_save = b.copy()
X = [0., 0., 0., 0., 0.]
swap_arr = []


def check_all_solutions(matrix, vector):
    rang_m = numpy.linalg.matrix_rank(matrix)
    expanded_matrix = numpy.zeros((len(matrix), len(matrix) + 1))
    sh = expanded_matrix.shape
    for i in range(sh[0]):
        for j in range(sh[1]):
            if j == sh[1] - 1:
                expanded_matrix[i][j] = vector[i]
            else:
                expanded_matrix[i][j] = matrix[i][j]
    rang_em = numpy.linalg.matrix_rank(expanded_matrix)
    if(rang_m < len(matrix)):
        if(rang_m == rang_em):
            print("Бесконечное кол-во решений")
        elif(rang_m < rang_em):
            print("Нет решений")
        else:
            print("Proizoshla malenkaya oploshnost")


def swap_rows(matrix, row_1, row_2):
    temp_row = matrix[row_1].copy()
    matrix[row_1] = matrix[row_2]
    matrix[row_2] = temp_row
    temp = b[row_1]
    b[row_1] = b[row_2]
    b[row_2] = temp


def swap_columns(matrix, column_1, column_2):
    swap_arr.append([column_1, column_2])
    for i in range(0, len(matrix)):
        matrix[i][column_1], matrix[i][column_2] = matrix[i][column_2], matrix[i][column_1]


def run_straight(matrix, vector):
    amount_row = len(matrix) # матрица квадратная: кол-во строк = кол-во столбцов
    for i in range(0, amount_row):
        curr_row = matrix[i]
        devider = curr_row[i] # делитель на диагонале
        if(devider == 0):
            print("Система несовместна")
            exit()
        curr_row /= devider
        vector[i] /= devider
        for j in range(i+1, amount_row):
            diag_el = matrix[j][i]
            matrix[j] -= diag_el * curr_row
            b[j] -= diag_el * vector[i]


def run_reverse(matrix, vector): # находим все x[i]
    amount_row = len(matrix)
    for i in reversed(range(0, amount_row)):
        for j in range(i, amount_row):
            vector[i] -= X[j] * matrix[i][j]
        X[i] = vector[i]


def gauss(A, b):
    run_straight(A, b)
    run_reverse(A, b)


def max_index_in_column(matrix, i_column):
    max = matrix[i_column][i_column] # кол-во строчек равно кол-во столбцов
    save_i = i_column
    for i in range(i_column, len(matrix)):
        if matrix[i_column][i] > max:
            max = matrix[i_column][i]
            save_i = i
    return save_i


def run_straight_column(matrix, vector):
    amount_row = len(matrix)  # матрица квадратная: кол-во строк = кол-во столбцов
    for i in range(0, amount_row):
        swap_rows(matrix, max_index_in_column(matrix, i), i)
        curr_row = matrix[i]
        devider = curr_row[i]  # делитель на диагонале
        if (devider == 0):
            print("Система несовместна")
            exit()
        curr_row /= devider
        vector[i] /= devider
        for j in range(i + 1, amount_row):
            diag_el = matrix[j][i]
            matrix[j] -= diag_el * curr_row
            b[j] -= diag_el * vector[i]


def gauss_maxcolumn (A, b):
    run_straight_column(A,b)
    run_reverse(A,b)


def max_element(A, k):
    max = A[k][k]
    max_indexes = [k, k]
    for i in range(k, len(A)):
        for j in range(k, len(A)):
            if max < A[i][j]:
                max = A[i][j]
                max_indexes = [i, j]
    return max_indexes


def run_straight_max(matrix, vector):
    amount_row = len(matrix)  # матрица квадратная: кол-во строк = кол-во столбцов
    for i in range(0, amount_row):
        max_indexes = max_element(matrix, i)
        swap_rows(matrix, max_indexes[0], i)
        swap_columns(matrix, max_indexes[1], i)
        curr_row = matrix[i]
        devider = curr_row[i]  # делитель на диагонале
        if (devider == 0):
            print("Система несовместна")
            exit()
        curr_row /= devider
        vector[i] /= devider
        for j in range(i + 1, amount_row):
            diag_el = matrix[j][i]
            matrix[j] -= diag_el * curr_row
            b[j] -= diag_el * vector[i]


def gauss_max(A, b):
    run_straight_max(A, b)
    run_reverse(A, b)
    for swap in reversed(swap_arr):
        X[swap[0]], X[swap[1]] = X[swap[1]], X[swap[0]]


if __name__ == '__main__':
    print("Исходная матрица:")
    for i in range(0, len(A)):
        print(f"{A[i]} = {b[i]}")
    check_all_solutions(A, b)
    print("Решение методом Гаусса(полного выбора):")
    gauss_max(A, b)
    for i in range(0, len(X)):
        print("%.8f" % X[i], end = " ")
    print("")
    print("Получившийся вектор свободных членов:")
    res = numpy.dot(A_save, X)
    print(res)
    print("Отклонение от изначального вектора свободных членов:")
    deviation = res - b_save
    print(deviation)

