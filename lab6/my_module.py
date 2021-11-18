# Модули в Python - это просто файлы Python с расширением .py, содержащие функции и операторы Python. Модули могут
# быть полезны, когда вы хотите использовать свою функцию в ряде программ без копирования ее определения в каждую
# программу. Модули импортируются в другие файлы с помощью ключевого слова import и имени файла без расширения. При
# первой загрузке модуля в работающий скрипт Python он инициализируется однократным выполнением кода в модуле.


def hello_world(name):
	print(f"Hello, world! My name is {name}")
