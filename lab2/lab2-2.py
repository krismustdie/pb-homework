# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))   # Вывод типа переменной number

float_number = 9.0
print(type(float_number))

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

my_string = '1234'
print(type(my_string))

boooo = False
print(type(boooo))


# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
print(int(float_number))
print(float(my_string))
print(str(boooo))