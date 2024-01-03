from sympy import *
x = symbols('x')
y = symbols('y')

def simple_method(phi_x, phi_y, X):
    X_solve = Matrix(X)
    X_next = Matrix([[0.0], [0.0]])
    count = 0
    while count < 2000:
        X_next[0] = phi_x.subs([(x, X_solve[0]),(y, X_solve[1])])
        X_next[1] = phi_y.subs([(x, X_solve[0]),(y, X_solve[1])])
        if max(abs(X_next - X_solve)) < 10 ** (-4):
            print(f"Кол-во итераций {count}")
            return X_next
        X_solve = X_next.copy()
        count += 1
    print(count)
    return X_solve


def newton_method(f1, f2, X):
    X_solve = Matrix(X)
    J = Matrix([[f1.diff(x), f1.diff(y)], [f2.diff(x), f2.diff(y)]])
    F = Matrix([[f1], [f2]])
    count = 0
    while count < 2000:
        NumJ = get_numeric_matrix(J, X_solve)
        NumF = get_numeric_matrix(F, X_solve)
        if(NumJ.det() == 0):
            print("Определитель матрицы Якоби равен 0 :(")
            exit()
        X_next = X_solve - (NumJ ** (-1) * NumF)
        if(max(abs(X_next - X_solve)) < 10 ** (-4)):
            print(f"Кол-во итераций: {count}")
            return X_next
        X_solve = X_next.copy()
        count += 1
    return X_solve


def get_numeric_matrix(Matr, X_solve):
    Numeric = Matr.copy()
    tup = Matr.shape
    for i in range(0, tup[0] * tup[1]):
        Numeric[i] = Matr[i].subs([(x, X_solve[0]), (y, X_solve[1])])
    return Numeric


def task(f1, f2, phi_x, phi_y, X):
    print("----------------------BEGIN------------------------")
    print("Исходная система уравнений:")
    print(f"{f1} = 0")
    print(f"{f2} = 0")
    print("Приближение:")
    print(X)
    print("Метод простых итераций:")
    solve = simple_method(phi_x, phi_y, X)
    print("Вектор решений:")
    print(solve)
    print("Значение f1 в точке:", f1.subs([(x, solve[0]), (y, solve[1])]))
    print("Значение f2 в точке:", f2.subs([(x, solve[0]), (y, solve[1])]))
    print("Метод Ньютона:")
    solve = newton_method(f1, f2, X)
    print("Вектор решений:")
    print(solve)
    print("Значение f1 в точке:", f1.subs([(x, solve[0]), (y, solve[1])]))
    print("Значение f2 в точке:", f2.subs([(x, solve[0]), (y, solve[1])]))
    print("------------------------END-------------------------\n")

if __name__ == "__main__":
    m = 0.1
    a = 0.7
    f1 = tan(x * y + m) - x
    f2 = a * x ** 2 + 2 * y ** 2 - 1
    phi_x = tan(x * y + m)
    phi_y = sqrt(0.5 - (a / 2) * x ** 2)
    X = [0.3, 0.6]
    task(f1, f2, phi_x, phi_y, X)

    f1 = sin(x * y) ** x - x
    f2 = cos(x * y) ** y - y
    phi_x = sin(x*y) ** x
    phi_y = cos(x*y) ** y
    X = [0.6, 0.8]
    task(f1, f2, phi_x, phi_y, X)

    f1 = 5*x**2 - log(y) - y - 1
    f2 = y**2 - log(x) - 5*x - 1
    phi_x = (log(y) / 5 + y / 5 + 1 / 5) ** (1/2)
    phi_y = (log(x) + 5 * x + 1) ** (1/2)
    X = [0.9, 2.3]
    task(f1, f2, phi_x, phi_y, X)

    f1 = x ** 2 + x * y - 10
    f2 = y + 3 * x * y ** 2 - 57
    phi_x = (10 - x*y) ** (1/2)
    phi_y = -((57- y)/(3*x)) ** (1/2)
    X = [4.4, -2.0]
    task(f1, f2, phi_x, phi_y, X)

    f1 = tan(x) - sin(y)
    f2 = cot(y) - cos(x)
    phi_x = atan(sin(y))
    phi_y = acot(cos(x))
    X = [0.7, 0.9]
    task(f1, f2, phi_x, phi_y, X)

    f1 = sin(x*y) - x
    f2 = cos(x*y) - y
    phi_x = sin(x*y)
    phi_y = cos(x*y)
    X = [0.1, 0.9]
    task(f1, f2, phi_x, phi_y, X)

    f1 = x**2 - y - 1
    f2 = y**2 - x - 1
    phi_x = (y + 1) ** (1/2)
    phi_y = (x + 1) ** (1/2)
    X = [1.5, 1.7]
    task(f1, f2, phi_x, phi_y, X)

