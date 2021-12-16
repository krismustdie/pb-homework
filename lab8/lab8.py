from sorts import *
from random import randint
from prettytable import PrettyTable
from time import time
from os import startfile


def timers(A): # Функция, проверяющая время, необходимое для сортировки массива заданными способами.
    start = time()
    Bubble_Sort(A)
    bubble = time() - start

    start = time()
    Merge_Sort(A)
    merge = time() - start

    start = time()
    Quick_Sort(A)
    quick = time() - start

    start = time()
    sorted(A)
    pyth = time() - start

    return ['%s' % bubble, '%s' % merge, '%s' % quick, '%s' % pyth]

# Создание массивов и запуск функции измерения времени
A = [randint(0, 50) for _ in range(10000)]
B = sorted(A)
C = sorted(A, reverse=True)
random_list = timers(A)
sort_list = timers(B)
rev_list = timers(C)

# Создание отчёта в виде таблицы
out = PrettyTable()
out.add_column("Вид сортировки", ["Сортировка пузырьком", "Сортировка слиянием", "Быстрая сортировка", "Встроенная "
                                                                                                       "функция"])
out.add_column("Случайная", random_list)
out.add_column("Отсортированная", sort_list)
out.add_column("Отсортированная в обратном порядке", rev_list)

# Запись таблицы в текстовый файл
with open('output.txt', 'w') as f:
    f.write(f'Количеcтво элементов последовательности: {len(A)}\n')
    f.write(out.get_string())

# Сообщение пользователю о завершении программы
if input('Выполнение завершено\nОткрыть файл с отчётом? (Y/N) ') == 'Y':
    startfile('output.txt')
