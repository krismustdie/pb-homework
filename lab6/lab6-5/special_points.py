import datetime as dt


def point_inp():
    with open('input.txt') as f:
        r = int(f.readline())
        x, y = map(int, f.readline().split())
    return r, x, y


def Radius(R, x, y):
    x1 = x - R
    x2 = x + R
    y1 = y - R
    y2 = y + R
    return x1, x2, y1, y2


def point_count(R, x, y):
    counter = 0
    x1, x2, y1, y2 = Radius(R, x, y)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if ((i ** 2 + j ** 2) ** 0.5) <= R:
                counter += 1
    return counter


def point_out(start, finish, ans):
    time = round(dt.datetime.timestamp(finish) - dt.datetime.timestamp(start), 2)
    start.strftime('%m/%d/%y %H:%M:%S')
    output = f'{start.strftime("%d.%m.%Y %H:%M")}\n{ans}\n{time}'
    with open('output.txt', 'w') as f:
        f.write(output)