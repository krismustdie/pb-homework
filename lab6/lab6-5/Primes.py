def Inp_Pr():
    with open('input.txt') as f:
        a = int(f.readline())
    return a


def Eratosthenes(n):
    alls = [i for i in range(2, n+1)]
    k = 0
    while k < len(alls):
        p = alls[k]
        for i in range(p*2, n+1, p):
            try:
                alls.remove(i)
            except ValueError:
                continue
        k += 1
    return alls


def Out_Pr(l):
    with open('output.txt', 'w') as f:
        out = ''
        for k in l:
            out += f'{k} '
        f.write(f'{out}')
