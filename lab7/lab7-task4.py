def c(m, n):
    if m == 0 or m == n:
        return 1
    else:
        return c(m, n - 1) + c(m - 1, n - 1)


n, m = map(int, input('Введите n и m через пробел:').split())
ans = c(m, n)
print(ans)
