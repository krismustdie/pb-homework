from math import sin, radians

# equation
x = float(input('Введите значение x: '))
if x < 0:
    print('Нет.')
else:
    y = (x + (x + x ** 0.5) ** 0.5) ** 0.5
    print('y =', y)

print('\n')

# geometry
r = float(input('Введите радиус вписанной окружности: '))
alpha = radians(float(input('Введите величину угла при основании в градусах: ')))
s = (4 * r ** 2) / sin(alpha)
print('S =', s)
