quarter = int(input("Введите номер четверти от 1 до 4 "))
while quarter != 1 and quarter != 2 and quarter !=3 and quarter !=4:
    print(f"Вы ввели {quarter}")
    quarter = int(input("Введите номер четверти от 1 до 4 "))
if quarter == 1:
    print(f"Для четверти {quarter} все значения X > 0 и все значиния Y > 0")
elif quarter == 2:
    print(f"Для четверти {quarter} все значения X < 0 и все значиния Y > 0")
elif quarter == 3:
    print(f"Для четверти {quarter} все значения X < 0 и все значиния Y < 0")
elif quarter == 4:
    print(f"Для четверти {quarter} все значения X > 0 и все значиния Y < 0")