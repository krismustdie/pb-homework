# Составной оператор присваивания объединяет в себе простое присваивание и арифметическую бинарную операцию (+=, -= и т.д).

number = 9.0

print("number = " + str(number))

number -= 2

print("number = " + str(number))

number += 5
print(number)

# Попрактикуйтесь в использовании разных типов составных операторов для переменной number, выведите результаты в консоль

number **= 2
print("number = " + str(number))

number %= 3
print("number = " + str(number))

number += 2
print("number = " + str(number))

number *= 7
print("number = " + str(number))
