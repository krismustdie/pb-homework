from Sq_and_Rect import PrintSquare
from Sq_and_Rect import PrintRectangle


def Inp():
    with open('input.txt') as f:
        sides = [int(i) for i in f.readline().split()]
        f = f.readline()
        f = f[1:len(f) - 1]
    return sides, f


sides, f = Inp()
if len(sides) == 1:
    PrintSquare(*sides, f)
else:
    PrintRectangle(*sides, f)