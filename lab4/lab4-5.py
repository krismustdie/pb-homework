# создаём пустые словари
surname = {}
name = {}
patr = {}
birth_year = {}
disease = {}
# считываем данные призывников
for i in range(1, 3):
    name[str(i)] = input("Введите имя: ")
    surname[str(i)] = input("Введите фамилию: ")
    patr[str(i)] = input("Введите отчество: ")
    birth_year[str(i)] = input("Введите год рождения: ")
    disease[str(i)] = input("Введите имеющееся заболевание или 'нет', в случае их отсутствия: ")
# выводим данные
print('{:25s}{:25s}{:25s}{:25s}{:25s}{:25s}'.format("№", 'Фамилия', 'Имя', 'Отчество', 'Год рождения', 'Заболевание'))
for i in range(1, 3):
    k = str(i)
    print(
        '{:25s}{:25s}{:25s}{:25s}{:25s}{:25s}'.format(k, surname[k], name[k], patr[k], birth_year[k], disease[k]))
