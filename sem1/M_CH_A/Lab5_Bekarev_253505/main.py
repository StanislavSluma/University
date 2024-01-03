import numpy, math

def jacobi_method(matrix):
    #check_matrix_simmetrix(matrix)
    eigenvectors = numpy.eye(len(matrix))
    temp_A = matrix.copy()
    count = 0;
    while(not_diag_squares(temp_A) > 1e-6):
        temp_V = numpy.eye(len(temp_A))
        m_i, m_j = not_diag_max_element(temp_A)
        if(temp_A[m_i][m_i] - temp_A[m_j][m_j] < 1e-10):
            cos_phi = 1 / (2 ** (1/2))
            if(temp_A[m_i][m_j] > 0):
                sin_phi = 1 / (2 ** (1/2))
            else:
                sin_phi = -1 / (2 ** (1/2))
        else:
            cos_phi = math.cos(0.5 * math.atan(2*temp_A[m_i][m_j] / (temp_A[m_i][m_i] - temp_A[m_j][m_j])))
            sin_phi = math.sin(0.5 * math.atan(2*temp_A[m_i][m_j] / (temp_A[m_i][m_i] - temp_A[m_j][m_j])))
        temp_V[m_i][m_i] = cos_phi
        temp_V[m_j][m_j] = cos_phi
        temp_V[m_i][m_j] = sin_phi * -1
        temp_V[m_j][m_i] = sin_phi
        temp_A = numpy.dot(numpy.dot(temp_V.transpose(), temp_A), temp_V)
        # print(f"Кол-во итераций: {count}")
        # print(temp_A)
        eigenvectors = numpy.dot(eigenvectors, temp_V)
        count += 1
    print(f"Кол-во итераций: {count}")
    return temp_A, eigenvectors


# def check_matrix_simmetrix(matrix):
#     if(not numpy.all(matrix == matrix.transpose())):
#         print("Матрица не является симметричной!")
#         exit()

def not_diag_max_element(matrix):
    max = matrix[0][1]
    max_i = 0
    max_j = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(j > i):
            #if(j != i):
                if(abs(matrix[i][j]) > abs(max)):
                    max = matrix[i][j]
                    max_i = i
                    max_j = j
    return max_i, max_j


def not_diag_squares(matrix):
    sum = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(j > i):
            #if(j != i):
                sum += 2 * matrix[i][j] ** 2
    return sum


def task(matrix):
    print("Исходная матрица:")
    print(matrix)
    eigen_num, eigen_vects = jacobi_method(matrix)
    print("Матрица собственных значений(после метода):")
    for str in eigen_num:
        print('[', end = ' ')
        [print('{:.4e}'.format(j), end=' ') for j in str]
        print(']')
    print("Собственные значения(диагональ):")
    eigen_num_zeros = numpy.zeros(eigen_num.shape)
    for i in range(len(eigen_num_zeros)):
        eigen_num_zeros[i][i] = eigen_num[i][i]
    print(eigen_num_zeros.diagonal())
    print("Матрица свободных векторов:")
    print(eigen_vects)
    print("Матрица после операции V * A * V.T:")
    print(numpy.dot(numpy.dot(eigen_vects, eigen_num), eigen_vects.T))
    print("Определители матрицы для каждого соб. знач.")
    det_vect = []
    for i in range(len(eigen_num_zeros)):
        temp_m = matrix.copy()
        for j in range(len(matrix)):
            temp_m[j][j] -= eigen_num_zeros[i][i]
        det_vect.append(numpy.linalg.det(temp_m))
    print('[', end = ' ')
    [print('{:.4e}'.format(i), end = ' ') for i in det_vect]
    print(']')


if __name__ == "__main__":
    C = numpy.array([[0.2, 0, 0.2, 0, 0],
                     [0, 0.2, 0, 0.2, 0],
                     [0.2, 0, 0.2, 0, 0.2],
                     [0, 0.2, 0, 0.2, 0],
                     [0, 0, 0.2, 0, 0.2]])
    D = numpy.array([[2.33, 0.81, 0.67, 0.92, -0.53],
                     [0.81, 2.33, 0.81, 0.67, 0.92],
                     [0.67, 0.81, 2.33, 0.81, 0.92],
                     [0.92, 0.67, 0.81, 2.33, -0.53],
                     [-0.53, 0.92, 0.92, -0.53, 2.33]])
    A = numpy.array(3 * C + D)
    task(A)
    matrix = numpy.array([[0., 0., 0.],
                          [0., 7., 3.],
                          [0., 3., 4.]])
    task(matrix)
    matrix = numpy.array([[0., 3., 7.],
                          [3., 0., 11.],
                          [7., 11., 0.]])
    task(matrix)
    matrix = numpy.array([[3., 3., 3.],
                          [3., 3., 3.],
                          [3., 3., 3.]])
    task(matrix)
    matrix = numpy.array([[9., 8., 7.],
                          [4., 5., 6.],
                          [3., 2., 1.]])
    task(matrix)