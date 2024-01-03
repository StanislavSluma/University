from sympy import *
x = symbols('x')
y = symbols('y')


def euler_method(func, f_y0, left, right, accuracy, epsilon):
    tempY = -666.
    while True:
        X, Y = [], []
        n = int((right - left) / accuracy)
        X.append(left)
        Y.append(f_y0)
        for i in range(n):
            X.append(X[i] + accuracy)
            Y.append(Y[i] + accuracy * func.subs([(x, X[i]), (y, Y[i])]))
        if abs(tempY - Y[-1]) < epsilon:
            break
        tempY = Y[-1]
        accuracy /= 2
    return X, Y, accuracy


def modify_euler_method(func, f_y0, left, right, accuracy, epsilon):
    tempY = -666.
    while True:
        X, Y = [], []
        n = int((right - left) / accuracy)
        X.append(left)
        Y.append(f_y0)
        for i in range(n):
            X.append(X[i] + accuracy)
            Y.append(Y[i] + accuracy * func.subs([(x, X[i] + 0.5 * accuracy),
                                       (y, Y[i] + 0.5 * accuracy * func.subs([(x, X[i]), (y, Y[i])]))]))
        if abs(tempY - Y[-1]) < epsilon:
            break
        tempY = Y[-1]
        accuracy /= 2
    return X, Y, accuracy


def runge_kutta_method(func, f_y0, left, right, accuracy, epsilon):
    tempY = -666.
    while True:
        X, Y = [], []
        K = [0., 0., 0., 0.]
        n = int((right - left) / accuracy)
        X.append(left)
        Y.append(f_y0)
        for i in range(n):
            K[0] = accuracy * func.subs([(x, X[i]), (y, Y[i])])
            K[1] = accuracy * func.subs([(x, X[i] + 0.5 * accuracy), (y, Y[i] + 0.5 * K[0])])
            K[2] = accuracy * func.subs([(x, X[i] + 0.5 * accuracy), (y, Y[i] + 0.5 * K[1])])
            K[3] = accuracy * func.subs([(x, X[i] + accuracy), (y, Y[i] + K[2])])
            X.append(X[i] + accuracy)
            Y.append(Y[i] + (K[0] + 2 * K[1] + 2 * K[2] + K[3])/ 6)
        if abs(tempY - Y[-1]) < epsilon:
            break
        tempY = Y[-1]
        accuracy /= 2
    return X, Y, accuracy


def task(func, f_y0, left, right, accuracy, epsilon):
    print("Изначальное дифференциальное уравнение:")
    print(f"y' = {func}")
    print(f"Изначальный шаг: {accuracy}")
    print(f"Заданая точночть: {epsilon}")
    print(f"Точка для проверки значений: X0 = {(right - left) / 2}")

    print(f"Метод Эйлера")
    X1, Y1, h1 = euler_method(func, f_y0, left, right, accuracy, epsilon)
    index1 = int((right - left) / (2 * h1))
    print(f"Метод достиг указанной точности при h = {h1}")
    print("Значение в точке X0:")
    print('%.8f' % Y1[index1])

    print(f"Модернизированный метод Эйлера (h = {accuracy})")
    X2, Y2, h2 = modify_euler_method(func, f_y0, left, right, accuracy, epsilon)
    index2 = int((right - left) / (2 * h2))
    print(f"Метод достиг указанной точности при h = {h2}")
    print("Значение в точке X0:")
    print('%.8f' % Y2[index2])

    print(f"Метод Рунге-Кутта (h = {accuracy})")
    X3, Y3, h3 = runge_kutta_method(func, f_y0, left, right, accuracy, epsilon)
    index3 = int((right - left) / (2 * h3))
    print(f"Метод достиг указанной точности при h = {h3}")
    print("Значение в точке X0:")
    print('%.8f' % Y3[index3])


def problem(orig, func, f_y0, left, right, accuracy, epsilon):
    print("Изначальное дифференциальное уравнение:")
    print(f"y' = {func}")
    print(f"y = {orig}")
    print(f"Изначальный шаг: {accuracy}")
    print(f"Заданая точночть: {epsilon}")
    print(f"Точка для проверки значений: X0 = {(right - left) / 2}")
    print(f"Значение функции в точке: {orig.subs(x, (right - left) / 2)}")

    print(f"Метод Эйлера")
    X1, Y1, h1 = euler_method(func, f_y0, left, right, accuracy, epsilon)
    index1 = int((right - left) / (2 * h1))
    print(f"Метод достиг указанной точности при h = {h1}")
    print("Значение в точке X0:")
    print('%.8f' % Y1[index1])

    print(f"Модернизированный метод Эйлера (h = {accuracy})")
    X2, Y2, h2 = modify_euler_method(func, f_y0, left, right, accuracy, epsilon)
    index2 = int((right - left) / (2 * h2))
    print(f"Метод достиг указанной точности при h = {h2}")
    print("Значение в точке X0:")
    print('%.8f' % Y2[index2])

    print(f"Метод Рунге-Кутта (h = {accuracy})")
    X3, Y3, h3 = runge_kutta_method(func, f_y0, left, right, accuracy, epsilon)
    index3 = int((right - left) / (2 * h3))
    print(f"Метод достиг указанной точности при h = {h3}")
    print("Значение в точке X0:")
    print('%.8f' % Y3[index3])


if __name__ == '__main__':
    # a = 0.9
    # m = 2. + 1.
    # f_x_y = a * (1 - y ** 2)/(m * x**2 + y ** 2 + 1)
    # f_y0 = 0.
    # task(f_x_y, f_y0, 0., 1., 1., 0.001)

    orig = ln(cos(x))
    f_x_y = -tan(x)
    f_y0 = 0.
    #problem(orig, f_x_y, f_y0, 0., 1., 1., 0.0001)
    task(f_x_y, f_y0, 0., 1., 1., 0.0001)