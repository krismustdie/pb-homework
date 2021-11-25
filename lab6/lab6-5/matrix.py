import numpy as np


def Print_Matrix(A):
    temp = ''
    for i in A:
        for j in i:
            temp += f'{j:5.1f}'
        temp += '\n'
    return temp


def Matrix_Inp():
    with open('input.txt') as f:
        n, m = map(int, f.readline().split())
    return n, m


def Rand_Matrix(n, m):
    A = np.random.randint(0, 10, (n, m))
    k = int(np.random.randint(5, 15, 1))
    B = np.random.randint(0, 10, (m, k))
    return A, B


def Matrix_Max_Div(A):
    temp = []
    for k in A:
        temp.append(k / max(k))
    return np.array(temp)


def Mult_Matrix(A, B):
    C = np.dot(A, B)
    return C


def Matrix_Out(a, b, c):
    output = f'Матрица A:\n{Print_Matrix(a)}Матрица B:\n{Print_Matrix(b)}Матрица A*B:\n{Print_Matrix(c)}'
    with open('output.txt', 'w') as f:
        f.write(output)
