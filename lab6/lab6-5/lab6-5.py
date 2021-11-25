from Sq_and_Rect import *
from about_num import *
from Primes import *
from matrix import *
from special_points import *
from datetime import datetime


def rec_sq():
    sides, f = SR_Inp()
    if len(sides) == 1:
        PrintSquare(*sides, f)
    else:
        PrintRectangle(*sides, f)


def num_inf():
    try:
        number = num_inp()
        num_k = num_count(number)
        num_s = num_sum(number)
        num_m = num_mult(number)
        num_out(number, num_k, num_s, num_m)
    except FileNotFoundError:
        print('Файл с входными данными не обнаружен')



def simple():
    try:
        a = Inp_Pr()
        prime_list = Eratosthenes(a)
        Out_Pr(prime_list)
    except FileNotFoundError:
        print('Файл с входными данными не обнаружен')


def points():
    start = datetime.now()
    R, x, y = point_inp()
    ans = point_count(R, x, y)
    finish = datetime.now()
    point_out(start, finish, ans)
    pass


def matr():
    n, m = Matrix_Inp()
    A, B = Rand_Matrix(n, m)
    C = Mult_Matrix(Matrix_Max_Div(A), B)
    Matrix_Out(A, B, C)
    pass


com = int(input('''Введите номер программы:
[1] Прямоугольники и квадраты
[2] Всё о  цифрах в числе
[3] Генератор простых чисел
[4] Особые точки
[5] Матрицы
'''))
if com == 1:
    rec_sq()
elif com == 2:
    num_inf()
elif com == 3:
    simple()
elif com == 4:
    points()
elif com == 5:
    matr()
else:
    print('Неверный номер программы')
