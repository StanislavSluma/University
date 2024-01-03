import numpy

C = numpy.array([[0.01, 0., -0.02, 0., 0.],
                 [0.01, 0.01, -0.02, 0., 0.],
                 [0., 0.01, 0.01, 0., 0.02],
                 [0., 0., 0.01, 0.01, 0],
                 [0., 0., 0., 0.01, 0.01]])
D = numpy.array([[1.33, 0.21, 0.17, 0.12, -0.13],
                 [-0.13, -1.33, 0.11, 0.17, 0.12],
                 [0.12, -0.13, -1.33, 0.11, 0.17],
                 [0.17, 0.12, -0.13, -1.33, 0.11],
                 [0.11, 0.67, 0.12, -0.13, -1.33]])
#b = numpy.array([1.2, 2.2, 4., 0., -1.2])
#A = numpy.array(3 * C + D)
b = numpy.array([1., 2., 3.])
# A = numpy.array([[1., 2., 3.],
#                  [2., 1., 3],
#                  [2., 3., 1.]])
A = numpy.array([[3., 0., 2.],
                  [2., 3., 2.],
                  [2., 0., 3.]])
X = numpy.zeros(len(A))
X_next = numpy.zeros(len(A))


def all_check():
    return check_on_row() or check_on_column() or check_norm()


def check_on_row():
    matrix = A.copy()
    for i in range(0, len(matrix)):
        summ = 0.
        for j in range(0, len(matrix)):
            if i != j:
                summ += abs(matrix[i][j])
        if summ > abs(matrix[i][i]):
            print(f"Сумма модулей по строке {i} ({summ}) больше модуля диагонального элемента {A[i][i]}")
            return False
    return True


def check_on_column():
    matrix = A.transpose()
    for i in range(0, len(matrix)):
        summ = 0.
        for j in range(0, len(matrix)):
            if i != j:
                summ += abs(matrix[i][j])
        if summ > abs(matrix[i][i]):
            print(f"Сумма модулей по столбцу {i} ({summ}) больше модуля диагонального элемента {A[i][i]}")
            return False
    return True


def check_norm():
    matrix = A.copy()
    summ = 0.
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i != j:
                summ += (matrix[i][j]/matrix[i][i]) ** 2
    if summ > 1:
        print(f"||B|| больше 1")
        return False
    return True


def iteration_method():
    global X, X_next
    X = numpy.zeros(len(A))
    X_next = numpy.zeros(len(A))
    check = True
    amount = 0
    while check:
        for i in range(0, len(A)):
            summ = 0.
            summ += b[i]
            for j in range(0, len(A)):
                if i != j:
                    summ -= A[i][j] * X[j]
            X_next[i] = summ / A[i][i]
        eps = X_next - X
        for i in range(0, len(eps)):
            eps[i] = abs(eps[i])
        max_eps = max(eps)
        if max_eps < 10 ** (-4):
            check = False
        X = X_next.copy()
        amount += 1
    print("Кол-во итераций: ", amount)


def zeidel_method():
    global X, X_next
    X = numpy.zeros(len(A))
    check = True
    amount = 0
    while check:
        X_next = X.copy()
        for i in range(0, len(A)):
            summ = 0.
            summ += b[i]
            for j in range(0, len(A)):
                if i != j:
                    summ -= A[i][j] * X_next[j]
            X_next[i] = summ / A[i][i]
        eps = X_next - X
        for i in range(0, len(eps)):
            eps[i] = abs(eps[i])
        max_eps = max(eps)
        if max_eps < 10 ** (-4):
            check = False
        X = X_next.copy()
        amount += 1
    print("Кол-во итераций: ", amount)

__name__ = '_anisimov_<3_'

if __name__ == '_anisimov_<3_':
    print("Исходная матрица:")
    for i in range(0, len(A)):
        print(f"{A[i]} = {b[i]}")
    if all_check():
        print("Решение методом простых итераций:")
        iteration_method()
        print("Вектор решений:")
        print(X)
        print("Получившийся вектор свободных значений:")
        res = numpy.dot(A, X)
        for i in range(0, len(res)):
            print("%.8f" % res[i], end = " ")
        print("\nОтклонение от изначального вектора свободных членов")
        print(res - b)
        print("Решение методом Зейделя:")
        zeidel_method()
        print("Вектор решений:")
        print(X)
        print("Получившийся вектор свободных значений:")
        res = numpy.dot(A, X)
        for i in range(0, len(res)):
            print("%.8f" % res[i], end = " ")
        print("\nОтклонение от изначального вектора свободных членов")
        print(res - b)
    else:
        print("Нельзя решить методом Зейдаля или простых итераций")
