def num_inp():
    with open('input.txt') as f:
        a = f.readline().split()[0]
    return a


def num_count(a):
    k = len(a)
    return k


def num_sum(a):
    s = 0
    for i in a:
        s += int(i)
    return s


def num_mult(a):
    m = 1
    for i in a:
        m *= int(i)
    return m


def num_out(n, k, s, m):
    out = (f'''Число: {n}
Количество цифр: {k}
Сумма цифр: {s}
Произведение цифр: {m}''')
    with open('output1.txt', 'w') as f:
        f.write(out)
