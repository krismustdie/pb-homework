from sorts import *
from random import randint
from prettytable import PrettyTable
from time import time
from os import startfile


def timers(A):
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


A = [randint(0, 50) for _ in range(10000)]
B = sorted(A)
C = sorted(A, reverse=True)
random_list = timers(A)
sort_list = timers(B)
rev_list = timers(C)

out = PrettyTable()
out.add_column("Вид сортировки", ["Сортировка пузырьком", "Сортировка слиянием", "Быстрая сортировка", "Встроенная "
                                                                                                       "функция"])
out.add_column("Случайная", random_list)
out.add_column("Отсортированная", sort_list)
out.add_column("Отсортированная в обратном порядке", rev_list)

with open('output.txt', 'w') as f:
    f.write(f'Количеcтво элементов последовательности: {len(A)}\n')
    f.write(out.get_string())

print('Выполнение завершено')
if input('Открыть файл с отчётом? (Y/N) ') == 'Y':
    startfile('output.txt')
