import sympy
from sympy import *
x = symbols('x')

def lagrange_method(X, Y):
    f_x = 1
    L_x = 0
    for i in range(len(X)):
        f_x *= (x - X[i])
    for i in range(len(Y)):
        f_xj = f_x / (x - X[i])
        L_x += (f_xj / f_xj.subs(x, X[i])) * Y[i]
    return L_x


def newton_method(X, Y):
    N_x = Y[0]
    for i in range(1, len(X)):
        f_i = add_newton_f(X[:i + 1:], Y[:i + 1:])
        for j in range(i):
            f_i *= (x - X[j])
        N_x += f_i
    return N_x


def add_newton_f(X, Y):
    if(len(X) == 2):
        return (Y[1] - Y[0]) / (X[1] - X[0])
    a = add_newton_f(X[1::], Y[1::])
    b = add_newton_f(X[:-1:], Y[:-1:])
    return (a - b) / (X[-1] - X[0])


def problem(X, Y):
    print("Изначальные данные:")
    print("Xi:", end = '  ')
    print(X)
    print("Yi:  [", end=' ')
    [print('%.2f' % el, end=" ") for el in Y]
    print(']')

    print("Многочлен Лагранжа:")
    L_x = simplify(lagrange_method(X, Y))
    #print(L_x)
    solve = []
    for i in X:
        solve.append(L_x.subs(x, i))
    print("Значения в точках Xi:")
    print('Y[i]:  [', end=' ')
    [print('%.2f' % solve[i], end=" ") for i in range(len(solve))]
    print(']')
    print("Значения в точке 0.47:")
    print(L_x.subs(x, 0.47))
    print("Отклонение от изначальных значений:")
    error = []
    for i in range(len(solve)):
        error.append(Y[i] - solve[i])
    print('[', end = ' ')
    [print('%.1e' % error[i], end = " ") for i in range(len(error)// 2)]
    print()
    [print('%.1e' % error[i], end = " ") for i in range(len(error)// 2, len(error))]
    print(']')

    print("Многочлен Ньютона:")
    N_x = simplify(newton_method(X, Y))
    #print(N_x)
    solve = []
    for i in X:
        solve.append(N_x.subs(x, i))
    print("Значения в точках Xi:")
    print('Y[i]:  [', end=' ')
    [print('%.2f' % el, end=" ") for el in solve]
    print(']')
    print("Значения в точке 0.47:")
    print(N_x.subs(x, 0.47))
    print("Отклонение от изначальных значений:")
    error = []
    for i in range(len(solve)):
        error.append(Y[i] - solve[i])
    print('[', end=' ')
    [print('%.1e' % error[i], end=" ") for i in range(len(error) // 2)]
    print()
    [print('%.1e' % error[i], end=" ") for i in range(len(error) // 2, len(error))]
    print(']')


def task(left, right, point_amount, function):
    print("Изначальная функция:")
    print(function)
    print("Изначальные данные:")
    X = []
    for i in range(point_amount + 2):
        X.append(left + (right - left)/(point_amount + 1) * i)
    print("Xi:  [", end=' ')
    [print('%.4f' % el, end=" ") for el in X]
    print(']')
    Y = []
    for i in range(len(X)):
        Y.append(function.subs(x, X[i]))
    print("Yi:  [", end=' ')
    [print('%.4f' % el, end=" ") for el in Y]
    print(']')

    print("Многочлен Лагранжа:")
    L_x = simplify(lagrange_method(X, Y))
    #print(L_x)
    print(f"Максимальное отклонение от {function}:")
    max = sympy.maximum(function - L_x, x, Interval(left, right))
    min = sympy.minimum(function - L_x, x, Interval(left, right))
    if abs(min) >= max:
        print(min)
    else:
       print(max)
    print("Многочлен Ньютона:")
    N_x = simplify(newton_method(X, Y))
    #print(N_x)
    print(f"Максимальное отклонение от {function}:")
    max = sympy.maximum(function - N_x, x, Interval(left, right))
    min = sympy.minimum(function - N_x, x, Interval(left, right))
    if abs(min) >= max:
        print(min)
    else:
        print(max)


if __name__ == '__main__':
    # X = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]
    # Y = [0., 0.41, 0.79, 1.13, 1.46, 1.76, 2.04, 2.3, 2.55, 2.79, 3.01]
    # k = 3
    # m = 1.5
    # for i in range(len(Y)):
    #     Y[i] += m*(-1)**k
    # problem(X, Y)
    for i in range(0, 6):
        task(1, 4, i*3 + 2, sin(x))