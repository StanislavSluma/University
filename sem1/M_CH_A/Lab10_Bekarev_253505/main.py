from sympy import *
x, y = symbols("x y")


def adams_method(func, f_y0, left, right, step, accuracy):
    tempY = -666.
    while True:
        X, Y = [], []
        n = int((right - left) / step)
        X.append(left)
        Y.append(f_y0)
        X.append(left + step)
        # Y1 находим с помощью модифицированного метода Эйлера
        Y.append(Y[0] + step * func.subs([(x, X[0] + 0.5 * step),
                                              (y, Y[0] + 0.5 * step * func.subs([(x, X[0]), (y, Y[0])]))]))
        for i in range(1, n):
            X.append(X[i] + step)
            Y.append(Y[i] + 0.5 * step * (3 * func.subs([(x, X[i]), (y, Y[i])]) - func.subs([(x, X[i - 1]), (y, Y[i - 1])])))
        if abs(tempY - Y[-1]) < accuracy:
            break
        tempY = Y[-1]
        step /= 2
    return X, Y, step


def task(func, f_y0, left, right, step, accuracy):
    print("Изначальное дифференциальное уравнение:")
    print(f"y' = {func}")
    print(f"Изначальный шаг: {step}")
    print(f"Заданная точность: {accuracy}")
    print(f"Точка для проверки значений: X0 = {(right - left) / 2}")
    print("Метод Адамса")
    X, Y, H = adams_method(func, f_y0, left, right, step, accuracy)
    print(f"Метод достиг указанной точности при h = {H}")
    print("Значение в точке X0:")
    index = int((right - left) / (2 * H))
    print(Y[index])


def problem(orig, func, f_y0, left, right, step, accuracy):
    print("Изначальное дифференциальное уравнение:")
    print(f"y' = {func}")
    print("Решение:")
    print(f"y = {orig}")
    print(f"Изначальный шаг: {step}")
    print(f"Заданная точность: {accuracy}")
    print(f"Точка для проверки значений: X0 = {(right - left) / 2}")
    print("Значение функции в точке X0:")
    print(orig.subs(x, (right - left) / 2))
    print("Метод Адамса")
    X, Y, H = adams_method(func, f_y0, left, right, step, accuracy)
    print(f"Метод достиг указанной точности при h = {H}")
    print("Значение в точке X0:")
    index = int((right - left) / (2 * H))
    print(Y[index])
    print("Погрешность:")
    print(orig.subs(x, (right - left) / 2) - Y[index])


if __name__ == '__main__':
    a = 0.9
    m = 2. + 1.
    f_x_y = a * (1. - y ** 2.) / (m * x ** 2. + y ** 2. + 1.)
    f_y0 = 0.
    task(f_x_y, f_y0, 0., 1., 1., 0.001)

    # orig = ln(cos(x))
    # f_x_y = -tan(x)
    # f_y0 = 0.
    # problem(orig, f_x_y, f_y0, 0., 1., 1., 0.00001)
