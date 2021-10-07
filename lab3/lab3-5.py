surname = input('Введи свою фамилию: ')
name = input('Введи своё имя: ')
group = int(input('Введи номер своей группы: '))
email = input('Привет, %s %s из группы %d!\nВведи свою электронную почту? ' % (name, surname, group))
out = surname[0:5] + name[0:5] * 2 + email[0:5] * 3
print(out.lower())
