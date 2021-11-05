def Inp_Rub():
    # Получение входных данных с клавиатуры
    k = int(input('Введите общую сумму покупок в копейках: '))
    return k


def Rub_Count(k):
    # Подсчёт количества рублей и копеек по заданному количеству копеек
    rub = k // 100
    kop = k % 100
    return rub, kop


def Gram_Case(rub, kop):
    # Определение необходимого падежа для вывода
    if rub == 0:
        rub_out = ''
    elif (9 < rub % 100 < 20) or (rub % 10 == 0) or (rub % 10 > 4):
        rub_out = f'{rub} РУБЛЕЙ \n'
    elif rub % 10 == 1:
        rub_out = f'{rub} РУБЛЬ \n'
    else:
        rub_out = f'{rub} РУБЛЯ \n'
    if kop == 0:
        kop_out = ''
    elif (9 < kop % 100 < 20) or (kop % 10 == 0) or (kop % 10 > 4):
        kop_out = f'{kop} КОПЕЕК \n'
    elif kop % 10 == 1:
        kop_out = f'{kop} КОПЕЙКА \n'
    else:
        kop_out = f'{kop} КОПЕЙКИ \n'
    return rub_out + kop_out


def Out_Rub(out):
    # Вывод ответа на экран
    print(out)


def money():
    # вычисление суммы покупок в рублях и копейках по заданной общей сумме в копейках
    k = Inp_Rub()
    rub, kop = Rub_Count(k)
    output = Gram_Case(rub, kop)
    Out_Rub(output)


def Inp_Eq():
    # Получение с клавиатуры коэффициентов квадратного уравнения
    inp = map(float, input('Введите коэффициенты a, b, c через пробел: ').split())
    return inp


def Disc(a, b, c):
    # Вычисление дискриминанта
    D = (b * b) - (4 * a * c)
    return D


def Roots(a, b, D):
    # Нахождение корней
    roots_list = []
    if D >= 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        roots_list.append(x1)
        if x1 != x2:
            roots_list.append(x2)
        roots_list.sort()
    return roots_list


def Out_Eq(a, b, c, roots_list):
    # Вывод данных
    print(f'''Уравнение:
({a:.5f})*X^2 + ({b:.5f})*X + ({c:.5f}) = 0
Количество корней: {len(roots_list)}''')
    if len(roots_list) != 0:
        print(f"{roots_list[0]:.5f}")
        print(f"{roots_list[-1]:.5f}")


def equation():
    # нахождение корней квадратного уравнения по заданным коэффициентам
    a, b, c = Inp_Eq()
    D = Disc(a, b, c)
    roots_list = Roots(a, b, D)
    Out_Eq(a, b, c, roots_list)


def Inp_Tr():
    # Получение длин сторон треугольника с клавиатуры
    inp = map(float, input("Введите длины сторон треугольника через пробел: ").split())
    return inp


def Kinds(a, b, c):
    # Определение вида треугольника
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or c + b <= a:
        kind = 0
    elif a == b == c:
        kind = 1
    elif a == b or b == c or a == c:
        kind = 2
    else:
        kind = 3
    return kind


def Out_Tr(kind):
    # Вывод полученного результата
    if kind == 0:
        print('Треугольник не существует')
    elif kind == 1:
        print('Треугольник равносторонний')
    elif kind == 2:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник общего вида')


def triangle():
    # Определение и вывод вида треугольника по заданным сторонам
    a, b, c = Inp_Tr()
    kind = Kinds(a, b, c)
    Out_Tr(kind)


com = int(input('''Введите номер программы:
[1] Копейка рубль бережёт
[2] Квадратное уравнение
[3] Вид треугольника
'''))
if com == 1:
    money()
elif com == 2:
    equation()
else:
    triangle()
