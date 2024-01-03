from sympy import *

x = symbols('x')
a = 4
b = 16
c = 16
beg_left = -10
beg_right = 10
f = a * x**2 + b * x + c
roots_amount = degree(f)
roots_bound = []
f_diff = diff(f)
f_arr = list()
f_arr.append(f)
f_arr.append(f_diff)


def get_sign_changes(left, right):
    Nleft = 0
    Nright = 0
    for i in range(0, len(f_arr) - 1):
        if f_arr[i].subs(x, left) * f_arr[i + 1].subs(x, left) < 0:
            Nleft += 1
    for i in range(0, len(f_arr) - 1):
        if f_arr[i].subs(x, right) * f_arr[i + 1].subs(x, right) < 0:
            Nright += 1
    return Nleft - Nright


def search_root_range(left, right):
    while True:
        amount = get_sign_changes(left, right)
        if amount >= 2:
            right = right - (right - left) / 2
        elif amount == 0:
            left = right
            right = right + (right - left) / 2
        elif amount == 1:
            while right - left > 2:
                middle = (right + left) / 2
                if get_sign_changes(left, middle) > get_sign_changes(middle, right):
                    right = middle
                else:
                    left = middle
            roots_bound.append((left, right))
            break


def search_allroots_range(left, right):
    curr_left = left
    for i in range(0, roots_amount):
        search_root_range(curr_left, right)
        curr_left = roots_bound[i][1]


def shturm_theory():
    global roots_amount
    for i in range(0, degree(f) - 1):
        f_arr.append(-1 * div(f_arr[i], f_arr[i + 1])[1])
    roots_amount = get_sign_changes(beg_left, beg_right)
    print(f"Кол-во корней на промежутке [{beg_left}, {beg_right}]: {roots_amount}")
    search_allroots_range(beg_left, beg_right)
    print("Границы корней уравнения:")
    print(roots_bound)


def binary_method(left, right):
    count = 1
    while True:
        middle = (left + right) / 2
        if right - left < 10 ** (-4):
            print(f"Кол-во итераций: {count}")
            return middle
        elif f.subs(x, middle) * f.subs(x, right) <= 0:
            left = middle
        else: #elif f.subs(x, left) * f.subs(x, middle) <= 0:
            right = middle
        count += 1


def chord_method(left, right):
    count = 1
    if f.subs(x, left) * diff(diff(f)).subs(x, left) < 0:
        curr = right
        while True:
            next = curr - (f.subs(x, curr) * (left - curr)) / (f.subs(x, left) - f.subs(x, curr))
            if(abs(curr - next) < 10 ** (-8)):
                print(f"Кол-во итераций: {count}")
                return (next + curr) / 2
            curr = next
            count += 1
    elif f.subs(x, right) * diff(diff(f)).subs(x, right) < 0:
        curr = left
        while True:
            next = curr - (f.subs(x, curr) * (right - curr)) / (f.subs(x, right) - f.subs(x, curr))
            if (abs(next - curr) < 10 ** (-8)):
                print(f"Кол-во итераций: {count}")
                return (next + curr) / 2
            curr = next
            count += 1
    else:
        print("Proizoshla malenkaya oploschnost :(")
        exit()


def newton_method(left, right):
    if f.subs(x, left)/diff(f).subs(x, left) - left < right - f.subs(x, right)/diff(f).subs(x, right):
        curr = left
    else:
        curr = right
    count = 1
    while True:
        next = curr - (f.subs(x, curr) / diff(f).subs(x, curr))
        if abs(curr - next) < 10 ** (-4):
            print(f"Кол-во итераций: {count}")
            return (next + curr) / 2
        curr = next
        count += 1


if __name__ == '__main__':
    print("Исходная функция:")
    print(f"f(x) = {f}")
    shturm_theory()
    # print("Метод половинного деления:")
    # root_bin = binary_method(roots_bound[0][0], roots_bound[0][1])
    # print(root_bin)
    # print("После подставления найденного корня имеем:")
    # print(f.subs(x, root_bin))
    # print("Метод хорд:")
    # root_chord = chord_method(roots_bound[0][0], roots_bound[0][1])
    # print(root_chord)
    # print("После подставления найденного корня имеем:")
    # print(f.subs(x, root_chord))
    print("Метод Ньютона:")
    root_newton = newton_method(roots_bound[0][0], roots_bound[0][1])
    print(root_newton)
    print("После подставления найденного корня имеем:")
    print(f.subs(x, root_newton))
