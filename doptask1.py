"""
1. Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.
"""
day_number = int(input("Введите номер дня недели "))
while day_number > 7 or day_number < 1:
    print("Такого дня не существует, введите целое число от 1 до 7")
    day_number = int(input("Введите номер дня недели "))
if day_number < 6:
    print(f"- {day_number} -> не является выходным")
else:
    print(f"- {day_number} -> выходной")