"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

user_time = int(input("Введите время в секундах "))
print(f"Вы ввели: {user_time}")
hour = user_time // 3600
minute = (user_time - hour * 3600) // 60
second = user_time % 60
print(f"Время в формате чч:мм:сс: {hour}:{minute}:{second}")
