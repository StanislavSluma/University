import sympy
from sympy import *
x = symbols('x')


def diff_method_1(func, point, step, accuracy):
    prev = (func.subs(x, point + step) - func.subs(x, point)) / step
    while(True):
        step /= 2
        diff = (func.subs(x, point + step) - func.subs(x, point)) / step
        if abs(diff - prev) <= accuracy:
            return diff, step
        prev = diff

def diff_method_2(func, point, step, accuracy):
    prev = (func.subs(x, point + step) - func.subs(x, point - step)) / (2 * step)
    while (True):
        step /= 2
        diff = (func.subs(x, point + step) - func.subs(x, point - step)) / (2 * step)
        if abs(diff - prev) <= accuracy:
            return diff, step
        prev = diff


def diff2_method(func, point, step, accuracy):
    prev = (func.subs(x, point + step) - 2 * func.subs(x, point) + func.subs(x, point - step)) / (step ** 2)
    while (True):
        step /= 2
        diff = (func.subs(x, point + step) - 2 * func.subs(x, point) + func.subs(x, point - step)) / (step ** 2)
        if abs(diff - prev) <= accuracy:
            return diff, step
        prev = diff


def integral_middle_rectangle(func, left, right, step, accuracy):
    prev = 666.
    while True:
        i = left
        Integ = 0.
        while i < right - 0.5 * step:
            Integ += step * func.subs(x, i + 0.5 * step)
            i += step
        if abs(Integ - prev) <= accuracy:
            return Integ, step
        prev = Integ
        step /= 2


def integral_trapezoid(func, left, right, step, accuracy):
    prev = 666.
    while True:
        i = left + step
        Integ = float(step * (func.subs(x, left) + func.subs(x, right)) / 2)
        while i < right - 0.9 * step:
            Integ += step * float(func.subs(x, i))
            i += step
        if abs(Integ - prev) <= accuracy:
            return Integ, step
        prev = Integ
        step /= 2


def simpthon_method(func, left, right, step, accuracy):
    prev = 666.
    while True:
        X, Y = [], []
        check = False
        i = left
        while i < right + 0.5 * step:
            X.append(i)
            i += step
        if(len(X) % 2 == 0):
            X.append(float(right + step))
            check = True
        for i in range(0, len(X)):
            Y.append(float(func.subs(x, X[i])))
        Integ = 0.
        j = 0
        while j < len(Y) - 2:
            Integ += Y[j] + 4 * Y[j + 1] + Y[j + 2]
            j += 2
        if(check):
            Integ -= 0.5 * (Y[len(Y) - 3] + 4. * Y[len(Y) - 2] + Y[len(Y) - 1])
        Integ *= (step / 3)
        if abs(Integ - prev) <= accuracy:
            return Integ, step
        prev = Integ
        step /= 2


def task(func, point, left, right, step, accuracy):
    print(f"Изначальная функция f(x): {func}")
    print(f"Заданная точность: {accuracy}")
    print(f"Производная в точке {point}:")
    dif = diff(func, x).subs(x, point)
    print(dif, '\n')

    print("1-ая формула производной:")
    print("Y'[k] = (Y[k]-Y[k-1])/(X[k]-X[k-1])")
    diff1, h = diff_method_1(func, point, step, accuracy)
    print(diff1)
    print(f"Точность была достигнута при шаге: {h}\n")

    print("2-ая формула производной:")
    print("Y'[k] = (Y[k+1]-Y[k-1])/(X[k+1]-X[k-1])")
    diff2, h = diff_method_2(func, point, step, accuracy)
    print(diff2)
    print(f"Точность была достигнута при шаге: {h}\n")

    print(f"Вторая производная в точке {point}:")
    diffdiff = diff(diff(func, x), x).subs(x, point)
    print(diffdiff)
    print("Формула второй производной:")
    print("Y''[k] = (Y'[k+1]-Y'[k-1])/(X[k+1]-X[k-1])")
    diffdiff1, h = diff2_method(func, point, step, accuracy)
    print(diffdiff1)
    print(f"Точность была достигнута при шаге: {h}\n")

    # print(f"Интеграл ф-ии {func} на интервале({left}, {right}):")
    # Int = integrate(func, x).subs(x, right) - integrate(func, x).subs(x, left)
    # print(Int, "\n")

    print("Метод средних прямоугольников")
    Int1, h = integral_middle_rectangle(func, left, right, step, accuracy)
    print(Int1)
    print(f"Точность была достигнута при шаге: {h}\n")

    print("Метод трапеций")
    Int2, h = integral_trapezoid(func, left, right, step, accuracy)
    print(Int2)
    print(f"Точность была достигнута при шаге: {h}\n")

    print("Метод Симпсона")
    Int3, h = simpthon_method(func, left, right, step, accuracy)
    print(Int3)
    print(f"Точность была достигнута при шаге: {h}\n")


if __name__ == '__main__':
    func = x**x
    task(func, 1.5, 1., 2., 0.5, 1e-4)

