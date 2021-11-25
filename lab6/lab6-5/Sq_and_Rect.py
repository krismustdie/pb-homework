def SR_Inp():
    with open('input.txt') as f:
        sides = [int(i) for i in f.readline().split()]
        f = f.readline()
        f = f[1:len(f) - 1]
    return sides, f


def PrintRectangle(a, b, file):
    with open(file, 'w') as f:
        f.write('* ' * a + '\n')
        for _ in range(b - 2):
            f.write('* ' + '  ' * (a - 2) + '*' + '\n')
        f.write('* ' * a)



def PrintSquare(a, file):
    with open(file, 'w') as f:
        f.write('* ' * a + '\n')
        for _ in range(a - 2):
            f.write('* ' + '  ' * (a - 2) + '*' + '\n')
        f.write('* ' * a)


