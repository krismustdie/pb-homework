surname = input('Введи свою фамилию: ')
name = input('Введи своё имя: ')
group = int(input('Введи номер своей группы: '))
email = input(f'Привет, {name} {surname.} из группы {group}!\nВведи свою электронную почту: ')
out = str(surname[0:5] + name[0:5] * 2 + email[0:5] * 3).lower
print(out)
