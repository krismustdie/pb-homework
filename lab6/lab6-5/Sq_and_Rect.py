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
