"""моя первая задача на Python"""
X = 10
print(X)

age = int(input("Возраст?"))
print(age)

NAME = "Вася"
print("Привет, " + NAME)
A = 1
print(f"Привет, {NAME}, {A}")
i = 0
while True:
    i += 1
    if i >= 10:
        break
    if i % 2 == 0:
        continue
    print(i)

name = input("Введите свое имя ")
print(name)
