"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

user_number = int(input("Введите целое положительное число "))
while user_number < 0:
    print(f"Вы ввели {user_number}")
    user_number = int(input("Введите целое положительное число "))
temp_number = user_number
max_digit = temp_number % 10
while temp_number // 10 > 0:
    temp_number //= 10
    if temp_number % 10 > max_digit:
        max_digit = temp_number % 10
print(f"Самой большой цифрой в числе {user_number} является цифра: {max_digit}")
