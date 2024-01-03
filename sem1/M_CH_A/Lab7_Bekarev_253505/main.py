import sympy, numpy
from sympy import *
import matplotlib.pyplot as plt
x = symbols('x')

def spline_method(left, right, point_amount, func):
    point_amount += 2
    X = []
    Y = []
    A = []
    B = []
    C = []
    D = []
    S = []
    alpha = []
    betta = []
    for i in range(point_amount):
        X.append(left + (right - left)/(point_amount - 1) * i)
        Y.append(func.subs(x, X[i]))

    alpha.append(-1 * (X[2] - X[1]) / (2 * (X[2] - X[0])))
    betta.append((((Y[2] - Y[1]) / (X[2] - X[1])) - ((Y[1] - Y[0]) / (X[1] - X[0]))) / (X[2] - X[0]) * 3 / 2)
    for i in range(1, point_amount - 2):
        a = (X[i + 1] - X[i]) / 3
        b = 2 * ((X[i + 2] - X[i]) / 3)
        c = (X[i + 2] - X[i + 1]) / 3
        d = (((Y[i + 2] - Y[i + 1]) / (X[i + 2] - X[i + 1])) - ((Y[i + 1] - Y[i]) / (X[i + 1] - X[i])))
        alpha.append(-1 * c / (a * alpha[i - 1] + b))
        betta.append((d - a * betta[i - 1]) / (a * alpha[i - 1] + b))

    alpha.reverse()
    betta.reverse()
    C.append(betta[0])
    for i in range(1, point_amount - 1):
        C.append(alpha[i - 1] * C[i - 1] + betta[i - 1])
    C.append(0.)
    C.reverse()

    for i in range(point_amount - 1):
        B.append((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]) - C[i] * (X[i + 1] - X[i]) - ((C[i + 1] - C[i]) * (X[i + 1] - X[i]) / 3))
        D.append((C[i + 1] - C[i]) / (3 * (X[i + 1] - X[i])))
        A.append(Y[i])

    f = x
    for i in range(point_amount - 1):
        f = A[i] + B[i]*(x - X[i]) + C[i]*(x - X[i])**2 + D[i]*(x - X[i])**3
        S.append((f, x <= X[i+1]))
    S.append((f, x > X[i+1]))
    S = Piecewise(*S)
    return S, X


def task(left, right, point_amount, func, test_point):
    print(f"Изначальная функция F(x): {func}")
    S_x, X = spline_method(left, right, point_amount, func)
    #print(S_x)
    print("Узловые точки:")
    print('[', end = '')
    [print('%.4f' % X[i], end = ' ') for i in range(len(X))]
    print(']')

    print(f"Значения в точке x = (b - a) * 0.5: ({(right - left) * 0.5})")
    print(f"S(x) = {S_x.subs(x, (right - left) * 0.5)}")
    print(f"F(x) = {func.subs(x, (right - left) * 0.5)}")
    print("Разность F(x) - S(x) в данной точке:")
    print((func - S_x).subs(x, (right - left) * 0.5))

    print(f"Значения в тестовой точке x: ({test_point})")
    print(f"S(x) = {S_x.subs(x, test_point)}")
    print(f"F(x) = {func.subs(x, test_point)}")
    print("Разность F(x) - S(x) в данной точке:")
    print((func - S_x).subs(x, test_point))

    print("График функции:")
    f_lambda = sympy.lambdify(x ,func, 'numpy')
    x_values = numpy.linspace(left - 0.5, right + 3, 100)
    y_values = f_lambda(x_values)
    plt.plot(x_values, y_values, label = f'f(x) = {func}')
    f_lambda = sympy.lambdify(x, S_x, 'numpy')
    x_values = numpy.linspace(left - 0.5, right + 3, 100)
    y_values = f_lambda(x_values)
    plt.plot(x_values, y_values, label='S(x)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    task(1, 5, 8, log(x), 2.)