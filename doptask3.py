"""
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""
x = int(input("Введите значение координаты X "))
while x == 0:
    print(f"Вы ввели {x}")
    x = int(input("Введите целое число, отличное от нуля "))
y = int(input("Введите значение координаты Y "))
while y == 0:
    print(f"Вы ввели {y}")
    y = int(input("Введите целое число, отличное от нуля "))
if y > 0 and x > 0:
    print(f"x={x}; y={y} -> 1")
elif y > 0 and x < 0:
    print(f"x={x}; y={y} -> 2")
elif y < 0 and x > 0:
    print(f"x={x}; y={y} -> 4")
elif y < 0 and x < 0:
    print(f"x={x}; y={y} -> 3")