soldiers = {}
for _ in range(5):
    name = str(input('Введите ФИО: '))
    soldiers[name] = (input("Введите год рождения и заболевание: ").split(" "))

print(f'{"№":2}{"ФИО":40}{"Год рождения":25}{"Заболевание":25}')
n = 1
for key, value in soldiers.items():
    print(f'{str(n):2}{key:40}{value[0]:25}{value[1]:25}')
    n += 1
