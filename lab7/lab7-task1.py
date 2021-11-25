def p(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * p(n - 1, x) - (n - 1) * p(n - 2, x)) / n


n, x = map(float, input('Введите n и x через пробел:').split())
for i in range(int(n) + 1):
    ans = p(i, x)
    print(ans)
